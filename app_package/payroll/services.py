"""
Business logic regarding salary report's flow and data processing.
"""

import json
import logging
from abc import ABC, abstractmethod
from itertools import groupby
from typing import List, NoReturn, Optional

from pydantic import ValidationError

from app_package.payroll.contracts.reporting import (
    EmpWageRecord, EmpWageRequestDto, EmpWageResponseDto,
    WageProcessByDivisionDto,
)
from app_package.settings import RuntimeEnv


class WageReportProcess(ABC):
    """Define the flow and interfaces."""

    def __init__(self, request_dto: EmpWageRequestDto, **toggles):
        """Construct a new SalaryReportProcess object.

        :param request_dto: request object
        :param toggles: key-value pairs as toggles
        :raises TypeError: parsed JSON file but failed to convert into a list type
        """
        for k, v in toggles.items():
            setattr(self, k, v)
        self._logger: logging.Logger = logging.getLogger(__name__)
        self._dataset: List[EmpWageRecord] = []
        self._request_dto = request_dto or EmpWageRequestDto()
        self._response_dto = EmpWageResponseDto()

        list_of_dict: list = self._request_dto.list_of_dict or []
        filepath: Optional[str] = self._request_dto.filepath
        if filepath:
            self.logger.info('Starting reading JSON file: %s', filepath)
            with open(filepath, 'r', encoding='UTF-8') as f:
                try:
                    list_of_dict = json.load(f)
                except json.decoder.JSONDecodeError as ex:
                    self.logger.warning(
                        '[%s] Error while processing raw data from %s', type(ex).__name__, filepath,
                    )
                    return

                if not isinstance(list_of_dict, list):
                    self.logger.info(
                        'Failed reading JSON file as a list type from %s', filepath,
                    )
                    return

        if list_of_dict:
            try:
                self._dataset = EmpWageRecord.to_list_of_obj(list_of_dict=list_of_dict)
            except ValidationError as ex:
                self.logger.warning(
                    '[%s] Error while converting raw data from %s', type(ex).__name__, filepath,
                )
                return

        if self._dataset:
            self.logger.info(
                'Converted JSON data, total %i record(s)', len(list_of_dict),
            )

    @property
    def logger(self) -> logging.Logger:
        """Logger object"""
        return self._logger

    @property
    def request_dto(self) -> EmpWageRequestDto:
        """Input object"""
        return self._request_dto

    @property
    def response_dto(self) -> EmpWageResponseDto:
        """Output object"""
        return self._response_dto

    @property
    def dataset(self) -> List[EmpWageRecord]:
        """Data source typed of List[EmpWageRecord]"""
        return self._dataset

    def get_toggle(self, key: str) -> bool:
        """Get enabled/disabled flag by key.

        :param key: toggle name as key
        :return: toggle's value or False as default
        """
        return getattr(self, key, False)

    def execute(self) -> EmpWageResponseDto:
        """Main flow.
           Steps:
            step1: pre processing
            step2: salary processing
            step3: layout processing
            final step: post processing

        :return: self.response_dto (EmpWageResponseDto)
        :raises ValidationError: invalid model
        :raises ValueError: missing data or cyclic hierarchy detected
        """
        is_ok: bool = False
        try:
            if not self.dataset:
                raise ValueError('your dataset is empty.')

            # Step1: pre processing
            res_pre_process: List[WageProcessByDivisionDto] = self._pre_process()
            if not res_pre_process:
                raise ValueError('Failed to process data source.')

            # Step2: salary processing
            self._salary_process()

            # Step3: layout processing
            self._layout_process()

            # Final step
            self._post_process()
            is_ok = True
        except ValidationError as ex:
            self.logger.warning(
                '[%s] Error while converting model data', type(ex).__name__,
            )
        except ValueError as ex:
            self.logger.warning(
                '[%s] Error while processing salary data', type(ex).__name__,
            )

        self.response_dto.is_success = is_ok
        return self.response_dto

    def _pre_process(self) -> List[WageProcessByDivisionDto]:
        """The 1st step in the flow.
           To compute data from source of @property._dataset into @property.response_dto.
            step1: grouping by manager
            step2: prepare a manager list for quickly lookup by each employee
            step3: prepare depth for each employee in each division
            final step: iter each employee and assign his manager object and division hierarchy

        :return: list of SalaryProcessByDivisionDto
        :raises ValueError: cyclic hierarchy
        """
        self.logger.info('Starting pre processing...')
        res: EmpWageResponseDto = self.response_dto

        # Step1: grouping by manager
        res.top_managers = list(filter(lambda x: not x.mgr_id, self.dataset))
        dataset_exclude_topmgr = list(filter(lambda x: x.mgr_id, self.dataset))
        group_by_mgr = groupby(dataset_exclude_topmgr, lambda x: x.mgr_id)
        mgrs: dict[(int, EmpWageRecord)] = {}

        for mgr in self.dataset:
            mgrs[mgr.emp_id] = mgr

        # Step2: prepare a manager list
        for top_mgr in res.top_managers:
            # Store top manager's object for lookup afterwards
            top_mgr.depth = 1
            top_mgr.manager_record = top_mgr

        # Step3: division process
        for mgr_id, grp in group_by_mgr:
            higher_mgr: Optional[EmpWageRecord] = next(
                (e for e in self.dataset if e.emp_id == mgr_id), None,
            )
            if higher_mgr is None:
                continue

            # Store manager's object for lookup afterwards
            mgrs[mgr_id] = higher_mgr
            higher_mgr.depth = 1
            my_manager: Optional[EmpWageRecord] = higher_mgr
            # Prepare depth for each manager depens on his/her nested manager
            while my_manager is not None:
                higher_mgr.depth += 1
                if higher_mgr.depth > RuntimeEnv.MAX_HIERARCHY:
                    raise ValueError(
                        f'Exceed max depth={RuntimeEnv.MAX_HIERARCHY} (manager={mgr_id})',
                    )

                my_manager = mgrs[my_manager.mgr_id] if my_manager.mgr_id else None
                if my_manager is not None and my_manager.emp_id == mgr_id:
                    raise ValueError(f'Cyclic hierarchy (manager={mgr_id})')

            # Prepare depth for each employee in each division
            employees: List[EmpWageRecord] = []
            for emp in grp:
                employees.append(emp)
                if emp.manager_record is not None:
                    emp.manager_record = higher_mgr
                    emp.depth = higher_mgr.depth + 1

            # Division segmented data are ready!
            division = WageProcessByDivisionDto(employees=employees, manager=higher_mgr)
            res.divisions.append(division)
        self.logger.info('Finished pre processing.')

        return res.divisions

    @abstractmethod
    def _salary_process(self) -> int:
        """The 2nd step in the flow.
           To compute salary from
            source of @property.response_dto.divisions
            and @property.response_dto.top_managers.

        :return: the number of total salary
        """

    @abstractmethod
    def _layout_process(self) -> str:
        """The 3rd step in the flow.
           To render report's layout from
            source of @property.response_dto.divisions
            and @property.response_dto.top_managers.

        :return: the rendered ascii text
        """

    def _post_process(self) -> NoReturn:
        """The last step in the flow."""


class WageReportDemoProcess(WageReportProcess):
    """Implement the flow and interfaces."""

    def _salary_process(self) -> int:
        """The 2nd step in the flow.
           To compute salary from
            source of @property.response_dto.divisions
            and @property.response_dto.top_managers.

        :return: the number of total salary
        """
        self.logger.info('Starting salary processing...')
        res: EmpWageResponseDto = self.response_dto
        total_salary: int = 0
        mgr_salary: int = 0
        for division in res.divisions:
            mgr_salary = division.manager.salary if division.manager else 0
            emp_salary: int = 0
            for emp in division.employees:
                emp_salary += emp.salary
            if not RuntimeEnv.INCLUDE_DIV_MGR_SALARY_ENABLED:
                mgr_salary = 0
            division.salary = mgr_salary + emp_salary
            total_salary += division.salary

        for mgr in res.top_managers:
            mgr_salary = mgr.salary
            if not RuntimeEnv.INCLUDE_TOP_MGR_SALARY_ENABLED:
                mgr_salary = 0
            total_salary += mgr_salary

        self.logger.info('Finished salary processing.')
        res.total_salary = total_salary

        return total_salary

    def _layout_process(self) -> str:
        """The 3rd step in the flow.
           To render report's layout from
            source of @property.response_dto.divisions
            and @property.response_dto.top_managers.

        :return: the rendered ascii text
        """
        self.logger.info('Starting layout processing...')
        res: EmpWageResponseDto = self.response_dto
        lines: List[str] = []
        lines.append(f'Salary Report ({res.title})')
        lines.append('===')
        lines.append(f'({len(res.top_managers)}) Top Managers:')

        for top_mgr in res.top_managers:
            top_mgr.indent = self.__padding_left(depth=top_mgr.depth)
            lines.append(f'{top_mgr.indent}{top_mgr.first_name}')

        lines.append('')
        lines.append(f'({len(res.divisions)}) Divisions:')

        for division in sorted(res.divisions, key=lambda x: x.manager.depth if x.manager else 0):
            if division.manager is None:
                continue
            div_mgr: EmpWageRecord = division.manager
            div_mgr.indent = self.__padding_left(depth=div_mgr.depth)

            lines.append('')
            lines.append(f'{div_mgr.indent}Employees of: {div_mgr.first_name}')

            for emp in sorted(division.employees, key=lambda x: x.first_name):
                emp.indent = self.__padding_left(depth=emp.depth)
                lines.append(f'{emp.indent}∟{emp.first_name}')
            lines.append(f'{div_mgr.indent}Salary above: {division.salary}')

        lines.append('===')
        lines.append(f'Total Salary: {res.total_salary}')

        res.body = '\r\n'.join(lines)
        self.logger.info('Finished layout processing.')

        return res.body

    def __padding_left(self, depth: int, padding_char: str = '    ') -> str:
        """Internal utility to put prefix string.

        :param depth: to duplicate a number of padding_char
        :param padding_char: padding word
        :return: the left padding string
        """
        return padding_char * (depth or 0)

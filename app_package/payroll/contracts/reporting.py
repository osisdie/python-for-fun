"""
Domain models for HR/Payroll module.
"""
import logging
from typing import List, Optional

from pydantic import Field, ValidationError

from app_package.hr.models import EmployeeBaseDto
from app_package.protocols.contracts import RequestBaseDto, ResponseBaseDto


class EmpWageRecord(EmployeeBaseDto):
    """Basic model used for salary report's data processing."""
    # Employee's salary.
    salary: int = Field(default=0)

    # Refer to a manager object if this employee has a managr.
    manager_record: Optional[__name__] = None

    # Prefix chararcters while printing.
    indent: str = Field(default='')

    # The depth under organization hierarchy.
    depth: int = Field(default=0)

    @staticmethod
    def is_self_mgr(rec: EmployeeBaseDto) -> bool:
        """Check if record has no manager.

        :param rec: source data
        :return: True if match conditions, otherwise False
        """
        return rec and (not rec.mgr_id or rec.emp_id == rec.mgr_id)

    @staticmethod
    def to_list_of_obj(list_of_dict: List[dict]) -> List[__name__]:
        """Type convert from list of dictionary to list of EmpWageRecord object.

        :param list_of_dict: list of dictionary.
        :return: a List[EmpWageRecord]
        :raises ValidationError: Invalid model
        """
        converted_list: List[EmpWageRecord] = []
        for i, item in enumerate(list_of_dict):
            try:
                converted_list.append(
                    EmpWageRecord(
                        emp_id=item.get('id'),
                        first_name=item.get('first_name'),
                        salary=item.get('salary'),
                        mgr_id=item.get('manager'),
                    ),
                )
            except ValidationError as ex:
                msg = ex.errors()[0].get('msg') if ex.errors else 'invalid model'
                logging.warning(
                    '[%s] %s (record index=%i)', type(ex).__name__, msg, i,
                )
                raise

        return converted_list


class EmpWageRequestDto(RequestBaseDto):
    """Request model used for salary report's data processing."""

    def __init__(
        self,
        filepath: Optional[str] = None,
        list_of_dict: Optional[List[EmpWageRecord]] = None,
    ):
        """Construct a new EmpWageRequestDto object.

        :param filepath: a JSON file path
        :param list_of_dict: parsed JSON object in the list
        """
        super().__init__()

        self.title: str = ''  # Report's title.
        self.filepath: Optional[str] = filepath  # JSON file path
        self.list_of_dict: Optional[List[EmpWageRecord]] = list_of_dict


class EmpWageResponseDto(ResponseBaseDto):
    """Response model used for salary report's data processing."""

    def __init__(self):
        """Construct a new EmpWageResponseDto object."""
        super().__init__()

        self.title: str = 'Empty'  # Report's title.
        self.body: str = 'Empty'  # Report's body.
        self.total_salary: int = 0  # Sum of all salary from all departments
        self.top_managers: List[EmpWageRecord] = []  # List[EmpWageRecord]
        self.divisions: List[WageProcessByDivisionDto] = []  # List[WageProcessByDivisionDto]


class WageProcessByDivisionDto(object):
    """Collection salary of employees including the manager and members."""

    def __init__(self, employees: List[EmpWageRecord], manager: Optional[EmpWageRecord] = None):
        """Construct a new SalaryProcessByDivisionDto object.

        :param employees: member's total payroll
        :param manager: manager's payroll
        """
        self.emp_id: int = 0  # Manager's employee_id
        self.manager: Optional[EmpWageRecord] = manager  # Manager's ref object
        self.employees: List[EmpWageRecord] = employees  # Employees who report to this manager
        self.salary: int = 0  # Manager's salary

# EmpWageRecord.model_rebuild()

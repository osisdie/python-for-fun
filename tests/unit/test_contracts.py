"""
Test payroll module
"""
# pylint: disable=broad-except
import json

import pytest

# from app_package.payroll.contracts.reporting import EmpWageRequestDto
# from app_package.payroll.services import WageReportDemoProcess


# @pytest.mark.skip(reason='skip temporarily due to ci error')
# def test_postive_byfile(file_path):
#     """To test a executed report from json file."""
#     request_dto: EmpWageRequestDto = EmpWageRequestDto(filepath=file_path)
#     service: WageReportDemoProcess = WageReportDemoProcess(request_dto=request_dto)
#     assert service.dataset


# @pytest.mark.skip(reason='skip temporarily due to ci error')
# def test_postive_bylist():
#     """To test a executed report from list object."""
#     raw: str = '[{"id": 1,"first_name": "Dave","manager": 2,"salary": 100000}\
#         ,{"id": 2,"first_name": "Jeff","manager": null,"salary": 110000}\
#         ,{"id": 3,"first_name": "Andy","manager": 1,"salary": 90000}\
#         ,{"id": 4,"first_name": "Jason","manager": 1,"salary": 80000}\
#         ,{"id": 5,"first_name": "Dan","manager": 1,"salary": 70000}\
#         ,{"id": 6,"first_name": "Rick","manager": 1,"salary": 60000}\
#         ,{"id": 9,"first_name": "Suzanne","manager": 1,"salary": 80000}]'
#     list_of_dict: list = json.loads(raw)
#     assert len(list_of_dict) > 0

#     request_dto: EmpWageRequestDto = EmpWageRequestDto(list_of_dict=list_of_dict)
#     service: WageReportDemoProcess = WageReportDemoProcess(request_dto=request_dto)
#     assert service.dataset

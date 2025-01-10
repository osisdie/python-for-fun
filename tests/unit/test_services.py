"""
Test payroll module
"""
# pylint: disable=broad-except
import pytest

# from app_package.payroll.contracts.reporting import (
#     EmpWageRequestDto, EmpWageResponseDto,
# )
# from app_package.payroll.services import WageReportDemoProcess


# @pytest.mark.skip(reason='skip temporarily due to ci error')
# def test_postive_byfile(file_path):
#     """To test a executed report from json file."""
#     assert RuntimeEnv.DATA_PATH is not None
#     request_dto: EmpWageRequestDto = EmpWageRequestDto(filepath=file_path)
#     service: WageReportDemoProcess = WageReportDemoProcess(request_dto=request_dto)
#     result: EmpWageResponseDto = service.execute()
#     assert result.is_success
#     assert result.total_salary > 0
#     assert result.top_managers
#     assert result.divisions

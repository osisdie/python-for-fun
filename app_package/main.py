"""
Application Start
"""
# !/usr/bin/env python
# pylint: disable=broad-except

import argparse
import os
import sys

from app_package.payroll.contracts.reporting import (
    EmpWageRequestDto, EmpWageResponseDto,
)
from app_package.payroll.services import WageReportDemoProcess
from app_package.settings import RuntimeEnv


def print_hierarchy_v1():
    """Main function"""
    print('\r\n*****V1 Start*****')
    request_dto = EmpWageRequestDto(filepath=RuntimeEnv.DATA_PATH)
    service = WageReportDemoProcess(request_dto=request_dto)

    # core method
    result: EmpWageResponseDto = service.execute()
    print(result.body)
    print('V1 Completed!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Json information')
    parser.add_argument('--file', dest='file', type=str, help='Json file path')
    args = parser.parse_args()

    if args and args.file:
        RuntimeEnv.DATA_PATH = args.file

    print(f'SDK_ENV={RuntimeEnv.SDK_ENV}')
    print(f'DATA_PATH={RuntimeEnv.DATA_PATH}')

    if not os.path.exists(RuntimeEnv.DATA_PATH):
        print(f'[{RuntimeEnv.SDK_ENV}]json file not found: {RuntimeEnv.DATA_PATH}')
        sys.exit(1)

    print_hierarchy_v1()

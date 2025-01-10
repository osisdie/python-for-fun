# """
# Test performance
# """
# import pytest

# from app_package.exam.athena.service import PrintEmployeeService


# def print(json_path, recursive_enabled, cache_enabled):
#     """Regular print function"""
#     service = PrintEmployeeService(**{
#         'recursive_enabled': recursive_enabled,
#         'cache_enabled': cache_enabled
#     })
#     service.execute(json_path=json_path)


# def my_special_setup():
#     """Setup"""


# @pytest.fixture(scope='function')
# def resource():
#     """Resource"""
#     return './res/employees1.json'


# # @pytest.mark.skip(reason='skip temporarily due to ci error')
# @pytest.mark.parametrize('print_recursive_enabled', [False, True])
# @pytest.mark.parametrize('leveling_recursive_cache_enabled', [False, True])
# def test_profilio(benchmark, resource, print_recursive_enabled, leveling_recursive_cache_enabled):
#     """basic test cases as benchmark"""
#     benchmark.pedantic(
#         lambda: print(resource, print_recursive_enabled, leveling_recursive_cache_enabled),
#         rounds=100,
#         iterations=5
#     )

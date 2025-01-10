"""
Domain models for HR module.
"""
from typing import Optional

from pydantic import BaseModel, validator

from app_package.settings import RuntimeEnv


class EmployeeBaseDto(BaseModel):
    """Base calss of employee."""
    emp_id: int
    first_name: str
    mgr_id: Optional[int] = None

    @validator('first_name')
    def first_name_rule(cls, val: str):
        """Validate `first_name` property.

        :param val: first name.
        :raises ValueError: an invalid first name
        """
        if val and len(val) >= RuntimeEnv.MIN_LEN_USERNAME:
            return val
        raise ValueError('first_name is invalid')

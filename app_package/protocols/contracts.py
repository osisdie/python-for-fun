"""
Fundamental request and response models.
"""
from typing import List


class RequestBaseDto(object):
    """General purpose request model."""

    def __init__(self):
        """Construct a new RequestBaseDto object."""
        self.fields: List[str] = []  # List of extra query fields
        self.ext: dict = {}  # Additional dict information


class ResponseBaseDto(object):
    """General purpose response model."""

    def __init__(self):
        """Construct a new ResponseBaseDto object."""
        self.is_success: bool = False
        self.msg: str = ''
        self.code: int = 0
        self.data: object = None  # {}
        self.errors: object = None  # {}
        self.ext: dict = {}  # dict()

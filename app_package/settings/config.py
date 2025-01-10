"""
App settings for python-for-fun project.
"""


class Common(object):
    """Common/Shared/SDK configs."""
    SDK_ENV: str = 'local'
    DATA_PATH: str = 'res/salary.json'
    DEBUG: bool = False
    INCLUDE_DIV_MGR_SALARY_ENABLED: bool = False
    INCLUDE_TOP_MGR_SALARY_ENABLED: bool = False
    MIN_LEN_USERNAME: int = 3
    MAX_HIERARCHY: int = 100


class Local(Common):
    """Specified for local/debug environment."""
    SDK_ENV = 'local'
    DATA_PATH = 'res/salary.json'
    DEBUG = True


class Development(Common):
    """Specified for development/developer environment."""
    SDK_ENV = 'dev'
    DATA_PATH = 'res/salary.json'
    DEBUG = True


class Testing(Development):
    """Specified for testing/QA environment.
    Overwrite development settings.
    """
    SDK_ENV = 'tst'
    DATA_PATH = 'res/salary_tst.json'
    DEBUG = True


class Production(Common):
    """Specified for production environment."""
    SDK_ENV = 'prod'
    DATA_PATH = 'res/salary.json'
    DEBUG = False


class Staging(Production):
    """Specified for staging/pre-production environment.
    Overwrite production settings.
    """
    DATA_PATH = 'res/salary_stg.json'
    DEBUG = True

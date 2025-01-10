"""
Global configuration class
"""
import os
from typing import Optional

from app_package.settings.config import (
    Common, Development, Local, Production, Staging, Testing,
)

app_env: Optional[str] = os.getenv('APP_ENV', None)
env: Optional[str] = app_env and app_env.casefold()
RuntimeEnv: Common = Local()

if env is None:
    raise EnvironmentError('APP_ENV environment variable is not set.')

if env == 'local':
    RuntimeEnv = Local()
elif env == 'development':
    RuntimeEnv = Development()
elif env == 'testing':
    RuntimeEnv = Testing()
elif env == 'staging':
    RuntimeEnv = Staging()
elif env == 'production':
    RuntimeEnv = Production()
else:
    raise EnvironmentError(f'app_env is unexpected value: {app_env}')

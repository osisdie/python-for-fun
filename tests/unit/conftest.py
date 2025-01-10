import logging
import os

import pytest

from app_package.settings import RuntimeEnv


@pytest.fixture(name='file_path')
def fixture_file_path() -> str:
    return RuntimeEnv.DATA_PATH


def create_logger(app_name):
    """Create a logging interface"""
    logging_level = os.environ.get('LOG_LEVEL', logging.INFO)
    logging.basicConfig(
        level=logging_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    logger = logging.getLogger(app_name)
    return logger


# create logger
logger = create_logger('testing')
logger.info('start testing...')

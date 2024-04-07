import logging
import os

from dotenv import load_dotenv
from pydantic import BaseConfig

load_dotenv()


class GlobalConfig(BaseConfig):
    title: str = os.environ.get("TITLE")
    version: str = "1.0.0"
    description: str = os.environ.get("DESCRIPTION")
    log_format: str = os.environ.get("LOG_FORMAT")
    logging_level: int = logging.DEBUG


settings = GlobalConfig()

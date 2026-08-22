import configparser
import os
from pathlib import Path


DEFAULT_API_BASE_URL = "https://images.ygoprodeck.com/images/"
ENV_API_BASE_URL = "YGO_API_BASE_URL"

DEFAULT_REQUEST_DELAY = 1
ENV_REQUEST_DELAY = "YGO_API_REQUEST_DELAY"


class Config:
    def __init__(self, config_path: Path | None = None):
        self.config_path = config_path or Path("config.conf")
        self.api_base_url = self._get_api_base_url()
        self.request_delay = self._get_request_delay()

    def _get_api_base_url(self) -> str:
        # 1. Environment variable
        if value := os.getenv(ENV_API_BASE_URL):
            return value

        # 2. Config file
        if self.config_path.exists():
            parser = configparser.ConfigParser()
            parser.read(self.config_path)

            if parser.has_option("api", "base_url"):
                return parser.get("api", "base_url")

        # 3. Default
        return DEFAULT_API_BASE_URL

    def _get_request_delay(self) -> int:
        # 1. Environment variable
        if value := os.getenv(ENV_REQUEST_DELAY):
            return int(value)

        # 2. Config file
        if self.config_path.exists():
            parser = configparser.ConfigParser()
            parser.read(self.config_path)

            if parser.has_option("api", "request_delay"):
                return parser.getint("api", "request_delay")

        # 3. Default
        return DEFAULT_REQUEST_DELAY

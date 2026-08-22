import time
from pathlib import Path

import requests

from .config import Config


class ApiClient:
    def __init__(self, config: Config):
        self.config = config
        self.base_url = config.api_base_url.rstrip("/")

    def download_image(
        self,
        image_endpoint: str,
        image_id: int,
        output_path: Path,
    ) -> bool:
        url = f"{self.base_url}/{image_endpoint.lstrip('/')}/{image_id}.jpg"

        response = requests.get(url)

        if response.status_code == 404:
            print(f"Image not found: {url}")
            return False

        response.raise_for_status()

        output_path.write_bytes(response.content)
        return True

    def download_images(
        self,
        image_endpoint: str,
        output_path: Path,
        cards: list,
    ):
        for card in cards:
            output_file = output_path / f"{card['id']}.jpg"
            self.download_image(
                image_endpoint,
                card["id"],
                output_file,
            )

            time.sleep(self.config.request_delay)

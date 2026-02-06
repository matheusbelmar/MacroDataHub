import json
import requests as req
from pathlib import Path

class IBGEScraper:
    BASE_URL = 'https://apisidra.ibge.gov.br/'

    def __init__(
            self, 
            code:         str, 
            landing_dir:  Path
            ):
        
        self.code = code
        self.landing_dir = landing_dir

    def build_request(self) -> str:
        if not self.code:
            raise ValueError("Code is required for SIDRA scraper.")
        return r"{}values/{}?formato=json".format(self.BASE_URL, self.code)

    def fetch(self, 
              url: str
              ) -> None:
        response = req.get(url)
        response.raise_for_status()

        self.landing_dir.mkdir(parents=True, exist_ok=True)
        output_path = self.landing_dir / "raw.json"

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)

        return output_path

    def scrape(self):
        request=self.build_request()
        return self.fetch(request)
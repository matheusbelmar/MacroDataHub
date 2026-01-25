import requests as req
from macrodatahub.adapters.outbound.storage.local_storage import LocalStorageAdapter as LSA

class IBGEScraper:
    BASE_URL = 'https://apisidra.ibge.gov.br/'

    def __init__(
            self, 
            code:  str, 
            path:  str,
            cache: bool = False):
        
        self.code = code
        self.Raw_path = path
        self.Storage = LSA()

    def build_request(self) -> str:
        if not self.code:
            raise ValueError("Code is required for SIDRA scraper.")
        format_suffix = f"values/{self.code}?formato=json"
        return self.BASE_URL + format_suffix

    def fetch(self) -> list:
        url = self.build_request()
        response = req.get(url)
        #response.raise_for_status()
        return response.json()

    def Scrap(self):
        Response=self.fetch()
        self.Storage.save_raw(
                base_path=self.Raw_path,
                data=Response,
                ext = 'json')


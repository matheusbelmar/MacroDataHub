import requests as req

class IBGEScraper:
    BASE_URL = 'https://apisidra.ibge.gov.br/'

    def __init__(
            self, 
            code:          str, 
            landing_path:  str
            ):
        
        self.code = code
        self.Landing_path = landing_path

    def build_request(self) -> str:
        if not self.code:
            raise ValueError("Code is required for SIDRA scraper.")
        format_suffix = f"values/{self.code}?formato=json"
        return self.BASE_URL + format_suffix

    def fetch(self, 
              url: str
              ) -> None:
        response = req.get(url)
        #response.raise_for_status()
        return response.json()

    def Scrap(self):
        request=self.build_request()
        self.fetch(request)
        self.Storage.save_raw(
                base_path=self.Raw_path,
                data=Response,
                ext = 'json')


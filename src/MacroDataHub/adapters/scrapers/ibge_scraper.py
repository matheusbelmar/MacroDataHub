
# Conteúdo de adapters/scrapers/ibge_scraper.py
import json
import requests as req
import pandas as pd
from core.models.series import Series
from adapters.storage.local_storage import LocalStorageAdapter as LSA

class IBGEScraper:
    BASE_URL = 'https://apisidra.ibge.gov.br/'

    def __init__(self, name: str, code: str, path:str, req_config: dict = {}):
        self.name = name
        self.code = code
        self.Dumper = LSA(base_path= path)
        
        
        self.req_config = req_config

    def build_url(self) -> str:
        if not self.code:
            raise ValueError("Code is required for SIDRA scraper.")
        format_suffix = f"values/{self.code}?formato=json"
        return self.BASE_URL + format_suffix

    def fetch(self) -> list:
        url = self.build_url()
        response = req.get(url)
        #response.raise_for_status()
        return response.json()

    def parse(self, raw_data: list) -> pd.DataFrame:
        # Transforma a resposta JSON em DataFrame. Simplificado.
        return pd.json_normalize(raw_data)

    def to_series(self) -> Series:
        raw_data = self.fetch()
        df = self.parse(raw_data)
        return Series(
            name=self.name,
            source="ibge",
            data=df,
            path=f"ibge/{self.name.lower()}"
        )
    
    def run(self):
        Response=self.fetch()
        self.Dumper.save_raw(series_id=self.name,
                             data=Response)

scraper=IBGEScraper(name="IPCA", 
                    code=r"T/7060/P/all/V/63/C315/all/N1/1", 
                    path='/home/mbelmar/Documentos/Programaçao - Projetos/Projetos/MacroDataHub/data/raw_storage')

scraper.run()

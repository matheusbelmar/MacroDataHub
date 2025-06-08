import json
import requests as req
from src.MacroDataHub.extract.Super import DataImporter

class Scraper(DataImporter):
    def __init__(self, name, code, req_config = {}):
        BASE_URL  = r'https://apisidra.ibge.gov.br/'

    def build_url(self):

        """Builds SIDRA-specific URL using the 'code' and other config."""
        if not self.code:
            raise ValueError("Code is required for SIDRA scraper.")
        
        """For later features"""
        if "Req_Build" not in self.req_config:
            format_suffix = r'values/{}?formato=json'.format(self.code)
        
        return self.BASE_URL+format_suffix

    def fetch(self):
        response=req.get(self.Base_link).json()
        return response
    
    def save(self, response):
        with open("data/raw_storage/{}.json".format(self.data_name), 'w', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)
    
    def run(self):
        response=self.fetch
        self.save(response)
import os
import json
import pandas as pd
import requests as req
from Projetos.MacroDataHub.src.MacroDataHub.extract.SuperClass import BaseScraper


os.chdir(r"/home/mbelmar/Documentos/Programaçao - Projetos/Projetos/MacroDataHub/src")

class Scraper(BaseScraper):
    def __init__(self, name, code):
        self.Base_link  = r'https://apisidra.ibge.gov.br/values/{}?formato=json'.format(code)
        self.Code       = code
        self.data_name  = name

    def fetch(self):
        response=req.get(self.Base_link).json()
        return response
    
    def save(self, response):
        with open("data/raw_storage/{}.json".format(self.data_name), 'w', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)
    
    def run(self):
        response=self.fetch
        self.save(response)

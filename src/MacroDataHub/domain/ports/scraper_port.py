from abc import ABC, abstractmethod

class ScraperPort(ABC):
    @abstractmethod
    def parse(self, raw_data, schema: dict):
        pass
    
    @abstractmethod
    def build_url(self, code):
        pass

    @abstractmethod
    def fetch(self, url):
        pass
    
    @abstractmethod
    def Scrap(self):
        pass
    
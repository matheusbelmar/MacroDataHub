from abc import ABC, abstractmethod

class DataImporter(ABC):
    
    def __init__(self
                 ,name  :str
                 ,code  :str
                 ,source:str
                 ,req_config:dict={}):
        self.name = name
        self.code = code
        self.source = source
        self.req_config = req_config 

    @abstractmethod
    def fetch_data(self) -> dict:
        pass

    @abstractmethod
    def build_url(self) -> str:
        """Builds the final API URL based on code/config."""
        pass

    @abstractmethod
    def save_data(self) -> None:
        pass
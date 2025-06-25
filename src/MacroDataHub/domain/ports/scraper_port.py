from abc import ABC, abstractmethod

class ScraperPort(ABC):
    @abstractmethod
    def parse(self, raw_data, schema: dict):
        pass
from abc import ABC, abstractmethod


class CleanerPort(ABC):
    @abstractmethod
    def parse(self, raw_data, schema: dict):
        pass
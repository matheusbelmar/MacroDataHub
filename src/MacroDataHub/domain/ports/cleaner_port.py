from abc import ABC, abstractmethod


class CleanerPort(ABC):
    @abstractmethod
    def Transform(self, raw_data, schema: dict):
        pass
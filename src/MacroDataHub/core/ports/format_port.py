from abc import ABC, abstractmethod
from core.models.series import Series

class FormatPort(ABC):
    @abstractmethod
    def format(self, series: Series) -> bytes:
        pass
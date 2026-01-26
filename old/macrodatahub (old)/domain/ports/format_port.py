from abc import ABC, abstractmethod
from macrodatahub.domain.models.series import Series

class FormatPort(ABC):
    @abstractmethod
    def format(self, series: Series) -> bytes:
        pass
# Conteúdo de core/ports/storage_port.py
from abc import ABC, abstractmethod
from core.models.series import Series

class StoragePort(ABC):
    @abstractmethod
    def save(self, series: Series, dest: str):
        pass
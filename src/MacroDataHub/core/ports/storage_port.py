from abc import ABC, abstractmethod

class StoragePort(ABC):
    @abstractmethod
    def save_raw(self, series_id: str, data: dict) -> None:
        """Store raw data given a unique series ID"""
        pass
#
#    @abstractmethod
#    def load_raw(self, series_id: str) -> dict:
#        """Load raw data given a series ID"""
#        pass
#
#    @abstractmethod
#    def save_curated(self, series_id: str, df) -> None:
#        """Store parsed/curated data (e.g., a DataFrame)"""
#        pass
#
#    @abstractmethod
#    def load_curated(self, series_id: str):
#        """Load curated data"""
#        pass
# application/services/series_service.py

from domain.ports.scraper_port import ScraperPort
from domain.ports.storage_port import StoragePort
from domain.ports.format_port import FormatPort
from catalog.registry import Catalog
from domain.models.series import Series


class SeriesService:
    def __init__(
            self,
            formatter: FormatPort,
            catalog: Catalog
            ):
        self.formatter = formatter
        self.catalog = catalog


    def download(
        self,
        series: Series,
        clean: bool = True,
        dump: bool = False,
        register: bool = False
    ):
        """Download series from source.

        Args:
            series (Series): Series object.
            clean (bool): Apply parsing using schema.
            dump (bool): Save file to storage.
            register (bool): Register in catalog.

        Returns:
            DataFrame or raw data.
        """
        raw_data = self.scraper.fetch(series.code)

        data = (
            self.formatter.parse(raw_data, series.schema)
            if clean
            else raw_data
        )

        if dump:
            self.storage.save_raw(series.name, raw_data)
            if clean:
                self.storage.save_clean(series.name, data)

        if register:
            self.catalog.register_series(series)

        return data


    def load(
        self,
        series_name: str,
        clean: bool = True
    ):
        """Load series from storage.

        Args:
            series_name (str): Name in catalog.
            clean (bool): Parse raw data into DataFrame.

        Returns:
            DataFrame or raw data.
        """
        if not self.catalog.is_registered(series_name):
            raise Exception(f"Series '{series_name}' not registered.")

        raw_data = self.storage.load_raw(series_name)

        if clean:
            series = self.catalog.get_series(series_name)
            data = self.formatter.parse(raw_data, series.schema)
            return data

        return raw_data


    def upload(
        self,
        series_name: str
    ):
        """Upload stored series to external storage (e.g., MinIO).

        Args:
            series_name (str): Series identifier.

        Returns:
            bool: Success.
        """
        if not self.catalog.is_registered(series_name):
            raise Exception(f"Series '{series_name}' not registered.")

        local_path = self.catalog.get_local_path(series_name)
        self.storage.upload(local_path)

        return True


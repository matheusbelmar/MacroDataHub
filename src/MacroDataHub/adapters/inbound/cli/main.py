from adapters.outbound.scrapers.ibge_scraper import IBGEScraper
from adapters.outbound.storage.local_storage import LocalStorage
from adapters.outbound.formats.parquet_formatter import ParquetFormatter
from application.services.series_service import SeriesService
from catalog.registry import Catalog
from domain.models.series import Series


def main():
    scraper = IBGEScraper()             # Outbound adapter
    storage = LocalStorage()            # Outbound adapter
    formatter = ParquetFormatter()      # Outbound adapter
    catalog = Catalog()                 # Infra adapter

    service = SeriesService(
        scraper=scraper,
        storage=storage,
        formatter=formatter,
        catalog=catalog
    )

    series = Series(
        name="ipca_brasil",
        source="IBGE",
        code="7060",
        schema={"date": "column_a", "value": "column_b"}
    )

    df = service.download(series, clean=True, dump=True, register=True)
    print(df)


if __name__ == "__main__":
    main()
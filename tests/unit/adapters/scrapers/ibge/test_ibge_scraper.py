import pytest
from pathlib import Path
from mdb import IBGEScraper

def test_ibge_scraper(tmp_path, mocker):
    # mock correto (mesmo namespace)
    mock_get = mocker.patch("mdb.adapters.scrapers.ibge.ibge_scraper.req.get")

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"serie": "IPCA"}

    scraper = IBGEScraper(
        code="T/7060/P/all/V/63/C315/all/N1/1",
        landing_dir=tmp_path
    )

    path = scraper.scrape()

    assert path.exists()
    assert path.name == "raw.json"
    mock_get.assert_called_once()
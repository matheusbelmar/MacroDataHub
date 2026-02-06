import shutil
import pytest
from pathlib import Path
from mdb import IBGEScraper

@pytest.mark.integration
def test_ibge_actual_api_call(tmp_path):

    scraper = IBGEScraper(
        code="T/7060/P/all/V/63/C315/all/N1/1",
        landing_dir=tmp_path
    )
    
    # Tenta baixar de verdade
    path = Path(scraper.scrape())

    assert path.exists()
    assert path.stat().st_size > 0

    shutil.copy(path, Path("tests/integration/scrapers/ibge/fixtures") / path.name)

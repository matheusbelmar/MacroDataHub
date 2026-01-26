import pytest
from mdb import IBGEScraper

@pytest.mark.integration
def test_ibge_actual_api_call(stage_dir):
    """
    INTEGRATION TEST: Valida a conexão real com o provedor de dados.
    """
    scraper = IBGEScraper(
        nome_serie="ipca_real", 
        codigo_serie="1730", 
        stage_path=stage_dir
    )
    
    # Tenta baixar de verdade
    try:
        path = scraper.scrap()
        assert path.exists()
        assert path.stat().st_size > 0
    except Exception as e:
        pytest.fail(f"A integração com o IBGE falhou: {e}")
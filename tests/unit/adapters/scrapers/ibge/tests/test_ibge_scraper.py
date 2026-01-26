import pytest
from mdb import IBGEScraper

def test_ibge_scraper_logic(stage_dir, mocker):
    """
    UNIT TEST: Testa se o scraper salva o arquivo no lugar certo
    e se usa os parâmetros corretos, sem tocar na internet.
    """
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = "data;valor\n2026-01;10.5"

    scraper = IBGEScraper(
        nome_serie="ipca_test", 
        codigo_serie=r"T/7060/P/all/V/63/C315/all/N1/1",
        stage_path=stage_dir
    )
    
    path = scraper.scrap()
    
    # Valida comportamento interno
    assert path.name == "ipca_test.csv"
    assert mock_get.called
    mock_get.assert_called_with(
        "https://api.ibge.gov.br/v1/series/1730", # Exemplo de URL
        timeout=30
    )
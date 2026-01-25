import pytest
# O ponto indica que estamos subindo um nível para achar o módulo vizinho
# Se você estiver usando "pip install -e .", pode usar: from ibge.ibge_scraper import IBGEScraper
from ..ibge_scraper import IBGEScraper

def test_ibge_scrap_process(stage_dir):
    """
    Testa a classe IBGEScraper passando os parâmetros no __init__
    e executando o método scrap.
    """
    
    nome = "ipca"
    codigo = r"T/6381/P/all/V/all/N1/1"
    caminho_stage = stage_dir 

    # 2. Inicialização da classe (passando os inputs solicitados)
    scraper = IBGEScraper(
        nome_serie=nome, 
        codigo_serie=codigo, 
        stage_path=caminho_stage
    )

    # 3. Chamada da função Scrap
    resultado = scraper.scrap()

    # 4. Verificações (Asserts)
    assert resultado is not None
    # Verifica se o arquivo foi criado dentro da pasta de stage correta
    assert (caminho_stage / f"{nome}.csv").exists()


scraper=IBGEScraper(code=r"T/6381/P/all/V/all/N1/1", 
                    path='/home/mbelmar/Documentos/Programaçao - Projetos/Projetos/MacroDataHub/data/raw_storage')
scraper.Scrap()
import pytest
import shutil

@pytest.fixture
def stage_dir(tmp_path):
    """
    Cria uma pasta temporária de stage para o scraping.
    O pytest limpa isso automaticamente após os testes.
    """
    d = tmp_path / "pipelines_teste/ibge" 
    d.mkdir()
    yield d
    # Opcional: limpeza extra pós-teste se necessário
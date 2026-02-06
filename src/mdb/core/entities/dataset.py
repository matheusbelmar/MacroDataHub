from dataclasses import dataclass
import pandas as pd

@dataclass
class MacroDataset:
    """O contrato de saída de qualquer cleaner do framework."""
    data: pd.DataFrame  # Com colunas padronizadas: ['date', 'value', 'index_code']
    provider: str
    series_name: str
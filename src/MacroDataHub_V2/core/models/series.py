from dataclasses import dataclass
import pandas as pd

@dataclass
class Series:
    name: str
    source: str
    data: pd.DataFrame
    path: str   # caminho relativo para salvar a série
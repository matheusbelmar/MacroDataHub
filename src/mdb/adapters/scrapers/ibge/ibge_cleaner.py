import pandas as pd
from pathlib import Path
from typing import Optional

class IBGEScleaner:
    BASE_URL = 'https://apisidra.ibge.gov.br/'

    def __init__(
            self, 
            name: str, 
            landing_path: Path,
            raw: Optional[bool] = False,
            serialize: Optional[bool] = False
            ):
        self.name               = name
        self.landing_path       = landing_path
        self.raw_delivery       = raw
        self.serial_delivery    = serialize

    def load(
            self, 
            path: Path) -> pd.DataFrame:
        return pd.read_json(path)


    def cleaner_stg1(
            self, 
            ds_raw: pd.DataFrame
            ) -> pd.DataFrame:

        if self.raw_delivery:
            df_tgt = ds_raw.copy()
        if self.serial_delivery:
            raise KeyError
        else: 
            tgt_cols = ["D1C", "NC", "NN", "MN", "D3C", "D3N", "D4C", "D4N", "V"]
            df_tgt = ds_raw.copy()[[i for i in tgt_cols if i in ds_raw.columns]]

        return df_tgt.rename(columns=df_tgt.iloc[0]).drop(df_tgt.index[0]).reset_index(drop=True)

    def main(self):
        df_stg0 = self.load(self.landing_path)  
        df_target = self.cleaner_stg1(df_stg0)
        return df_target

test_dir = r"tests/integration/scrapers/ibge/fixtures/raw.json"
instancia = IBGEScleaner(name="IPCA", landing_path= test_dir, raw=True)
df = instancia.main()

pd.set_option('display.max_columns', None)
df.head()
import requests as req
import pandas as pd

code='25241'

url = (
        "http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json"
    )

r=req.get(url.format(code))

ts=r.json()

df=pd.DataFrame.from_dict(ts)

df=df.set_index('data')
df
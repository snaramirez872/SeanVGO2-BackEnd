import pandas as pd
import json

df = pd.read_csv("../data/test-data/spreadsheets/dummy.csv")

dat = df.to_dict(orient="records")

with open("../data/test-data/test.json", "w", encoding="utf-8") as f:
    json.dump(dat, f, indent=2)

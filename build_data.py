import json
import pandas as pd
import math

EXCEL_PATH = "Data base Pricing.xlsx"   # aynı klasöre koy
SHEET_NAME = "Base_de_donnée"
OUT_JSON = "pricing.json"

df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)
header = df.iloc[1].tolist()
df = df.iloc[2:].copy()
df.columns = header

# rename extra unnamed columns
cols = []
for i,c in enumerate(df.columns):
    if isinstance(c,float) and math.isnan(c):
        cols.append(f"Extra_{i}")
    else:
        cols.append(c)
df.columns = cols

series=None
category=None
records=[]
for _,row in df.iterrows():
    art=row.get("ART")
    desc=row.get("DESCRIPTION")
    um=row.get("UM")

    if pd.isna(art) and isinstance(desc,str) and desc.strip():
        txt=desc.strip()
        if txt.upper().startswith("SÉRIE") or txt.upper().startswith("SERIE"):
            series=txt
            category=None
        else:
            category=txt
        continue

    if pd.notna(art):
        def fnum(v):
            return None if pd.isna(v) else float(v)
        records.append({
            "art": str(art).strip(),
            "description": str(desc).strip() if isinstance(desc,str) else "",
            "um": str(um).strip() if isinstance(um,str) else ("" if pd.isna(um) else str(um)),
            "dzd": fnum(row.get("DZD")),
            "euro": fnum(row.get("Euro")),
            "dzd_eqv": fnum(row.get("DZDéqv")),
            "series": series,
            "category": category
        })

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print(f"OK: {len(records)} kayıt → {OUT_JSON}")

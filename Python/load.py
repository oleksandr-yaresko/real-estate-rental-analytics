import pandas as pd
from sqlalchemy import create_engine

# Загружаем CSV
df = pd.read_csv(
    "Data/mainz_listings.csv",
    sep=";"
)

df["source"] = "Kleinanzeigen"

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:190882@localhost:5432/real_estate_analytics"
)

# Загружаем данные
df.to_sql(
    "listings",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully!")
print(f"Rows loaded: {len(df)}")
print(df.columns.tolist())
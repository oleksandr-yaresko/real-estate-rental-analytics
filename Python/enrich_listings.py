import pandas as pd
import requests

from extract import extract_size_m2
from extract import extract_rooms

df = pd.read_csv(
    "Data/mainz_listings.csv",
    sep=";"
)

sample = df.copy()

sizes = []
rooms_list = []

for _, row in sample.iterrows():

    url = "https://www.kleinanzeigen.de" + row["url"]

    print("Processing:", row["listing_id"])

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    if row["listing_id"] == 3324712419:
        with open(
            "failed_page.html",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(response.text)

        print("Failed page saved")

    size = extract_size_m2(response.text)
    rooms = extract_rooms(response.text)

    if size is None or rooms is None:
        print("\nFAILED:")
        print(row["listing_id"])
        print(row["title"])
        print(url)

    sizes.append(size)
    rooms_list.append(rooms)

sample["size_m2"] = sizes
sample["rooms"] = rooms_list

sample["size_m2"] = (
    sample["size_m2"]
    .str.replace(" m²", "", regex=False)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

sample["rooms"] = (
    sample["rooms"]
    .str.replace(",", ".", regex=False)
    .astype(float)
)

sample["price_per_m2"] = (
    sample["price"] / sample["size_m2"]
).round(2)

market_avg = sample["price_per_m2"].mean()

sample["deal_score"] = (
    market_avg - sample["price_per_m2"]
).round(2)

sample["discount_percent"] = (
    (market_avg - sample["price_per_m2"])
    / market_avg * 100
).round(2)

print(
    sample[
        [
            "listing_id",
            "price",
            "size_m2",
            "rooms",
            "price_per_m2",
            "deal_score",
            "discount_percent"
        ]
    ].head(10)
)

print("\nMissing values:")
print(sample.isna().sum())

failed_rows = sample[
    sample["size_m2"].isna()
]

print("\nFailed listings:")
print(
    failed_rows[
        ["listing_id", "title"]
    ]
)

sample = sample.dropna(
    subset=[
        "size_m2",
        "rooms",
        "price_per_m2"
    ]
)
print("\nRows after cleaning:", len(sample))

sample.to_csv(
    "Data/mainz_listings_scored.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("Scored CSV saved!")
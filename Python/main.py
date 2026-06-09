from extract import (
    get_search_page,
    extract_item_ids,
    extract_titles,
    extract_prices
)

import pandas as pd

URL = "https://www.kleinanzeigen.de/s-wohnung-mieten/mainz/c203l5315"

html = get_search_page(URL)

ids = extract_item_ids(html)
titles = extract_titles(html)
prices = extract_prices(html)

print("IDs:", len(ids))
print("Titles:", len(titles))
print("Prices:", len(prices))

# Берем минимальную длину
min_len = min(len(ids), len(titles), len(prices))

ids = ids[:min_len]
titles = titles[:min_len]
prices = prices[:min_len]

df = pd.DataFrame({
    "listing_id": ids,
    "title": titles,
    "price": prices
})

df["price"] = df["price"].astype(int)


def classify_listing(title):

    title = title.upper()

    if "TAUSCHWOHNUNG" in title:
        return "Tauschwohnung"

    if "WG" in title:
        return "WG"

    if "WBS" in title:
        return "WBS"

    return "Apartment"


df["market_category"] = df["title"].apply(classify_listing)


print("\nData Preview:")
print(df[["title", "market_category", "price"]].head(10))

print("\nDataset Info:")
print(df.info())

df.to_csv(
    "Data/mainz_listings.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)
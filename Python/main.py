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

print("\nData Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())
from extract import extract_urls
from extract import (
    get_search_page,
    extract_item_ids,
    extract_titles,
    extract_prices
)

import pandas as pd

all_ids = []
all_titles = []
all_prices = []
all_urls = []


# Собираем первые 5 страниц
for page in range(1, 6):

    if page == 1:
        url = "https://www.kleinanzeigen.de/s-wohnung-mieten/mainz/c203l5315"
    else:
        url = f"https://www.kleinanzeigen.de/s-wohnung-mieten/mainz/seite:{page}/c203l5315"

    print(f"\nProcessing page {page}...")

    html = get_search_page(url)

    

    if page == 1:
        urls = extract_urls(html)

        print("\nFirst 20 URLs:")
        for u in urls[:20]:
            print(u)

        print("Total URLs found:", len(urls))

    
    ids = extract_item_ids(html)
    titles = extract_titles(html)
    prices = extract_prices(html)
    urls = extract_urls(html)

    print(f"Found IDs: {len(ids)}")
    print(f"Found Titles: {len(titles)}")
    print(f"Found Prices: {len(prices)}")

    min_len = min(
        len(ids),
        len(titles),
        len(prices),
        len(urls)
    )
    all_urls.extend(urls[:min_len])
    all_ids.extend(ids[:min_len])
    all_titles.extend(titles[:min_len])
    all_prices.extend(prices[:min_len])

print("\nCreating DataFrame...")

df = pd.DataFrame({
    "listing_id": all_ids,
    "title": all_titles,
    "price": all_prices,
    "url": all_urls
})

# Удаляем дубликаты
df = df.drop_duplicates(subset=["listing_id"])

# Цена в число
df["price"] = df["price"].astype(int)

# Классификация
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

print(df.columns)
print("\nFinal Dataset:")
print(df.head())

print("\nTotal Unique Listings:", len(df))

# Сохраняем CSV
df.to_csv(
    "Data/mainz_listings.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("\nCSV saved successfully!")

html = get_search_page(
    "https://www.kleinanzeigen.de/s-wohnung-mieten/mainz/c203l5315"
)

with open("search_page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML file saved")
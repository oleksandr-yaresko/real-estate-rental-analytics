from extract import (
    get_search_page,
    extract_item_ids,
    extract_titles
)

import pandas as pd

URL = "https://www.kleinanzeigen.de/s-wohnung-mieten/mainz/c203l5315"

html = get_search_page(URL)

ids = extract_item_ids(html)
titles = extract_titles(html)

df = pd.DataFrame({
    "listing_id": ids,
    "title": titles
})

print(df.head())
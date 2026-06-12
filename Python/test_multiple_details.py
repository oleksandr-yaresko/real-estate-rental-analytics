import pandas as pd
import requests

from extract import extract_size_m2
from extract import extract_rooms

df = pd.read_csv(
    "Data/mainz_listings.csv",
    sep=";"
)

sample = df.head(5)

for _, row in sample.iterrows():

    url = "https://www.kleinanzeigen.de" + row["url"]

    print("\n-------------------")
    print("Title:", row["title"])
    print(row["url"])
    print("URL:", url)

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    print("Final URL:", response.url)

    size = extract_size_m2(response.text)
    rooms = extract_rooms(response.text)

    print("Size:", size)
    print("Rooms:", rooms)
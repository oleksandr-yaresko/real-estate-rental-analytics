import requests
from extract import extract_size_m2
from extract import extract_rooms

url = "https://www.kleinanzeigen.de/s-anzeige/modernisierte-2-zimmerwohnung-in-gesuchter-lage/3432928943-203-5317"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

with open("detail_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Detail page saved")

size = extract_size_m2(response.text)

print("Size:", size)

rooms = extract_rooms(response.text)

print("Rooms:", rooms)

size_number = float(
    size.replace(" m²", "")
        .replace(",", ".")
)

rooms_number = float(
    rooms.replace(",", ".")
)

price = 837

price_per_m2 = round(
    price / size_number,
    2
)

print("Price per m²:", price_per_m2)
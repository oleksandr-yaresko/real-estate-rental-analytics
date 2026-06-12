import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


def get_search_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    print(f"Status Code: {response.status_code}")

    return response.text


def extract_item_ids(html):
    pattern = r"item_id:\s*valOrUnknown\('(\d+)'\)"

    ids = re.findall(pattern, html)

    return ids


def extract_titles(html):
    pattern = r"item_name:\s*valOrUnknown\('(.+?)'\)"

    titles = re.findall(pattern, html)

    return titles

def extract_prices(html):
    pattern = r"price:\s*formatPriceOrUnknown\('(\d+)'\)"

    prices = re.findall(pattern, html)

    return prices

def extract_urls(html):
    pattern = r'(/s-anzeige/[^"\']+)'
    return re.findall(pattern, html)

from bs4 import BeautifulSoup


def extract_size_m2(html):

    soup = BeautifulSoup(html, "html.parser")

    details = soup.find_all(
        "li",
        class_="addetailslist--detail"
    )

    for detail in details:

        text = detail.get_text(" ", strip=True)

        if "Wohnfläche" in text:

            value = detail.find(
                "span",
                class_="addetailslist--detail--value"
            )

            if value:
                return value.text.strip()

    return None

def extract_rooms(html):

    soup = BeautifulSoup(html, "html.parser")

    details = soup.find_all(
        "li",
        class_="addetailslist--detail"
    )

    for detail in details:

        text = detail.get_text(" ", strip=True)

        if "Zimmer" in text:

            value = detail.find(
                "span",
                class_="addetailslist--detail--value"
            )

            if value:
                return value.text.strip()

    return None    
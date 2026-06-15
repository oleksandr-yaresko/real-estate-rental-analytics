# AI-Powered Real Estate Analytics Platform

## Business Problem

Finding affordable rental apartments in Germany is difficult because prices vary significantly across cities and districts.

This project analyzes rental listings from German real estate platforms and identifies below-market rental opportunities.

---

## Project Goals

- Collect rental listings
- Store data in PostgreSQL
- Analyze rental market trends
- Calculate €/m² metrics
- Identify undervalued listings
- Visualize insights in Power BI

---

## Tech Stack

- Python
- PostgreSQL
- SQL
- Power BI
- GitHub

---

## Architecture

Kleinanzeigen
    ↓
Python ETL
    ↓
PostgreSQL
    ↓
SQL Analytics Layer
    ↓
Power BI Dashboard

---

## Project Status

Version 1 (MVP) In Progress
## Data Dictionary

| Column | Description |
|----------|-------------|
| listing_id | Unique listing identifier |
| source | Data source |
| title | Listing title |
| url | Listing URL |
| price | Monthly rent in EUR |
| size_m2 | Apartment size in square meters |
| rooms | Number of rooms |
| city | City name |
| district | District name |
| listing_type | Apartment, WG, WBS, Tauschwohnung |
| is_wbs | WBS required |
| is_furnished | Furnished apartment |
| published_date | Listing publication date |
| scraped_at | Data collection timestamp |
| price_per_m2 | Rent per square meter |
| size_category | Small, Medium, Large |
| price_segment | Budget, Mid-Range, Premium |

## Initial Market Insights (Mainz)

Based on 124 rental listings collected from Kleinanzeigen:

| Category | Listings | Median Price (€) |
|-----------|-----------:|-----------:|
| Apartment | 71 | 850 |
| Tauschwohnung | 47 | 738 |
| WG | 6 | 550 |

### Key Findings

- Apartments represent 57% of all listings.
- The median apartment rent is €850.
- Tauschwohnungen are approximately 13% cheaper than regular apartments.
- WG rooms are the most affordable housing option with a median price of €550.

## Rental Price Distribution (Mainz)

Based on 124 rental listings:

| Price Range | Listings |
|------------|----------:|
| Under €600 | 29 |
| €600–799 | 36 |
| €800–999 | 29 |
| €1000–1199 | 11 |
| €1200+ | 19 |

### Key Findings

- More than half of listings are priced between €600 and €999.
- Only 15% of listings cost more than €1200.
- Affordable housing under €600 still represents nearly one quarter of the market.

• Analyzed 124 rental listings from Mainz
• Average rental price: €16.33 per m²
• WG listings showed the highest average price per m² (€20.10)
• 1-room apartments were the most expensive segment (€19.39 per m²)
• Large apartments (4 rooms) had the lowest average price per m² (€12.81)
• Identified listings ranging from €7.50 to €36.11 per m²

Key Feature: Best Deal Detection

The project identifies potentially undervalued rental properties by comparing each listing's price per square meter against the overall market average.

A custom Deal Score is calculated for every property:

Deal Score = Market Average Price per m² - Listing Price per m²

Positive values indicate listings priced below the market average, while negative values indicate listings priced above market levels.

This allows renters to quickly identify potentially attractive opportunities within the Mainz rental market.
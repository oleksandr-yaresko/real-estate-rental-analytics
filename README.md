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
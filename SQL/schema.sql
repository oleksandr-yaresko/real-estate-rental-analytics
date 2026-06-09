CREATE TABLE listings (
    listing_id TEXT PRIMARY KEY,
    source VARCHAR(50) NOT NULL,

    title TEXT NOT NULL,
    url TEXT,

    price NUMERIC(10,2),
    size_m2 NUMERIC(10,2),
    rooms NUMERIC(4,1),

    city VARCHAR(100),
    district VARCHAR(100),

    listing_type VARCHAR(50),

    is_wbs BOOLEAN DEFAULT FALSE,
    is_furnished BOOLEAN DEFAULT FALSE,

    published_date DATE,
    scraped_at TIMESTAMP,

    price_per_m2 NUMERIC(10,2),

    size_category VARCHAR(20),
    price_segment VARCHAR(20)
);
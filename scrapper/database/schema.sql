CREATE TABLE IF NOT EXISTS `article` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` TEXT NOT NULL,
    `author` TEXT NOT NULL,
    `created_at` TEXT NOT NULL,
    `body` TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `stocks` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,    -- Unique identifier for each stock entry
    `ticker_symbol` TEXT NOT NULL UNIQUE,             -- Ticker symbol of the stock (e.g., 'AAPL' for Apple)
    `company_name` TEXT NOT NULL,              -- Full name of the company (e.g., 'Apple Inc.')
    `sector` TEXT,                             -- Sector to which the company belongs (e.g., 'Technology')
    `industry` TEXT,                           -- Industry within the sector (e.g., 'Consumer Electronics')
    `market_cap` REAL,                         -- Market capitalization (e.g., 2.5 trillion)
    `price` REAL NOT NULL,                     -- Current stock price
    `volume` INTEGER,                          -- Total trading volume of the stock for the day
    `pe_ratio` REAL,                           -- Price-to-Earnings ratio (P/E ratio)
    `dividend_yield` REAL,                     -- Dividend yield percentage (e.g., 0.5%)
    `fifty_two_week_high` REAL,                -- 52-week high price
    `fifty_two_week_low` REAL                  -- 52-week low price
    -- `date_last_updated` DATE NOT NULL DEFAULT (DATE('now')),  -- Last updated date for this entry
);

CREATE TABLE IF NOT EXISTS `stock_change` (
    `stock_id` INTEGER NOT NULL,
    `change_type` TEXT NOT NULL,
    `change_amount` REAL NOT NULL,
    `change_date` TEXT NOT NULL,
    FOREIGN KEY(`stock_id`) REFERENCES `stocks`(`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `article_stock_change` (
    `article_id` INTEGER NOT NULL,
    `stock_change_id` INTEGER NOT NULL,
    FOREIGN KEY(`article_id`) REFERENCES `article`(`id`) ON DELETE CASCADE
);

-- CREATE TABLE IF NOT EXISTS `` (
    
-- );

-- CREATE TABLE IF NOT EXISTS `` (
    
-- );

-- CREATE TABLE IF NOT EXISTS `` (
    
-- );
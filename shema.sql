CREATE TABLE IF NOT EXISTS base (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL DEFAULT'',
        status TEXT NOT NULL DEFAULT''
    )
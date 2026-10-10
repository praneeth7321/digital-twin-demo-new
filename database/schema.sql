CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    category TEXT,
    date TEXT
);

CREATE TABLE lifestyle_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    sleep_hours REAL,
    exercise_minutes INTEGER,
    date TEXT
);

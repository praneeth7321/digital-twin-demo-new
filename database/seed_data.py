import sqlite3

conn = sqlite3.connect("digital_twin.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, age) VALUES ('Demo User', 21)")
cursor.execute("INSERT INTO transactions (user_id, amount, category, date) VALUES (1, 500, 'Food', '2025-01-01')")
cursor.execute("INSERT INTO lifestyle_data (user_id, sleep_hours, exercise_minutes, date) VALUES (1, 6.5, 30, '2025-01-01')")

conn.commit()
conn.close()

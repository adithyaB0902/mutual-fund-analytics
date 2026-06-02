import sqlite3
from pathlib import Path

DB_PATH = "data/db/bluestock_mf.db"
SCHEMA_PATH = "sql/schema.sql"

# Remove old database
db_file = Path(DB_PATH)

if db_file.exists():
    db_file.unlink()

conn = sqlite3.connect(DB_PATH)

with open(
    SCHEMA_PATH,
    "r",
    encoding="utf-8"
) as f:

    schema = f.read()

conn.executescript(schema)

conn.commit()

print("Database created from schema.sql")

conn.close()
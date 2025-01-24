import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

def create_tables():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS queries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        query_text VARCHAR(255) NOT NULL,
        timestamp DATETIME NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INT AUTO_INCREMENT PRIMARY KEY,
        query_id INT NOT NULL,
        summary TEXT NOT NULL,
        ref_urls TEXT,
        timestamp DATETIME NOT NULL,
        FOREIGN KEY (query_id) REFERENCES queries(id)
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()

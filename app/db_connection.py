import mysql.connector
import os
from datetime import datetime


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

def save_query(query_text):
    conn = get_connection()
    cursor = conn.cursor()
    timestamp = datetime.now()

    insert_query = "INSERT INTO queries (query_text, timestamp) VALUES (%s, %s)"
    cursor.execute(insert_query, (query_text, timestamp))
    conn.commit()

    query_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return query_id

def save_result(query_id, summary, ref_str):
    conn = get_connection()
    cursor = conn.cursor()
    timestamp = datetime.now()

    insert_result = "INSERT INTO results (query_id, summary, ref_urls, timestamp) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_result, (query_id, summary, ref_str, timestamp))
    conn.commit()

    result_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return result_id

def get_results(query_id):
    conn = get_connection()
    cursor = conn.cursor()
    select_query = "SELECT summary, references, timestamp FROM results WHERE query_id=%s"
    cursor.execute(select_query, (query_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

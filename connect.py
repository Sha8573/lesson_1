import psycopg2 as db
import os
from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database=os.getenv("database"),
            host=os.getenv("host"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )
        cursor = database.cursor()
        cursor.execute(query)
        data = ["insert", "delete", "update", "select"]
        if query_type in data:
            database.commit()
            if query_type == "insert":
                return "INSERTED"

            elif query_type == "delete":
                return "DELETED"

            elif query_type == "update":
                return "UPDATED"

            elif query_type == "select":
                return cursor.fetchall()

            else:
                return "Error"
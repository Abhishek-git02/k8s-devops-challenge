from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "mongodb-service")

@app.route("/")
def home():
    return f"Flask App Running. Mongo Host: {db_host}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
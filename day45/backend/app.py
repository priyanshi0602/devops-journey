from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Day 45 DevOps Journey 🚀</h1>
    <h2>Flask + Docker Compose</h2>
    <p>Database User: {os.getenv("POSTGRES_USER")}</p>
    """

app.run(host="0.0.0.0", port=5000)
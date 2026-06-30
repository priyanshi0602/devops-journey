from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Production Multi-Tier Application 🚀</h1>
    <h2>Month 1 Resume Project</h2>

    <p>Database User :
    {os.getenv("POSTGRES_USER")}</p>
    """

app.run(host="0.0.0.0", port=5000)
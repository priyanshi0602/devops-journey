from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "Default App")
    return f"Welcome to {app_name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
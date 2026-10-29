from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "CI/CD Pipeline Automation demo",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "status": "healthy"
    })

@app.get("/health")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

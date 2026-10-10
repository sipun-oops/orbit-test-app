# Phase 2: the test app that ORBIT will deploy.
#   GET /        -> shows the app name and version
#   GET /health  -> {"status":"ok"} (Kubernetes uses this to know the app is ready)

import socket
from flask import Flask, jsonify

VERSION = "2.0.0"  # later: change this, push, redeploy -> the new version shows at the same URL

app = Flask(__name__)


@app.get("/")
def home():
    return f"<h1>Hello from ORBIT</h1><p>Version {VERSION}</p><p>Pod: {socket.gethostname()}</p>"


@app.get("/health")
def health():
    return jsonify(status="ok", version=VERSION)


# Only used when you run "python app.py" on your laptop.
# In the container, Gunicorn starts the app instead.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

# Application metadata
APP_NAME = "orbit-sample-flask"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

@app.route("/", methods=["GET"])
def index():
    """Main landing endpoint returning a simple HTML page."""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{ font-family: sans-serif; background-color: #f4f4f9; color: #333; text-align: center; padding: 50px; }}
            .container {{ background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display: inline-block; }}
            h1 {{ color: #0284c7; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to ORBIT PaaS! 🚀</h1>
            <p>Your Flask application <strong>{APP_NAME}</strong> (v{APP_VERSION}) is running smoothly!</p>
            <p style="color: #666; font-size: 0.9em;">Served by pod: {socket.gethostname()}</p>
        </div>
    </body>
    </html>
    """
    return html, 200

@app.route("/health", methods=["GET"])
def health():
    """Liveness & readiness probe endpoint for Kubernetes and ALB."""
    return jsonify({
        "status": "healthy",
        "service": APP_NAME,
        "version": APP_VERSION
    }), 200

if __name__ == "__main__":
    # Fallback for running app directly outside container
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)

from flask import request, jsonify

TOKEN = "mysecrettoken"

def auth_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify ({"error": "Unauthorized"}), 401

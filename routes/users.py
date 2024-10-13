from flask import Blueprint, request, jsonify
from middleware.auth import auth_token

users_bp = Blueprint("users", __name__)

users = []

# middleware authentication
@users_bp.before_request
def bef_req():
    auth_token()

# Get endpoint - get all users
@users_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(users)

# Post endpoint - add new user
@users_bp.route("/", methods=["POST"])
def create_user():
    user = {
        "sys_id": len(users)+1,
        "name": request.json.get("name")
    }
    users.append(user)
    return jsonify(user), 201

# Put endpoint - update existing user
@users_bp.route("/<int:id>", methods=["PUT"])
def update_user(id):
    user = next((i for i in users if i["id"] == id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    user["name"] = request.json.get("name", user["name"])
    return(jsonify(user))

# Delete endpoint - remove user
@users_bp.route("<int:id>", methods=["DELETE"])
def del_user(id):
    global users
    users = [i for i in users if i["id"]!=id]
    return '', 204

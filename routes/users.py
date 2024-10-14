from flask import Blueprint, request, jsonify
from middleware.auth import authenticate_token

users_bp = Blueprint("users", __name__)

users = []

# middleware authentication
@users_bp.before_request
def before_request():
    authenticate_token()

# Get endpoint 1 - get all users
@users_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(users)

# Post endpoint - add new user
@users_bp.route("/", methods=["POST"])
def create_user():
    user = {
        "id": len(users)+1,
        "user_id": request.json.get("user_id"),
        "name": request.json.get("name"),
        "age": request.json.get("age"),
        "email": request.json.get("email")
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

# Get endpoint 2 - return specific user
@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user_via_id(user_id):
    user = next((i for i in users if i["user_id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return(jsonify(user))

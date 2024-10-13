from flask import Flask, jsonify
from routes.brrp import brrp_bp

app = Flask(__name__)

app.register_blueprint(brrp_bp, url_prefix="/brrp")

@app.errorhandler(404)
def not_found(e):
 return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
 app.run(debug=True)

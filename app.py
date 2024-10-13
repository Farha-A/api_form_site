from flask import Flask, jsonify
# , render_template, request
from routes.brrp import brrp_bp

app = Flask(__name__)

app.register_blueprint(brrp_bp, url_prefix="/brrp")

@app.errorhandler(404)
def not_found(e):
 return jsonify({"error": "Resource not found"}), 404

# @app.route('/')
# def home():
#  return render_template('index.html')

# # POST endpoint for form filling
# @app.route('/submit', methods=['POST'])
# def submit():
#  name = request.form['name']
#  id = request.form['id']
#  age = request.form['age']
#  mail = request.form['mail']
#  return render_template('res.html', name=name, age=age, id=id, mail=mail)


if __name__ == '__main__':
 app.run(debug=True)
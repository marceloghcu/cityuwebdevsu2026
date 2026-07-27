from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get("username") or request.form.get("username")
    password = request.args.get("password") or request.form.get("password")
    if username == "user1" and password == "pass1":
        return "valid"
    return "invalid"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

from flask import Flask

app = Flask(__name__)

@app.route('/login')
def login():
    user = request.args.get("user")
    return "user: " + user

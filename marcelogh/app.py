from flask import Flask, request

app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    return f"username: {username}, password: {password}"


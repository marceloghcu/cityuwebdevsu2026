from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login')
def login():
    user = request.args.get('user', '')
    password = request.args.get('password', '')

    if user == 'cogh7595' and password == '1234':
        return jsonify({
            'status': 'success',
            'message': 'Login successful'
        })

    return jsonify({
        'status': 'error',
        'message': 'Invalid username or password'
    })
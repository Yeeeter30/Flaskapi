from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    message = request.args.get('message', 'Hello, World!')
    return jsonify({"message": message})

# Required for Vercel to recognize the app
def handler(environ, start_response):
    return app(environ, start_response)

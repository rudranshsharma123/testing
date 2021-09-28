from flask import Flask, request, jsonify, make_response

from werkzeug.serving import WSGIRequestHandler

app = Flask(__name__)

@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"

if __name__ == '__main__':
  WSGIRequestHandler.protocol_version = "HTTP/1.1"
  app.run(host='0.0.0.0', port=5000)  




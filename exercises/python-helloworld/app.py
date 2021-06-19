from flask import Flask
import flask
import json
import http
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def healthCheck():
    return  flask.Response(
        response= json.dumps({"result": "OK - healthy"}),
        status= http.HTTPStatus.OK,
        mimetype= 'application/json'
    )

@app.route("/metrics")
def metrics():
    return  flask.Response(
        response= json.dumps({"data": "UserCount: 140, UserCountActive: 23"}),
        status= http.HTTPStatus.OK,
        mimetype= 'application/json'
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')

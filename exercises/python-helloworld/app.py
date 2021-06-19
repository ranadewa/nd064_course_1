from flask import Flask
import flask
import json
import http
import logging

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def healthCheck():
    logging.debug('/status endpoint was reached');
    return  flask.Response(
        response= json.dumps({"result": "OK - healthy"}),
        status= http.HTTPStatus.OK,
        mimetype= 'application/json'
    )

@app.route("/metrics")
def metrics():
    logging.debug('/metrics endpoint was reached');
    return  flask.Response(
        response= json.dumps({"data": "UserCount: 140, UserCountActive: 23"}),
        status= http.HTTPStatus.OK,
        mimetype= 'application/json'
    )

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', datefmt='%c', level=logging.DEBUG,
    format='%(asctime)s, %(message)s' )
    app.run(host='0.0.0.0')

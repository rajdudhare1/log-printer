from flask import Flask, render_template,Response,request,jsonify,stream_with_context
from time import sleep
import requests

APP = Flask(__name__,static_folder="app/static/",template_folder="app/static/")
DATA= {}



@APP.route("/", methods=["GET"])
def root():
    """index page"""
    return render_template("index.html")

@APP.route("/feeder", methods = ['POST'])
def feed():
    if request.method == 'POST':
       with open('job.log','a') as a:
           a.write(str((request.json[0]['log']))+"\n")
    return "OK"

def logs():
    with open("job.log", "r") as f:
            while True:
                yield f.read()
                sleep(1)

def printLogs(msg=DATA):
    while True:
        yield str(msg)
        sleep(1)


@APP.route("/stream", methods=["GET"])
def stream():
    """returns logging information"""
    return Response(stream_with_context(logs()), mimetype="application/json", content_type="application/stream+json")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8080, threaded=True)
    
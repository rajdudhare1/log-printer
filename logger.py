from flask import Flask, render_template,Response,request,jsonify,stream_with_context
from time import sleep
import requests
import os

APP = Flask(__name__,static_folder="app/static/",template_folder="app/static/")
path_to_file = 'job.log'

@APP.route("/", methods=["GET"])
def root():
    """index page"""
    return render_template("index.html")

@APP.route("/feeder", methods = ['POST'])
def feed():
    if request.method == 'POST':
        with open(path_to_file,'a') as a:
           a.write(str((request.json[0]['log']))+"\n")
    return "OK"

def logs():
    if os.path.exists(path_to_file):
        with open("job.log", "r") as f:
            while True:
                yield f.read()
                sleep(1)


@APP.route("/stream", methods=["GET"])
def stream():
    """returns logging information"""
    return Response(stream_with_context(logs()), mimetype="application/json", content_type="application/stream+json")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8080, threaded=True)
    
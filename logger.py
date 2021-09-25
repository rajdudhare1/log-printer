from flask import Flask, render_template,Response,request,jsonify
from time import sleep

APP = Flask(__name__,static_folder="app/static/",template_folder="app/static/")
@APP.route("/", methods=["GET"])
def root():
    """index page"""
    return render_template("index.html")

@APP.route("/feeder", methods = ['POST'])
def feed():
    if request.method == 'POST':
       content = request.json
       #print(content)
       return "Ok"

def logs():
    with open("job.log", "r") as f:
            while True:
                yield f.read()
                sleep(1)

def printLogs():
    pass


@APP.route("/stream", methods=["GET"])
def stream():
    """returns logging information"""
    return Response(logs(), mimetype="text/plain", content_type="text/event-stream")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=8080, threaded=True)

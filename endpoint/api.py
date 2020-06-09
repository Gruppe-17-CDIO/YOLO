from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import os

##
# @author: Anders Frandsen
##

app = Flask(__name__)
api = Api(app)

# Upload dir: wwwroot + /images
UPLOAD_DIR = "/Users/arne/Documents/Kode/YOLO/endpoint/images"

@app.route("/")
def server_root():
    return "YOLO Endpoint: POST /detect"

@app.route("/detect/<filename>", methods=["POST"])
def post_file(filename):
    if ".png" not in filename:
        # return 400 error
        return "Only jpg is allowed", 400

    with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
        fp.write(request.data)

    # run docker

    # delete jpg

    # return json
    return "", 200

if __name__ == "__main__":
    app.run(port="5000")

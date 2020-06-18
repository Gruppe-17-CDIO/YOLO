from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from pydarknet import Detector
from pydarknet import Image as dimg
from io import BytesIO
from PIL import Image as im
import numpy as np
import cv2
import os
import time
import json
import sys

##
# @author: Anders Frandsen & Justus Gammelgaard

##

app = Flask(__name__)
api = Api(app)

# Upload dir: wwwroot + /images
UPLOAD_DIR = "/home/justus/Desktop/YOLO/input"

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
    #print(request.data)
    return recognize(filename), 200
    
    

def recognize(filename):
    #Read img
    img = cv2.imread(os.path.join(UPLOAD_DIR, filename))
    #img = cv2.imread(file)
    #stream = BytesIO()
    #img = im.open(stream).convert("RGB")
    #npary = np.array(img)
    
    dark_img = dimg(img)
    print("Filename: ", img)
    #create darknet detector
    net = Detector(bytes("cfg/yolofinal.cfg", encoding="utf-8"), bytes("weights/yolov3.weights", encoding="utf-8"), 0, bytes("cfg/data.data", encoding="utf-8"))
    res = [] 
    
    start_time = time.time()
    #Detect! can be given threshold parameters - see top of file :)
    #Has a standard threshold value of .5
    results = net.detect(dark_img)
    end_time = time.time()
    
    if len(results)==0:
       print("No results")
    else:
       print("There are Results")
      # print(results)

    print("Elapsed Time:", end_time-start_time)

    for cat, score, bounds in results:
        x, y, w, h = bounds
        #bytecode-decode to string
        cat_str = cat.decode("utf-8")
        #Format JSON
        json_obj = {"x": x, "y": y, "w": w, "h": h, "cat": cat_str, "score": score}
        #Append JSON to list
        res.append(json_obj)
        cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (255, 0, 0), thickness=2)
        cv2.putText(img,str(cat.decode("utf-8")),(int(x),int(y)),cv2.FONT_HERSHEY_DUPLEX,4,(0,0,255), thickness=2)
    print(res)
    cv2.imwrite(os.path.join("output", "outputpic.png"), img)
    return json.dumps(res)

if __name__ == "__main__":
    app.run(host="192.168.0.2", port="5000")

#From https://github.com/madhawav/YOLO3-4-Py/docker/docker_demo.py
#Edited by Justus Gammelgaard s185088
from pydarknet import Detector, Image
import cv2
import os
import time
import json
import sys
#Parameters for detect
thresh = .5
hier_thresh = .5
nms = .25
    

def recognize(file):
    #Read img
    #img = cv2.imread(os.path.join(os.environ["DARKNET_HOME"], filename))
    img = cv2.imread(file)
    dark_img = Image(img)
    print("Filename: ", file)
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

if __name__=='__main__':
    #run from cmd
    recognize(*sys.argv[1:])
    

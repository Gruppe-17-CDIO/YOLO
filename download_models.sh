#!/usr/bin/env bash

echo "Downloading config files..."

#mkdir cfg
#wget -O cfg/data.data https://finalweightscfg.imfast.io/data.data
#wget -O cfg/yolofinal.cfg https://finalweightscfg.imfast.io/yolofinal.cfg

#echo "Modify config parameters to enable Testing mode"
#sed -i '/batch=64/c\# batch=64' cfg/yolov3.cfg
#sed -i '/subdivisions=16/c\# subdivisions=16' cfg/yolov3.cfg
#sed -i '/# batch=1/c\batch=1' cfg/yolov3.cfg
#sed -i '/# subdivisions=1/c\subdivisions=1' cfg/yolov3.cfg

#mkdir data
#wget -O data/coco.names https://raw.githubusercontent.com/JustusGammelgaard/YOLO/master/data/coco.names

echo "Downloading yolov3 weights"
mkdir weights
wget -c -O https://trainingweight.imfast.io/yolov3-tiny-21000.weights
#wget -c -O weights/yolov3.weights https://finalweightscfg.imfast.io/yolov3.weights

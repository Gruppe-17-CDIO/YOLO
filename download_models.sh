#!/usr/bin/env bash

echo "Downloading config files..."

mkdir cfg
wget -O cfg/coco.data https://raw.githubusercontent.com/JustusGammelgaard/YOLO/master/cfg/coco.data
wget -O cfg/yolov123.cfg https://raw.githubusercontent.com/JustusGammelgaard/YOLO/master/cfg/yolov123.cfg

echo "Modify config parameters to enable Testing mode"
sed -i '/batch=64/c\# batch=64' cfg/yolov3.cfg
sed -i '/subdivisions=16/c\# subdivisions=16' cfg/yolov3.cfg
sed -i '/# batch=1/c\batch=1' cfg/yolov3.cfg
sed -i '/# subdivisions=1/c\subdivisions=1' cfg/yolov3.cfg

mkdir data
wget -O data/coco.names https://raw.githubusercontent.com/JustusGammelgaard/YOLO/master/data/coco.names

echo "Downloading yolov3 weights"
mkdir weights
wget -O weights/yolov123.weights https://yoloweights.imfast.io/yolov123.weights

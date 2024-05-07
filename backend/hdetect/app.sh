#!/bin/bash

FILE="$1"

cd yolov9 && rm -rf ./runs/detect && python detect.py --source "$FILE" --weights '/home/jitu/Projects/Hdetect/backend/hdetect/yolov9/best.pt'  --save-crop && cd .. && python ./main.py 
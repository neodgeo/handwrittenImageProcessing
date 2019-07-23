# Flask-API
 
Flask API is a service that analyse image and extract the text inside.
 
## Installation
 
Load the docker image spmallick/opencv-docker:opencv
 
```bash
docker pull spmallick/opencv-docker:opencv
docker run  -v /tmp/.X11-unix:/tmp/.X11-unix -v /path/of/FLask-API:/home -e DISPLAY=$DISPLAY -p 5000:5000 -p 8888:8888 -it spmallick/opencv-docker:opencv /bin/bash
```
 
Then inside the docker 
```bash
cd home
workon OpenCV-master-py3
Python app.py 
```

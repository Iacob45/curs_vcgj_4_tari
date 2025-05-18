#!/bin/bash

docker stop flask-norvegia
docker rm flask-norvegia
docker build -t flask-norvegia .
docker run -p 5000:5000 flask-norvegia

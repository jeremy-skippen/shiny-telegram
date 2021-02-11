#!/bin/sh

docker build . -t shiny-telegram:latest 1>/dev/null
docker run --name shiny-telegram shiny-telegram:latest python shiny-telegram.py $1 --port 8080
docker rm shiny-telegram 1>/dev/null

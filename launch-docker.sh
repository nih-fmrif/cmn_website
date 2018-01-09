#!/bin/bash

docker run -it -p 80:80 -v $PWD:/home/docker/code --name webapp --entrypoint=/bin/bash webapp
docker rm -vf webapp

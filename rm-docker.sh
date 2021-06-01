#!/bin/bash
#Handy script for removing all docker containers and images
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi -f $(docker images -a -q)
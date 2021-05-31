#!/bin/bash
docker build -t serverless/docker .
docker run -p 49160:3000 serverless/docker
#docker-compose up -d

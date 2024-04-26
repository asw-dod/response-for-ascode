#!/bin/bash

VERSION=$1

docker build -t ghcr.io/asw-dod/response-for-ascode:$1 .
docker push ghcr.io/asw-dod/response-for-ascode:$1

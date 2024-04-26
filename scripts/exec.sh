#!/bin/bash

docker run -e ASCODE_USERID=$1 -e ASCODE_USERPW=$2 ghcr.io/asw-dod/response-for-ascode:1.0.0

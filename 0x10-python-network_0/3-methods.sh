#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept this .
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

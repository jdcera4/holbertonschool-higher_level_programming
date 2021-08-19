#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sI GET "$1" | grep -i "Allow" | cut -d " " -f2

#!/bin/bash
# Script taht takes in a url, sends a request to that URL
curl -sI GET $1 | grep -i "Content-Length" | cut -d " " -f2

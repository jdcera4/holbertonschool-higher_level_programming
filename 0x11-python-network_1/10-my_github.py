#!/usr/bin/python3
"""Check status"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    user = str(sys.argv[1])
    pw = str(sys.argv[2])
    result = requests.get("https://api.github.com/user",
                          auth=(HTTPBasicAuth(user, pw)))

    try:
        data = result.json()
        print(data["id"])
    except:
        print("None")

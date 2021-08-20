#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    rq = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(rq) as response:
        html = response.read()
        print(html.decode("utf-8"))
#!/usr/bin/python3
"""api request git hub"""
import sys
import requests


if __name__ == "__main__":
    """apidata"""
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    result = requests.get(url)
    d = result.json()
    try:
        for i in range(10):
            print("{}: {}".format(d[i]["sha"],
                                  d[i]["commit"]["author"]["name"]))
    except IndexError:
        pass

#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
'''
from sys import argv
import requests as req


if __name__ == '__main__':
    if len(argv) > 1:
        res = req.get(argv[1])
        if 'X-Request-Id' in res.headers:
            print(res.headers['X-Request-Id'])

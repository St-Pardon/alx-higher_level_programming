#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
'''
from sys import argv
from urllib import request


if __name__ == '__main__':
    if len(argv) > 1:
        with request.urlopen(argv[1]) as res:
            print(res.headers['X-Request-id'])

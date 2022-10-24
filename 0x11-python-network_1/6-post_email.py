#!/usr/bin/python3
'''
Python script that takes in a URL and an email address, sends a
POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
'''
import requests as req
from sys import argv


if __name__ == '__main__':
    if len(argv) > 2:
        res = req.post(argv[1], data={'email': argv[2]})
        print(res.text)

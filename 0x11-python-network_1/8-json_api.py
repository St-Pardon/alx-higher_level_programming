#!/usr/bin/python3
'''
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
from sys import argv
import requests as req


if __name__ == '__main__':
    query = argv[1] if len(argv) > 1 else ""
    res = req.post('http://0.0.0.0:5000/search_user', data={'q': query})
    try:
        json_data = res.json()
        if json_data:
            print('[{}] {}'.format(json_data['id'], json_data['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')

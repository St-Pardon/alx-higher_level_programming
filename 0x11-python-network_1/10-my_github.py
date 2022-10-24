#!/usr/bin/python3
'''
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
'''
from sys import argv
import requests as req


if __name__ == '__main__':
    if len(argv) == 3:
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Username': argv[1],
            'Authorization': 'token {}'.format(argv[2])
        }
        res = req.get("https://api.github.com/user", headers=headers)
        if res.status_code == 200:
            user = res.json()
            # print(user['login'])
            if user['login'] == argv[1]:
                print(user['id'])
            else:
                print('None')
        else:
            print('None')

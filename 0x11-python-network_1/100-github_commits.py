#!/usr/bin/python3
"""Retrieves the last 10 commits of a repository.
"""
import requests as req
from sys import argv


if __name__ == "__main__":
    if len(argv) > 2:
        repo = argv[1]
        username = argv[2]
        api_url = 'https://api.github.com'
        req_url = '{}/repos/{}/{}/commits?{}'.format(
            api_url,
            username,
            repo,
            'per_page=10'
        )
        res = req.get(
            req_url,
            headers={'Accept': 'application/vnd.github.v3+json'}
        )
        if res.status_code == 200:
            for commit in res.json():
                commit_sha = commit['sha']
                commit_author = commit['commit']['author']['name']
                print('{}: {}'.format(commit_sha, commit_author))

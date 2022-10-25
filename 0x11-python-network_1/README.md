# 0x11. Python - Network #1


## Objectives
- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests` #requestsiswaysimplerthanurllib
- How to make HTTP `GET` request
- How to make HTTP `POST`/`PUT`/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of *this* project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)


## Tasks

### [0. What's my status? #0](./0-hbtn_status.py)
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

- [x] You must use the package `urllib`
- [x] You are not allowed to import any packages other than `urllib`
- [x] The body of the response must be displayed like the following example (tabulation before `-`)
- [x] You must use a `with` statement

### [1. Response header value #0](./1-hbtn_header.py)
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

- [x] You must use the packages `urllib` and `sys`
- [x] You are not allow to import packages other than `urllib` and `sys`
- [x] The value of this variable is different for each request
- [x] You don’t need to check arguments passed to the script (number or type)
- [x] You must use a `with` statement

### [3. Error code #0](./3-error_code.py)
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

- [x] You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
- [x] You must use the packages `urllib` and `sys`
- [x] You are not allowed to import other packages than `urllib` and `sys`
- [x] You don’t need to check arguments passed to the script (number or type)
- [x] You must use the `with` statement

### [4. What's my status? #1](./4-hbtn_status.py)
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

- [x] You must use the package `requests`
- [x] You are not allow to import packages other than `requests`
- [x] The body of the response must be display like the following example (tabulation before `-`)

### [5. Response header value #1](./5-hbtn_header.py)
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

- [x] You must use the packages `requests` and `sys`
- [x] You are not allow to import other packages than `requests` and `sys`
- [x] The value of this variable is different for each request
- [x] You don’t need to check script arguments (number and type)

### [6. POST an email #1](./6-post_email.py)
Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

- [x] The email must be sent in the variable `email`
- [x] You must use the packages `requests` and `sys`
- [x] You are not allowed to import packages other than `requests` and `sys`
- [x] You don’t need to error check arguments passed to the script (number or type)

### [7. Error code #1](./7-error_code.py)
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
- [x] You must use the packages `requests` and `sys`
- [x] You are not allowed to import packages other than `requests` and `sys`
- [x] You don’t need to check arguments passed to the script (number or type)

### [8. Search API](./8-json_api.py)
Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

The letter must be sent in the variable `q`
- [x] If no argument is given, set `q=""`
- [x] If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
- Otherwise:
 - [x] Display `Not a valid JSON` if the JSON is invalid
 - [x] Display `No result` if the JSON is empty
- [x] You must use the package `requests` and `sys`
- [x] You are not allowed to import packages other than `requests` and `sys`

### [9. My GitHub!](./10-my_github.py)
Write a Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://docs.github.com/en/rest/users) to display your `id`

- [x] You must use [Basic Authentication](https://alx-intranet.hbtn.io/rltoken/VsPQfbYBgBA0PPdpdJNPIQ) with a [personal access token as password](https://alx-intranet.hbtn.io/rltoken/cQ7P5gl79x0I_3Pl3hG2hw) to access to your information (only `read:user` permission is needed)
- [x] The first argument will be your `username`
- [x] The second argument will be your `password` (in your case, a personal access token as password)
- [x] You must use the package `requests` and `sys`
- [x] You are not allowed to import packages other than `requests` and `sys`
- [x] You don’t need to check arguments passed to the script (number or type)

### [10. Time for an interview!](./100-github_commits.py)
The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```
Write a Python script that takes 2 arguments in order to solve this challenge.

- [x] The first argument will be the `repository name`
- [x] The second argument will be the `owner name`
- [x] You must use the packages `requests` and `sys`
- [x] You are not allowed to import packages other than `requests` and `sys`
- [x] You don’t need to check arguments passed to the script (number or type)
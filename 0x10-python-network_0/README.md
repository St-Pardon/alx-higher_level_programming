# 0x10. Python - Network #0

## Resources
- [HTTP (HyperText Transfer Protocol)](https://alx-intranet.hbtn.io/rltoken/rAon_EpQ6PGl8N0plySn4A) *(except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)*
- [HTTP Cookies](https://alx-intranet.hbtn.io/rltoken/MhVCl_0oviQldWPn5oX-NQ)

## Tasks
### [0. cURL body size](./0-body_size.sh)
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

- [x] The size must be displayed in bytes
- [x] You have to use `curl`


### [1. cURL to the end](./1-body.sh)
Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the bodyof the response

- [x] Display only body of a `200` status code response
- [x] You have to use `curl`


### [2. cURL Method](./2-delete.sh)
Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response

- [x] You have to use `curl`


### [3. cURL only methods](./3-methods.sh)
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

- [x] You have to use `curl`


### [4. cURL headers](./4-header.sh)
Write a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response

- [x] A header variable `X-School-User-Id` must be sent with the value `98`
- [x] You have to use `curl`


### [5. cURL POST parameters](./5-post_params.sh)
Write a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response

- [x] A variable `email` must be sent with the value `test@gmail.com`
- [x] A variable `subject` must be sent with the value `I will always be here for PLD`
- [x] You have to use `curl`


### [6. Find a peak](./6-peak.py)
Write a function that finds a **peak** in a list of unsorted integers.

- [x] Prototype: `def find_peak(list_of_integers):`
- [x] You are not allowed to import any module
- [x] Your algorithm must have the lowest complexity *(hint: you don’t need to go through all numbers to find a peak)*
- [x] `6-peak.py` must contain the function
- [x] `6-peak.txt` must contain the complexity of your algorithm: `O(log(n))`, `O(n)`, `O(nlog(n))` or `O(n2)`
 [x] **Note:** there may be more than one peak in the list
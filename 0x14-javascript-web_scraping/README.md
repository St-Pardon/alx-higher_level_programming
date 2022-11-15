# 0x14. JavaScript - Web scraping

## Tasks
### [0. Readme](./0-readme.js)
Write a script that reads and prints the content of a file.

- [x] The first argument is the file path
- [x] The content of the file must be read in `utf-8`
- [x] If an error occurred during the reading, print the error object

### [1. Write me](./1-writeme.js)
Write a script that writes a string to a file.

- [x] The first argument is the file path
- [x] The second argument is the string to write
- [x] The content of the file must be written in `utf-8`
- [x] If an error occurred during while writing, print the error object

### [2. Status code](./2-statuscode.js)
Write a script that display the status code of a `GET` request.

- [x] The first argument is the URL to request (`GET`)
- [x] The status code must be printed like this: `code: <status code>`
- [x] You must use the module `request`

### [3. Star wars movie title](./3-starwars_title.js)
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- [x] The first argument is the movie ID
- [x] You must use the [Star wars API](https://alx-intranet.hbtn.io/rltoken/YMr5jJ8pkuJCZDTyIWc7Aw) with the endpoint `https://swapi-api.hbtn.io/api/films/:id`
- [x] You must use the module `request`

### [4. Star wars Wedge Antilles](./4-starwars_count.js)
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

- [x] The first argument is the API URL of the Star wars API: `https://swapi-api.hbtn.io/api/films/`
- [x] Wedge Antilles is character ID `18` - your script **must** use this ID for filtering the result of the API
- [x] You must use the module `request`

### [5. Loripsum](./5-request_store.js)
Write a script that gets the contents of a webpage and stores it in a file.

- [x] The first argument is the URL to request
- [x] The second argument the file path to store the body response
- [x] The file must be UTF-8 encoded
- [x] You must use the module `request`

### 6. [How many completed?](./6-completed_tasks.js)
Write a script that computes the number of tasks completed by user id.

- [x] The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
- [x] Only print users with completed task
- [x] You must use the module `request`
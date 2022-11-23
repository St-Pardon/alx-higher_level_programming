# 0x15. JavaScript - Web jQuery

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/4724718.jpg)

## Import JQuery
```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/1f1ihd.jpg)

## Tasks

### [0. No JQuery](./0-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- [x] You must use `document.querySelector` to select the HTML tag
- [x] You can’t use the JQuery API

### [1. With JQuery](./1-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API

### [2. Click and turn red](./2-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API

### [3. Add `.red` class](./3-script.js)
Write a JavaScript script that adds the class red to the `<header>` element when the user clicks on the tag `DIV#red_header`

- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API

### [4. Toggle classes](./4-script.js)
Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:

- [x] The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
If the current class is red, when the user click on DIV#toggle_header, the class must be updated to `green` ; and the reverse.
- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API

### [5. List of elements](./5-script.js)
Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:

- [x] The new element must be: `<li>Item</li>`
- [x] The new element must be added to `UL.my_list`
- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API

### [6. Change the text](./6-script.js)
Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`

- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API

### [7. Star wars character](./7-script.js)
Write a JavaScript script that fetches the character `name` from this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

- [x] The name must be displayed in the HTML tag `DIV#character`
- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API

### [8. Star Wars movies](./8-script.js)
Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

- [x] All movie titles must be list in the HTML tag `UL#list_movies`
- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API

### [9. Say Hello!](./9-script.js)
Write a JavaScript script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello.`

- [x] The translation of “hello” must be displayed in the HTML tag `DIV#hello`
- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API
- [x] Your script must work when it is imported from the `<head>` tag

### [10. No jQuery - document loaded](./100-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- [x] You must use `document.querySelector` to select the HTML tag
- [x] You can’t use the jQuery API
- [x] Note: Your script must be imported from the `<head>` tag, not at the end of the HTML


### [11. List, add, remove](./101-script.js)
Write a JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks:

- [x]The new element must be: `<li>Item</li>`
- [x] The new element must be added to `UL.my_list`
- [x] When the user clicks on `DIV#add_item:` a new element is added to the list
- [x] When the user clicks on `DIV#remove_item:` the last element is removed from the list
- [x] When the user clicks on `DIV#clear_list:` all elements of the list are removed
- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API
- [x] You script must work when it imported from the `HEAD` tag

### [12. Say hello to everybody!](./102-script.js)
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

- [x] You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
- [x] The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
- [x] The translation must be fetched when the user clicks on `INPUT#btn_translate`
- [x] The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API
- [x] You script must work when imported from the `<head>` tag

### [13. And press ENTER](./103-script.js)
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
- [x] The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
- [x] The translation must be fetched when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
- [x] The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
- [x] You can’t use `document.querySelector` to select the HTML tag
- [x] You must use the JQuery API
- [x] You script must work when imported from the `<head>` tag
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
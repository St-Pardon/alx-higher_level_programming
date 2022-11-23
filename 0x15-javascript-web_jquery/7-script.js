$('document').ready(() => {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data, status) => {
    $('DIV#character').html(data.name);
  });
});

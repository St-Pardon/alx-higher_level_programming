$('document').ready(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, status) => {
    data.results.forEach(item => {
      $('UL#list_movies').append(`<li>${item.title}</li>`);
    });
  });
});

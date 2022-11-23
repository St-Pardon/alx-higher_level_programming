$('document').ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, status) => {
    $('DIV#hello').html(data.hello);
  });
});

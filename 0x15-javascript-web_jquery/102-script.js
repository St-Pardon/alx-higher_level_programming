$(() => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').val();

    $.get(`https://fourtonfish.com/hellosalut/?lang=${code}`, (data, status) => {
      $('DIV#hello').html(data.hello);
    });
  });
});

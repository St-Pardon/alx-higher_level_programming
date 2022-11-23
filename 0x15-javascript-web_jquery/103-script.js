$(() => {
  const translateHello = () => {
    const code = $('INPUT#language_code').val();

    $.get(`https://fourtonfish.com/hellosalut/?lang=${code}`, (data, status) => {
      $('DIV#hello').html(data.hello);
    });
  };

  $('INPUT#btn_translate').click(translateHello);
  $('INPUT#language_code').keydown((e) => {
    if (e.key === 'Enter') translateHello();
  });
});

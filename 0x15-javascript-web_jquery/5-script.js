$('document').ready(() => {
  $('DIV#add_item').click(() => {
    const li = document.createElement('li');

    li.textContent = 'Item';
    $('UL.my_list').append(li);
  });
});

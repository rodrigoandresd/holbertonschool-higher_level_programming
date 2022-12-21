
$.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', (content) => {
    $('#hello').text(content.hello);
});

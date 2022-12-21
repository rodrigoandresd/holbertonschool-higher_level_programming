
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (content) => {
  for (const MOVIE of content.results) {
    $('#list_movies').append(`<li>${MOVIE.title}</li>`)
  }
});

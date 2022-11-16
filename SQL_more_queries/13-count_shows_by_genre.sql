-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS 'genre',
    COUNT(tv_shows.title) AS 'number_of_shows'
FROM tv_genres
    JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
    LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.id IS NOT NULL
GROUP BY tv_genres.name
ORDER BY COUNT(tv_shows.id) DESC;
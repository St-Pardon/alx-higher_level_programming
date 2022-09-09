-- script that lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each.
SELECT tv_shows.title, tv_genres.name
    FROM tv_shows
    LEFT JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres
        ON tv_genres.id = tv_show_genres.genre_id
    ORDER BY tv_shows.title, tv_genres.name ASC;

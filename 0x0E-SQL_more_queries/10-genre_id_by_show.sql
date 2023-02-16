#!/bin/bash

-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
mysql -u -uroot -p hbtn_0d_tvshows < ~/alx-higher_level_programming/0x0E-SQL_more_queries/10-genre_id_by_show.sql
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;


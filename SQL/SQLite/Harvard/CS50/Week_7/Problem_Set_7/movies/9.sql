SELECT people.name FROM people INNER JOIN movies, stars ON movies.id = stars.movie_id AND people.id = stars.person_id WHERE movies.year = "2004" ORDER BY people.birth;

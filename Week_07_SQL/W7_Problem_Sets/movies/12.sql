-- Select the titles of movies
SELECT m.title
FROM movies m
-- Join stars table to get movie-star relationships
JOIN stars s ON m.id = s.movie_id
-- Join people table to get star details
JOIN people p ON p.id = s.person_id
-- Filter for movies starring Bradley Cooper
WHERE p.name = 'Bradley Cooper'
-- Further filter for movies also starring Jennifer Lawrence
AND m.id IN (
    SELECT s.movie_id
    FROM stars s
    JOIN people p ON p.id = s.person_id
    WHERE p.name = 'Jennifer Lawrence'
);
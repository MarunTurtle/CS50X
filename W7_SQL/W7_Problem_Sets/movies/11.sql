-- Select the titles of movies
SELECT m.title
-- Join the ratings table to get movie ratings
FROM movies m
JOIN ratings r ON r.movie_id = m.id
-- Join the stars table to get the actors in the movies
JOIN stars s ON s.movie_id = m.id
-- Join the people table to get actor details
JOIN people p ON s.person_id = p.id
-- Filter for movies starring Chadwick Boseman
WHERE p.name = 'Chadwick Boseman'
-- Order the results by rating in descending order
ORDER BY r.rating DESC
-- Limit the results to the top 5 movies
LIMIT 5;
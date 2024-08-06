-- Select the names of people who starred in the movie 'Toy Story'
SELECT p.name
FROM people p
-- Join stars table to link people with their roles in movies
JOIN stars s ON s.person_id = p.id
-- Join movies table to filter by the specific movie title
JOIN movies m ON s.movie_id = m.id
-- Filter for the movie 'Toy Story'
WHERE m.title = 'Toy Story'
-- Order the results alphabetically by name
ORDER BY p.name ASC;
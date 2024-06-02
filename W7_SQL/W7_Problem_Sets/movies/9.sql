-- Select distinct names of people who starred in movies released in 2004
SELECT DISTINCT p.name
FROM people p
-- Join stars table to link people with their roles in movies
JOIN stars s ON s.person_id = p.id
-- Join movies table to filter by movie release year
JOIN movies m ON s.movie_id = m.id
-- Filter movies released in the year 2004
WHERE m.year = 2004
-- Order results by birth date in ascending order
ORDER BY p.birth ASC;
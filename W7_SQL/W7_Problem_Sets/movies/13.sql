-- Select distinct names of people who have co-starred with Kevin Bacon
SELECT DISTINCT p.name 
FROM people p
-- Join stars table to link people with movies
JOIN stars s ON s.person_id = p.id
-- Join movies table to get movie details
JOIN movies m ON s.movie_id = m.id
-- Filter movies that include Kevin Bacon
WHERE m.id IN (
    -- Subquery to find movies featuring Kevin Bacon
    SELECT DISTINCT m.id
    FROM movies m
    -- Join stars table to link movies with people
    JOIN stars s ON s.movie_id = m.id
    -- Join people table to get person details
    JOIN people p ON s.person_id = p.id
    -- Filter for Kevin Bacon born in 1958
    WHERE p.name = 'Kevin Bacon' AND p.birth = 1958
)
-- Exclude Kevin Bacon from the result
AND p.name != 'Kevin Bacon';
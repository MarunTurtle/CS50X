SELECT DISTINCT p.name FROM people p
JOIN stars s ON s.person_id = p.id
JOIN movies m ON s.movie_id = m.id
WHERE m.id IN (
    SELECT distinct m.id
    FROM movies m
    JOIN stars s ON s.movie_id = m.id
    JOIN people p ON s.person_id = p.id
    WHERE p.name = 'Kevin Bacon' and p.birth = 1958
)
AND p.name != 'Kevin Bacon';

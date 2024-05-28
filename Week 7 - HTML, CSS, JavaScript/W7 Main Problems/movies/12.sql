SELECT m.title
FROM movies m
JOIN stars s ON m.id = s.movie_id
JOIN people p ON p.id = s.person_id
WHERE p.name = 'Bradley Cooper'
AND m.id IN (
    SELECT s.movie_id
    FROM stars s
    JOIN people p ON p.id = s.person_id
    WHERE p.name = 'Jennifer Lawrence'
);

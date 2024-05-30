-- Select distinct names of people who are directors of highly-rated movies
SELECT DISTINCT p.name
FROM people p
-- Join directors table to get director information
JOIN directors d ON p.id = d.person_id
-- Join movies table to get movie information
JOIN movies m ON d.movie_id = m.id
-- Join ratings table to filter movies with high ratings
JOIN ratings r ON m.id = r.movie_id
-- Filter for movies with a rating of 9.0 or higher
WHERE r.rating >= 9.0
-- Order the results by rating in descending order
ORDER BY r.rating DESC;
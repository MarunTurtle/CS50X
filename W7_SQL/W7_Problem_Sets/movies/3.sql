-- Select the titles of movies released in or after 2018
-- Order the results alphabetically by title
SELECT title 
FROM movies 
WHERE year >= 2018 
ORDER BY title ASC;
-- Select the title and year of movies
-- Filter movies with titles containing 'Harry Potter'
-- Order the results by year in ascending order
SELECT title, year 
FROM movies 
WHERE movies.title LIKE ('%Harry Potter%') 
ORDER BY movies.year ASC;
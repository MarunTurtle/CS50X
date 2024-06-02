-- Select movie titles and their ratings
SELECT movies.title, ratings.rating
FROM movies
-- Join movies with ratings based on movie ID
JOIN ratings ON movies.id = ratings.movie_id
-- Filter for movies released in the year 2010
WHERE movies.year = 2010
-- Order results by rating in descending order, then by title in ascending order
ORDER BY ratings.rating DESC, movies.title ASC;
-- Count the number of ratings that are equal to 10
SELECT COUNT(rating) 
FROM ratings 
WHERE ratings.rating = 10;
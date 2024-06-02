-- Select the name of songs by the artist 'Post Malone'
SELECT name 
FROM songs 
WHERE artist_id = (
    -- Subquery to find the artist_id of 'Post Malone'
    SELECT id 
    FROM artists 
    WHERE name = 'Post Malone'
);
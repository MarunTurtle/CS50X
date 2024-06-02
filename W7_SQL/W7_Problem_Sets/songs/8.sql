-- Select the names of artists and their songs
SELECT artists.name, songs.name
FROM songs
-- Join the artists table to get artist details
JOIN artists ON artists.id = songs.artist_id
-- Filter songs that feature other artists
WHERE songs.name LIKE '%feat.%';
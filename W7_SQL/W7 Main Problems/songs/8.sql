SELECT artists.name, songs.name
FROM songs
JOIN artists ON artists.id = songs.artist_id
WHERE songs.name LIKE '%feat.%';

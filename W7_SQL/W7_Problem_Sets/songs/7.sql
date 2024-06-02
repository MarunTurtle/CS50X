-- Select the average energy of songs by the artist 'Drake'
SELECT AVG(energy)
FROM songs
JOIN artists ON artists.id = songs.artist_id  -- Join songs with artists based on artist ID
WHERE artists.name = 'Drake';  -- Filter for songs by the artist 'Drake'
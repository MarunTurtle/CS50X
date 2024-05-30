SELECT AVG(energy)
FRom songs
JOIN artists ON artists.id = songs.artist_id
WHERE artists.name = 'Drake';

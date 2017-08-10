-- Music DB exercise - Schema:
CREATE TABLE artist ( id SERIAL PRIMARY KEY, name VARCHAR );
CREATE TABLE album ( id SERIAL PRIMARY KEY, name VARCHAR, released DATE );
CREATE TABLE song ( id SERIAL PRIMARY KEY, name VARCHAR, writer VARCHAR );
CREATE TABLE artist_to_album ( id SERIAL PRIMARY KEY, artist_id INTEGER REFERENCES artist (id), album_id INTEGER REFERENCES album (id), lead BOOLEAN);
CREATE TABLE track ( id SERIAL PRIMARY KEY, name VARCHAR, duration INTERVAL, album_id INTEGER REFERENCES album (id), song_id INTEGER REFERENCES song (id) );
CREATE TABLE instrument ( id SERIAL PRIMARY KEY, name VARCHAR );
CREATE TABLE track_to_instrument ( id SERIAL PRIMARY KEY, track_id INTEGER REFERENCES track (id), instrument_id INTEGER REFERENCES instrument (id) );

-- Questions
-- Problem 1
SELECT * FROM track WHERE track.album_id = 3;
-- Problem 2
SELECT * FROM track JOIN artist_to_album ON artist_to_album.album_id = track.album_id JOIN artist ON artist_to_album.artist_id = artist.id WHERE artist.id = 2;
-- Problem 3
SELECT * FROM track WHERE track.duration = (SELECT MAX(track.duration) FROM track);
-- Problem 4
SELECT * FROM album WHERE album.released > '2005-01-01' AND album.released < '2010-01-01';
-- Problem 5
SELECT COUNT(album.id) FROM album JOIN artist_to_album ON artist_to_album.album_id = album.id JOIN artist ON artist_to_album.artist_id = artist.id WHERE artist.id = 2 AND album.released < '2005-01-01';
-- Problem 6
SELECT artist.name, album.name FROM album JOIN artist_to_album ON artist_to_album.album_id = album.id JOIN artist ON artist_to_album.artist_id = artist.id WHERE album.released = (SELECT MAX(album.released) FROM album);
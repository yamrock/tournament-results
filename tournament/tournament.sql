-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- CREATE TABLE players (id SERIAL PRIMARY KEY NOT NULL, 
-- 		      name TEXT );
CREATE TABLE standings (id SERIAL PRIMARY KEY NOT NULL,
			name TEXT , 
			wins INTEGER, 
			matches INTEGER );

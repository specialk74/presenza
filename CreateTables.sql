DROP TABLE IF EXISTS presenza;

CREATE TABLE presenza (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL,
	pranzo INTEGER NOT NULL,
	cena INTEGER NOT NULL,
	dormire INTEGER NOT NULL,
	macchina INTEGER NOT NULL,
	pranzoDefault INTEGER NOT NULL,
	cenaDefault INTEGER NOT NULL,
	dormireDefault INTEGER NOT NULL,
	lastupdate DATE NOT NULL
);

INSERT INTO presenza (name, patente, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Marco",   1, 96,127,127, datetime());
INSERT INTO presenza (name, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Simona",  96,127,127, datetime());
INSERT INTO presenza (name, patente, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Lucia",   1, 0,0,0, datetime());
INSERT INTO presenza (name, patente, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Gabriele",1, 0,0,0, datetime());
INSERT INTO presenza (name, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Paolo",   0,0,0, datetime());
INSERT INTO presenza (name, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Michele", 96,127,127, datetime());

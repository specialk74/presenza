DROP TABLE IF EXISTS presenza;

CREATE TABLE presenza (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL,
	pranzo INTEGER NOT NULL,
	cena INTEGER NOT NULL,
	dormire INTEGER NOT NULL,
	pranzoDefault BOOLEAN NOT NULL,
	cenaDefault BOOLEAN NOT NULL,
	dormireDefault BOOLEAN NOT NULL,
	lastupdate DATE NOT NULL
);

INSERT INTO presenza (name, pranzo, cena, dormire, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Marco",   0,0,0,0,1,1, datetime());
INSERT INTO presenza (name, pranzo, cena, dormire, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Simona",  0,0,0,0,1,1, datetime());
INSERT INTO presenza (name, pranzo, cena, dormire, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Lucia",   0,0,0,0,0,0, datetime());
INSERT INTO presenza (name, pranzo, cena, dormire, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Gabriele",0,0,0,0,0,0, datetime());
INSERT INTO presenza (name, pranzo, cena, dormire, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Paolo",   0,0,0,0,0,0, datetime());
INSERT INTO presenza (name, pranzo, cena, dormire, pranzoDefault, cenaDefault, dormireDefault, lastupdate) VALUES ("Michele", 0,0,0,0,1,1, datetime());

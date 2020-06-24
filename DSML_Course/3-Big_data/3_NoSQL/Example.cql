DESC KEYSPACES;
create KEYSPACE example WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor': 1};
DESC KEYSPACES;
USE example;
CREATE TABLE users (user_name varchar, password varchar, gender varchar, last_name varchar, PRIMARY KEY (user_name));
INSERT INTO users (user_name, password, gender, last_name) VALUES ('pperezc', 'mypass', 'male', 'perez');
SELECT * FROM users WHERE last_name='perez';
SELECT * FROM users WHERE last_name='perez' ALLOW FILTERING;
CREATE INDEX ON users(last_name);
SELECT * FROM users WHERE last_name='perez';
ALTER TABLE users ADD name varchar;
UPDATE users SET name='pedro' WHERE user_name='pperezc';
SELECT * FROM users;
SELECT * FROM users WHERE last_name='perez';
SELECT * FROM users LIMIT 1;
ALTER TABLE users ADD emails set<text>;
INSERT INTO users(user_name, password, gender, last_name, emails) VALUES ('Laura', '5m8svvd', 'female', 'Paez', {'lau@uno.com'});
SELECT * FROM users;
UPDATE users SET emails = emails+{'lau1234@uno.com'} WHERE user_name = 'Laura';
SELECT * FROM users;
ALTER TABLE users ADD top_places list<text>;
UPDATE users SET top_places = ['rivendell', 'rohan'] WHERE user_name = 'Laura';
SELECT * FROM users;
UPDATE users SET top_places = top_places+['the shire'] WHERE user_name='Laura';
SELECT * FROM users;
UPDATE users SET top_places[2] = 'riddermark' WHERE user_name='Laura';
SELECT * FROM users;
DELETE top_places[1] FROM users WHERE user_name = 'Laura';
SELECT * FROM users;
ALTER TABLE users ADD telefonos map<text, text>;
UPDATE users SET telefonos ={'casa':'123456', 'oficina':'1236'} WHERE user_name='Laura';
SELECT * FROM users;
UPDATE users SET telefonos['celular'] = '3012356' WHERE user_name='Laura';
SELECT * FROM users;





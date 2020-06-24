DESC keyspace;
CREATE KEYSPACE IF NOT EXISTS twitter WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};
USE twitter;

-- Se crea la tabla y tres usuarios iniciales x,y,z todos se siguen entre ellos.
CREATE TABLE users(user_id int, username varchar, email set<text>, seguidos list<text>, seguidores list<text>, PRIMARY KEY (user_id));
INSERT INTO users(user_id, username, email, seguidos, seguidores)VALUES (1,'x', {'x@gmail.com'},['y','z'],['y','z']);
INSERT INTO users(user_id, username, email, seguidos, seguidores)VALUES (2,'y', {'y@gmail.com'},['x','z'],['x','z']);
INSERT INTO users(user_id, username, email, seguidos, seguidores)VALUES (3,'z', {'z@gmail.com'},['x','y'],['x','y']);

-- Entra un nuevo usuario w que sigue a x,y,z pero no lo siguen aun.
INSERT INTO users(user_id, username, email, seguidos)VALUES (4,'w', {'w@gmail.com'},['x','y','z']);

UPDATE users SET seguidores = seguidores+['w']  WHERE user_id = 1;
UPDATE users SET seguidores = seguidores+['w']  WHERE user_id = 2;
UPDATE users SET seguidores = seguidores+['w']  WHERE user_id = 3;

-- Punto 1
CREATE INDEX ON users(username);
SELECT seguidos FROM users WHERE username = 'x';
SELECT seguidores FROM users WHERE username = 'y';
SELECT seguidores FROM users WHERE username = 'x' AND seguidores CONTAINS 'y' ALLOW FILTERING;

-- Punto 2 El usuario x deja de seguir a z y ahora sigue a w.
DELETE seguidos[1] FROM users WHERE user_id = 1;
DELETE seguidores[0] FROM users WHERE user_id = 3;
UPDATE users SET seguidos = seguidos +['w']  WHERE user_id = 1;

SELECT seguidos, seguidores FROM users;
SELECT * FROM users;


--//Tabla 
--//user_id | email           | seguidores      | seguidos        | username
--//————+————————+————————+————————+—————
--//       1 | {'x@gmail.com'} | ['y', 'z', 'w'] |      ['y', 'w'] |        x--
--//       2 | {'y@gmail.com'} | ['x', 'z', 'w'] |      ['x', 'z'] |        y
--//       4 | {'w@gmail.com'} |            null | ['x', 'y', 'z'] |        w
--//       3 | {'z@gmail.com'} |      ['y', 'w'] |      ['x', 'y'] |        z
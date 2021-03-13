CREATE DATABASE IF NOT EXISTS data;
use data;

CREATE TABLE users(
  email VARCHAR(100),
  password TEXT,
  PRIMARY KEY (email)
);

INSERT INTO users VALUES ('coyote@acme.es', '8dbfcfc23f22c58c1b200821f89fc103');
COMMIT;

CREATE TABLE items(
  name VARCHAR(30),
  description VARCHAR(200),
  image TEXT,
  PRIMARY KEY (name)
);

INSERT INTO items VALUES ('yunque', 'Yunque estandar de 80kg', 'https://i.pinimg.com/originals/6e/97/35/6e9735420a8b3f23998b4f3aa7150f31.png');
INSERT INTO items VALUES ('cohete', 'Cohete estandar de 100km/h', 'http://americandigest.org/sidelines/CJLAR.jpg');
INSERT INTO items VALUES ('dinamita', 'TNT 100 Megatones', 'http://3.bp.blogspot.com/-1mXk1jSqilQ/VGvOfpdLQuI/AAAAAAAAgic/j9gHkoY_Xao/s1600/coyote_dinamita1.jpg');
COMMIT;


CREATE TABLE orders(
  email VARCHAR(100),
  name VARCHAR(30),
  FOREIGN KEY (email) REFERENCES users(email) ON DELETE CASCADE,
  FOREIGN KEY (name) REFERENCES items(name) ON DELETE CASCADE,
  PRIMARY KEY (email, name)
);

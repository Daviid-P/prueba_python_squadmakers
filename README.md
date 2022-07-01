# Tarea 2:
## ¿Qué repositorio utilizarías?

Usaria MongoDB porque es lo que usaba en las practicas que acabé hace poco, lo tengo fresco, es facil de usar y para guardar texto ya nos vale, seguramente usando alguna dependencia como flask-pydantic

```
use jokes_db
```

```js
db.jokes.insert({number: 1, string: "El chiste"})
```


Si tuviera que usar una base de datos relacional usaria PostgreSQL o MariaDB con SQLalchemy ya que son gratis y opensource, aunque para este proyecto en concreto SQLite ya valdria.

- PostgreSQL
```postgresql
CREATE DATABASE jokes_db;

CREATE TABLE jokes (
    number INT PRIMARY KEY,
    string VARCHAR UNIQUE,
    CHECK (string <> '')
);
```

- MariaDB
```SQL
CREATE DATABASE jokes_db;

CREATE TABLE jokes (
    number INT NOT NULL AUTO_INCREMENT,
    string VARCHAR NOT NULL,
    CONSTRAINT number_pk PRIMARY KEY (number)
    CONSTRAINT string_unique UNIQUE (string)
    CONSTRAINT sting_not_empy CHECK (string <> '')
);
```
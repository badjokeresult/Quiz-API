GRANT ALL PRIVILEGES ON DATABASE "quizdb" TO quizuser;

DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS question;

CREATE TABLE category
    (id INT PRIMARY KEY NOT NULL,
     title VARCHAR NOT NULL,
     created_at TIMESTAMP NOT NULL);

CREATE TABLE question
    (id INT PRIMARY KEY NOT NULL,
     answer VARCHAR NOT NULL,
     question VARCHAR NOT NULL,
     created_at TIMESTAMP NOT NULL,
     category_id INT NOT NULL,
     CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES category(id));
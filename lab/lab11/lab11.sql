.read lab11_data.sql


CREATE TABLE bluedog AS
  SELECT color,pet FROM students WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color,pet,song FROM students WHERE color = "blue" AND pet = "dog"  ;


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;



CREATE TABLE matchmaker AS
  SELECT a.pet,a.song,a.color,b.color from students as a,students as b where a.time <b.time and a.song = b.song and a.pet = b.pet;


CREATE TABLE sevens AS
  SELECT seven from students ,numbers where students.time = numbers.time and students.number = 7 and numbers."7"="True";


CREATE TABLE avg_difference AS
  SELECT round(avg(abs(number - smallest))) from students;


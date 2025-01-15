.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size from dogs , sizes where height <=max and height > min;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT ac.name
    from dogs as ac,dogs as ap,parents as b where ac.name = b.child and ap.name = b.parent order by -ap.height;


-- Sentences about siblings that are the same size
CREATE TABLE help AS
  SELECT a.name as name1,b.name as name2,a.size as samesize 
    FROM parents as p,parents as q, size_of_dogs as a,size_of_dogs as b WHERE a.size = b.size and a.name < b.name and a.name = p.child and b.name = q.child and p.parent = q.parent;

CREATE TABLE sentences AS
  SELECT 'The two siblings, '|| name1 || ' plus ' || name2 ||' have the same size: ' || samesize from help;

'''CREATE TABLE parents AS
  SELECT 'abraham' AS parent, 'barack' AS child UNION
  SELECT 'abraham'          , 'clinton'         UNION
  SELECT 'delano'           , 'herbert'         UNION
  SELECT 'fillmore'         , 'abraham'         UNION
  SELECT 'fillmore'         , 'delano'          UNION
  SELECT 'fillmore'         , 'grover'          UNION
  SELECT 'eisenhower'       , 'fillmore';

CREATE TABLE dogs AS
  SELECT 'abraham' AS name, 'long' AS fur, 26 AS height UNION
  SELECT 'barack'         , 'short'      , 52           UNION
  SELECT 'clinton'        , 'long'       , 47           UNION
  SELECT 'delano'         , 'long'       , 46           UNION
  SELECT 'eisenhower'     , 'short'      , 35           UNION
  SELECT 'fillmore'       , 'curly'      , 32           UNION
  SELECT 'grover'         , 'short'      , 28           UNION
  SELECT 'herbert'        , 'curly'      , 31;

CREATE TABLE sizes AS
  SELECT 'toy' AS size, 24 AS min, 28 AS max UNION
  SELECT 'mini'       , 28       , 35        UNION
  SELECT 'medium'     , 35       , 45        UNION
  SELECT 'standard'   , 45       , 60;'''
  
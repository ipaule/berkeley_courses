CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- Q1 --
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name, b.size FROM dogs as a, sizes as b WHERE min < height and height <= max;

-- Q2 --
-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child FROM parents, dogs WHERE parent = name ORDER BY -height;

-- Q3 --
-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS small, b.child AS big FROM parents AS a, parents AS b WHERE a.parent = b.parent
  AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.small || ' and ' || a.big || ' are ' || b.size || ' siblings'
  FROM siblings AS a, size_of_dogs AS b, size_of_dogs AS c
  WHERE a.small = b.name and a.big = c.name and b.size = c.size;

-- Q4 --
-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);
-- Add your INSERT INTOs here

CREATE TABLE stacks AS
SELECT a.name || ', ' || b.name || ', ' || c.name || ', ' || d.name as doglist,
      a.height + b.height + c.height + d.height as total
FROM dogs as a, dogs as b, dogs as c, dogs as d
WHERE a.height < b.height and b.height < c.height and c.height < d.height
  and a.height + b.height + c.height + d.height > 170 order by total;

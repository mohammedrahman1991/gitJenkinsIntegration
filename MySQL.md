https://www.youtube.com/watch?v=7S_tz1z_5bA

Go to youtube page; learn to install

or go to :
1. mysql.com/downloads/
search downloads 

click community downloads
download Community server:
https://dev.mysql.com/downloads/mysql/
match version to computer
then go back to downloads
download latest version of:
MySQLWorkBench:
link: https://dev.mysql.com/downloads/workbench/

now run the Workbench


//// Using MaqlWorkBench
import databases


next type query to select a specific datsbase
USE sql_store

SELECT cthen collumns
SELECT *; = all  //make sure colon is added here
FROM customers
WHERE = filers
WHERE customer_id = 1
use --
hyphins to comment out line
ORDER BY first_name

order matters for clauses:
otherwise ull have syntax error:
"note use capital letter on commands"
1st. : SELECT
2.: FROM
3. WHERE
4. ORDER BY
puT each clause in seperate line even though u can put in same to avoid confusion

select all customers from customer table

SELECT has multiple uses

ie: SELECT last_name, first_name, points
SELECT last_name, first_name, points, points+10
SELECT last_name, first_name, points, points*10+100
SELECT last_name, first_name, points, (points*10)+100 AS discount_factor //will rename the column
SELECT last_name, first_name, points, (points*10)+100 AS 'discount factor'

now go to another table
u can edit table directly then click apply for changes 

SELECT state
FROM customers

will reveal duplicates as well
if u want to remove duplicates use
SELECT DISCTINCT state
FROM customers

specific queries:
SELECT *
FROM customers
WHERE points >3000
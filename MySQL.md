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

can use other operators
SELECT *
FROM customers
WHERE state = 'VA'

for specific queries

or WHERE birth_date > '1990-01-01'

go to another chart like so:
SELECT *
FROM orders
WHERE order_date >= '2019-01-01'

GRABS one value from chart very specific

can use AND operator with 2nd condition

SELECT *
FROM customers
WHERE birth_date > '1990-01-01' or points >1000 AND state = 'VA'


we can negate it
SELECT *
FROM customers
WHERE NOT (birth_date > '1990-01-01' or points >1000 AND state = 'VA')
negates each condition or does oposite

or can switch operators
WHERE birth_date < '1990-01-01' or points >1000 AND state = 'VA'

IN operator

SELECT *
FROM customers
WHERE state IN ('VA', 'WA', 'GA')

BETWEEN makes code cleaner
ie: 
SELECT *
FROM customers
WHERE points >= 1000 AND points <= 3000

or 
SELECT *
FROM customers
WHERE points BETWEEN 

get letters based on 1 letter
ie:
SELECT *
FROM customers
WHERE last_name LIKE '%b%'

this query will display all last_names in customer chart that contain the letter B capital or small
any position of their name
the % allows us to do that 

to find all letters that last name end with y
type: 
SELECT *
FROM customers
WHERE last_name LIKE '%y'

exact 2 letters :
WHERE last_name LIKE '_y'

or 5 letters that have ending y"
WHERE last_name LIKE '_____y'

this is used with LIKE
% = any number of charatcers
_ = single character

old operator is LIKE
but new OPERATOR is : 

Regular Expressions

SELECT *
FROM customers
WHERE last_name LIKE '%field%'
WHERE last_name REGEXP 'field'
WHERE last_name REGEXP '^field'  returns null
this is because carrot sign or ^ is used for beggining of word. THere are
no fields that start with field thus null
WHERE last_name REGEXP 'field$'
$ = end of name
this will show results 

WHERE last_name REGEXP 'field|mac|rose'
3 customers
| = or
multiple seearch patterns
WHERE last_name REGEXP 'e[fmq]'
can also supply range of characters
WHERE last_name REGEXP '[a-h]e'

^ begginig
$ ending
| logical or
[abcd]
[a-f]e
before the letter e [a-f] can appear
or '[gim]e' this is before e any customer last name
or it can be after e
'e[fmq]'

how to find NULL values
SELECT *
FROM customers
WHERE phone IS NULL

returns 1 value where there is NULL
can do opposite by typing:
WHERE phone IS NOT NULL

write a query on orders not shipped yet
go to orders tables
look at data

SELECT *
FROM orders
WHERE shipped_date IS  NULL

how to SORT data from sql queries
sort by ID

SELECT *
FROM customers
ORDER BY first_name
can also doing it in descneding order
ORDER BY first_name DESC

ORDER BY state, first_name
can also sort specifics in ASC or DESC
like so:
ORDER BY state DESC, first_name ASC

MY sql we can sort by any collusm whether its in SELECT clause or not
SELECT first_name, last_name, 10+1 AS Points
FROM customers
ORDER BY points, first_name

can also do:
SELECT first_name, last_name
FROM customers
ORDER BY 1,2 - this is no good
so sort by collum name
ORDER BY last_name, first_name.
-----

SELECT *
FROM order_items
WHERE order_id = 2
ORDER BY quantity * unit price DESC

or we can

SELECT *, quantity * unit_price AS total_price
FROM order_items
WHERE order_id = 2
ORDER BY total_price DESC

THE LIMIT CLAUSE
how to limit number o f records from query

SELECT *
FROM customers
LIMIT 3

how to skip 
SELECT *
FROM customers
LIMIT 6,3
this means it will skip first 6, then display next 3

now lets find the most loyal customers
SELECT *
FROM customers
ORDER BY points DESC [highest to least]
now i want to grab top 3

LIMIT 3

now to select from multiple charts
SELECT *
FROM orders
INNER JOIN / OUTER JOIN

inner keyword is options

We want to join orders tables with customer table

ON phrase then type condition ordrers.customer_id = customers.customer_id
make sure customer ID column 
lign up records so columns are equal
wheneer we joining, make sure CUSTOMER ID colum in order table = customers ID colymn on customrers

SELECT *
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id

so to be more specific instead of SELECT *
we can write 

SELECT order_id, first_name, last_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id

can also make it display customer_id

SELECT order_id, orders.customer_id, first_name, last_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id

----
can also make code look less redudant, pay close attention to abbreviation [ALIAS] o for orders, & c for customers
SELECT order_id, o.customer_id, first_name, last_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
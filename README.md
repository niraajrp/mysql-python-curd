# mysql-python-curd

I've used XAMPP's Apache and MySQL model to run the database on localhost.
This program lets you manually enter, update and delete entries in a table of a database. 

Database Specifications in accordance with code:::
Database used: MySQL
Database name : twitter
Table name: tweets_table
Column headers: id, username, tweet, date_created


Points to Remember::::

Exported copy of database(ie. twitter.sql) is placed under "database" folder. This "twitter.sql" file can be imported in MySQL for easy operations or you can create the database from scratch with same parameters as mentioned in the python code

Program will throw error if database name, table name and table column header do not match with what is mentioned in program.
# Logs Analysis Project

## Intro

The `news` database contains newspaper articles, as well as the web server log
for the site. The log has a database row for each time a reader loaded a web
page. The main idea of the project is to build an *internal reporting tool*
that uses information from the database to answer questions about the site's
user activity:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## The database overview

The `news` database contains three tables:
- *articles*
- *authors*
- *log*

The `articles` table has the following columns:
- **author** (id of the author, integer)
- **title** (title of the article, text)
- **slug** (part of the article's path, text)
- **lead** (lead of the article, text)
- **body** (body of the article, text)
- **time** (time of publishing, timestamp)
- **id** (id of the article, integer)

The `authors` table has the following columns:
- **name** (name of the author, text)
- **bio** (bio of the author, text)
- **id** (id of the author, integer)

The `log` table has the following columns:
- **path** (text)
- **ip** (inet)
- **method** (text)
- **status** (text)
- **time** (timestamp)
- **id** (integer)

## Implementation of the project

To perform the analysis and answer the questions mentioned in the *Intro*
section, specific data from all of the tables are compiled and processed with
a help of SQL.

`logs_analysis.py` contains the *queries* (SQL statements) to be executed
against the database, as well as the *functions* that force the execution and
present the results in a reader-friendly format.

## Dependencies (built with)

- [Python 3.7.0](https://www.python.org/downloads/)
- [PostgreSQL 9.5.13](https://www.postgresql.org/)
- [Psycopg 2](http://initd.org/psycopg/)

## How to run it

- Make sure **Python** is installed on your computer. Otherwise, download and
  install *Python 3.7.0* from the download page (see Dependencies above);
- download and install [Oracle VM Virtual Box](https://www.virtualbox.org/);
- make sure the CPU Virtualization is enabled;
- download and install [Vagrant](https://www.vagrantup.com/);
- download and unzip [VM configuration files](http://bit.ly/2BdmpWt);
- you should have the *FSND-Virtual-Machine* directory with the *vagrant*
  directory inside after the previous step;
- in your terminal, `cd` to the *vagrant* directory and run the command
  `vagrant up` (this causes Vagrant to download the Linux operating system and
  install it. It may take quite a while depending on how fast your Internet
  connection is);
- run `vagrant ssh` command to log into the virtual machine;
- download and unzip the [data](http://bit.ly/2MLVtyd) and put the
  *newsdata.sql* file to the *vagrant* directory;
- in your terminal, run the command `cd /vagrant`;
- run `psql -d news -f newsdata.sql` to connect to the database server, create
  tables and populating them with data;
- escape the *psql* mode;
- download `logs_analysis.py` and put it to the *vagrant* directory;
- run the command `python logs_analysis.py`.

## Outro: comments

For more information on the logic of the queries and functions explore the
comments to the `logs_analysis.py`.
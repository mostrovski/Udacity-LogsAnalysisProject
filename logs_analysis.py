#!/usr/bin/env python3

import psycopg2

'''
1. What are the most popular three articles of all time? The following query
connects the table of articles to the table of logs, and counts the number of
views for each article using that the 'path' in the logs table includes the
'slug' from the articles table; the output is sorted by the views number and
limited to three:
'''
popular_articles_query = """
select articles.title, count(log.path) as views_num from articles join log on
articles.slug = substring(log.path, 10) group by articles.title order by
views_num desc limit 3;
"""
'''
2. Who are the most popular article authors of all time? The following query
connects the table of articles to the table of authors (to have the author's
name associated with the article, not the id), connects it to the logs table,
and counts the number of views for each author; the output is sorted by the
views number:
'''
popular_authors_query = """
select name as contributor, count(log.path) as views_num from (select
authors.name, articles.title, articles.slug from authors join articles on
authors.id = articles.author) as auth_art join log on auth_art.slug =
substring(log.path, 10) group by contributor order by views_num desc;
"""
'''
3. On which days did more than 1% of requests lead to errors? The following
query works with the logs table. 1) It creates two subqueries (tables req_log
and err_log) to count the overall number of requests, and the number of
requests that raised an error for each day. 2) The next subquery (error_share)
uses those numbers to calculate the perecntage of errors for each day, and
sorts the table by this percentage. 3) The main query limits the output:
'''
error_days_query = """ select * from (select r_day as day,
round((100*error_num/request_num), 2) as error_percentage from (select
date(time) as r_day, cast(count(status) as decimal) as request_num from log
group by r_day) as req_log join (select date(time) as e_day,
cast(count(status) as decimal) as error_num from log where not status =
'200 OK' group by e_day) as err_log on req_log.r_day = err_log.e_day order by
error_percentage desc) as error_share where error_percentage > 1.00;
"""


def execute_query(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    query_result = c.fetchall()
    db.close()
    return query_result


def popular_articles():
    articles = execute_query(popular_articles_query)
    print("\n1. What are the most popular three articles of all time?\n")
    for article in articles:
        print("'" + str(article[0]) + "', " + str(article[1]) + " views\n")


def popular_authors():
    authors = execute_query(popular_authors_query)
    print("\n2. Who are the most popular article authors of all time?\n")
    for author in authors:
        print(str(author[0]) + ", " + str(author[1]) + " views\n")


def error_day():
    error_days = execute_query(error_days_query)
    print("\n3. On which days did more than 1% of requests lead to errors?\n")
    for error_day in error_days:
        print(str(error_day[0]) + ", " + str(error_day[1]) + "%"+" errors\n")


def analysis_results():
    popular_articles()
    popular_authors()
    error_day()

analysis_results()

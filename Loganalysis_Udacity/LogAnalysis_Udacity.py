#!/usr/bin/env python
import psycopg2
# first top three articles execution


def top_three_art():
    conn = psycopg2.connect(dbname="news", user='vagrant', password='vagrant')
    cur = conn.cursor()
    q1 = ''' SELECT title, count(*) as views FROM articles
             JOIN log
             ON articles.slug = substring(log.path, 10)
             GROUP BY title ORDER BY views DESC LIMIT 3; '''
    if(q1):
        cur.execute(q1)
        rs = cur.fetchall()
        print(" \n  ^^What are the top three articles of all time ? \n")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        count = 0
        for resu in rs:
            count = count+1
            print(resu[0] + str(resu[1]) + " views")
            print("++++++++++++++++++++++++++++++++++++++++++++++")
    else:
        print("Something went Wrong!")
# top four authors


def top_three_aut():
    conn = psycopg2.connect(dbname="news", user='vagrant', password='vagrant')
    cur = conn.cursor()
    q2 = '''
    SELECT authors.name, count(*) as views
    FROM articles
    JOIN authors
    ON articles.author = authors.id
    JOIN log
    ON articles.slug = substring(log.path, 10)
    WHERE log.status LIKE '200 OK'
    GROUP BY authors.name ORDER BY views DESC;
    '''
    if(q2):
        cur.execute(q2)
        rs = cur.fetchall()
        print("\n  ^^Who are the top article authors of all time ? \n")
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        count = 1
        for resu in rs:
            number = '(' + str(count) + ') "'
            tit = resu[0]
            views = '"\tAut' + str(resu[1]) + " views"
            print(tit + views)
            count = count+1
            print("++++++++++++++++++++++++++++++++++++++++++++++")
    else:
        print("Something went Wrong!")
# lead errors


def log_error_ana():
    conn = psycopg2.connect(dbname="news", user='vagrant', password='vagrant')
    cur = conn.cursor()
    q3 = '''
    SELECT round((dhat*2.0*5.0*10.0)/tripper, 3) as
    resu, to_char(errorphase, 'DD Mon YYYY')
    FROM runcount ORDER BY resu desc limit 1;
    '''
    if(q3):
        cur.execute(q3)
        rs = cur.fetchall()
        print("^^^Days on which more than 1% of requests lead to errors ? ")
        for resu in rs:
            print("\t" + str(resu[1]) + " - " + str(resu[0]) + "%")
    else:
        print("Something went Wrong!")
top_three_art()
top_three_aut()
log_error_ana()

# -*- encoding: utf-8 -*-
# Made by http://www.elmalabarista.com
# This will teach about how use the sqlite full text search
# abilities from python

# About

# You have a app used by users? Wanna a good search functionality?
# Then implement full text search (FTS). Is easy with sqlite, perform well
# and give good results. PostgreSQL is another database with good
# FTS functionality

# Official docs
# http://www.sqlite.org/fts3.html

# Usefull links
# https://en.wikipedia.org/wiki/Full_text_search
# http://docs.python.org/2/library/sqlite3.html

# Other FTS libraries, independent of the database engine
# http://pythonhosted.org/Whoosh/
# http://lucene.apache.org/core/
# http://sphinxsearch.com/

import collections
import datetime
#import sqlite3
import pyodbc
import sys


from utils import printTitle, printSubTitle, printExplain, printTab, printError

printTitle("You need to provide search functionality")
# print """
# Your app/web site need a way to give search results, fast & easy
# """

printSubTitle("First, we need a database")
# This will run in the memory

#conn = sqlite3.connect(':memory:')

conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=RAMCOBL267;DATABASE=PYTHONDB;UID=sa;PWD=development12$')

# conn.row_factory = sqlite3.Row


def exeSql(sql):
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    # return c.fetchall()


def selectSql(sql, params=None):
    c = conn.cursor()
    if params:
        c.execute(sql, params)
        
    else:
        c.execute(sql)
        
    return c.fetchall()


SQL_SCHEMA = """

if NOT exists( select * from sys.tables where name = 'persons')
    begin
    
    CREATE TABLE Persons
    (Per_Id INTEGER NOT NULL, 
     CONSTRAINT Persons_index_Id PRIMARY KEY CLUSTERED (Per_Id),
    FullName VARCHAR(100), 
    City VARCHAR(100), 
    Country VARCHAR(100),
    Phone VARCHAR(100),
    Street VARCHAR(100), 
    Email VARCHAR(100), 
    CreatedAt VARCHAR(100) )
    
    end

"""

SQL_INSERT = """

if NOT exists( select * from sys.tables where name = 'persons')
    begin
    INSERT INTO Persons (City,Country,Phone,FullName,Street,Per_Id,Email,CreatedAt) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    end
"""

#INSERT INTO Persons (City,Country,Phone,FullName,Per_Id,Street,Email,CreatedAt) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#?City,?Country,?Phone,?FullName,?Id,?Street,?Email,?CreatedAt

print (SQL_SCHEMA)
exeSql(SQL_SCHEMA)

from data import PERSONS
# Some data for testing
# Generated from http://www.databasetestdata.com/


def readCsv(csv_data):
    # A simple utily to read a CSV-like data as namedtuples
    # Note the use of generator, to avoid build all in memory
    Row = None
    for line in csv_data.splitlines():
        if Row:
            yield Row._make(line.split(u','))
        else:
            header = line.split(u',')
            Row = collections.namedtuple("Row", [x.replace(u' ', u'') for x in header])


printExplain("Importing 1000 records...")
cur = conn.cursor()
cur.executemany(SQL_INSERT, readCsv(PERSONS))
print ("Done!")

printExplain("Using LIKE is not enough")
print ("""
Is possible to perform queries with the LIKE keyword. However, the user interface
regulary is complicated with several boxes that restrict the fields/tables to search,
and is probably necesary to concatenate the fields to search and the query probably will
perform worse with LIKE than with direct comparision keywords like =, <, >.

For example, to search name & city that could start with 'Ad', like in a auto-complete box
"""
)

printExplain("Regular LIKE search")

SEARCH_LIKE = """
SELECT FullName, City FROM Persons WHERE FullName LIKE  ?  OR City LIKE  ?  
ORDER BY FullName
"""

print (SEARCH_LIKE)

#using a hellish sequence of motherfracking escape sequences, we end up with the following ugly looking line:\


for row in selectSql(SEARCH_LIKE, ['%Ad%%', '%Ad%%']):
    print (row)

conn.commit()      

printTitle("Installing the FTS support")

printExplain("Sql server has FTS enabled by default")

print (" - just need to create the text catalogs on the DB")

printExplain(" also need to create the text index on the particular table and column")

# SQL_FTS = """
# CREATE VIRTUAL TABLE Persons_index USING fts4(personId INT, content);
# """

# SQL_FTS = """
# --USE PYTHONDB
# CREATE FULLTEXT CATALOG PERSfts WITH ACCENT_SENSITIVITY = OFF

# CREATE FULLTEXT INDEX ON PERSONS (FULLNAME, CITY, COUNTRY)
# KEY INDEX Persons_index_Id
# ON PERSfts
# WITH STOPLIST = SYSTEM 

# """


# SQL_FTS = """

# EXEC fulltext_imp

# """

# exeSql(SQL_FTS)


#print (SQL_FTS)

#printExplain("You need at least 1 field to store the data, and put any other field you need for JOINS")

#printExplain("You need to populate the virtual table with INSERTS from the table(s) that are part of the index")

#print ("Inserting the data...")

# SQL_POPULATEINDEX = """
# INSERT INTO Persons_index (personId, content)
# SELECT Id, FullName || ' ' || City || ' ' || Country || ' ' || Street
#     FROM Persons
# """

# printExplain("Note how I concatenate the fields with a space")

# print (SQL_POPULATEINDEX)
# exeSql(SQL_POPULATEINDEX)
# # print "Done.."

printExplain("To have the index up-to-date, use triggers")

printTitle("Searching with FTS")
printExplain("Search is very easy, instead of LIKE, use CONTAINS and FREETEXT ")

SEARCH_FTS = """
SELECT * FROM Persons
WHERE CONTAINS(*, ? )
ORDER BY FullName
"""

# SEARCH_FTS = """
# SELECT FullName, City FROM Persons WHERE Per_Id IN (
#   SELECT personId FROM Persons_index WHERE content MATCH ?

# )
# ORDER BY FullName
# """



#print (SEARCH_FTS)
printSubTitle("Search results:")
# Because I add more fields to this, the results are different
#for row in selectSql(SEARCH_FTS, dict(Content='Ad*')):
for arg in sys.argv:
    arg = '"'+ arg + '*"'
    for row in selectSql(SEARCH_FTS, arg ):
        print (row)
        print ('that should be a row') 



printExplain("Using FTS, is possible to do faster queries for things that are slow with LIKE")
# print "For example, looking for a string in any position '*arden*'"

printSubTitle("Search results:")
# Note: Is case-insensitive!
for row in selectSql(SEARCH_FTS, 'arden'):
    print (row)

# print ("And for a phrase like 'Dillan King' in ANY part of the content")


# printSubTitle("Search results:")
# # Note: Is enclosed in ""
# for row in selectSql(SEARCH_FTS, dict(Content='"Dillan King"')):
#     print (row)

printSubTitle("SET operations")
printExplain("You can use OR, NOT like in a web search engine!")


printSubTitle("Search results AND:")
# Just separate the words with a space
for row in selectSql(SEARCH_FTS, '"King* Neva*"'):
    print (row)

printSubTitle("Search results OR:")
for row in selectSql(SEARCH_FTS, '"Neva"" OR "King"'):
    print (row)

printSubTitle("Search results NOT:")
# Use the unary marked '-'
for row in selectSql(SEARCH_FTS, '"King" -"Neva"'):
    print (row)

printTitle("Conclusion")
# print """
# Sqlite + FTS is a easy way to add rich search capabilities to
# any app (web, mobile, desktop).

# Beacuse is already integrate in the database itself, you not need a separate
# server/library and different API, also, is more easy to mantain the index
# up to date because the data is already in the database, and you can
# mix & match regular SQL queries and FTS queries.

# FTS is particulary usefull for end-users, because the experience is similar to
# use a search engine like google.

# Plus, FTS perform well for cases where the regular queries will need a full scan
# to find the data.

# Take in account the index is inside the database, and it increase the size of it.
# """
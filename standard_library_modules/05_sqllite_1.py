# Python Database
# ref : https://wiki.python.org/moin/DatabaseInterfaces
# Adobe, Apple, Mozilla/Firefox, Google, Symbian, Sun
# Linux>Gnome Banshee

# https://www.sqlite.org/index.html
# http://sqlitebrowser.org/

# About SQLite
# Executive Summary
#
#     Full-featured SQL
#     Billions and billions of deployments
#     Single-file database
#     Public domain source code
#     All source code in one file (sqlite3.c)
#     Small footprint
#     Max DB size: 140 terabytes (247 bytes)
#     Max row size: 1 gigabyte
#     Faster than direct file I/O
#     Aviation-grade quality and testing
#     Zero-configuration
#     ACID transactions, even after power loss
#     Stable, enduring file format
#     Extensive, detailed documentation
#     Long-term support
#
# SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. The code for SQLite is in the public domain and is thus free for use for any purpose, commercial or private. SQLite is the most widely deployed database in the world with more applications than we can count, including several high-profile projects.
# SQLite is an embedded SQL database engine. Unlike most other SQL databases, SQLite does not have a separate server process. SQLite reads and writes directly to ordinary disk files. A complete SQL database with multiple tables, indices, triggers, and views, is contained in a single disk file. The database file format is cross-platform - you can freely copy a database between 32-bit and 64-bit systems or between big-endian and little-endian architectures. These features make SQLite a popular choice as an Application File Format. SQLite database files are a recommended storage format by the US Library of Congress. Think of SQLite not as a replacement for Oracle but as a replacement for fopen()
# SQLite is a compact library. With all features enabled, the library size can be less than 600KiB, depending on the target platform and compiler optimization settings. (64-bit code is larger. And some compiler optimizations such as aggressive function inlining and loop unrolling can cause the object code to be much larger.) There is a tradeoff between memory usage and speed. SQLite generally runs faster the more memory you give it. Nevertheless, performance is usually quite good even in low-memory environments. Depending on how it is used, SQLite can be faster than direct filesystem I/O.
# SQLite is very carefully tested prior to every release and has a reputation for being very reliable. Most of the SQLite source code is devoted purely to testing and verification. An automated test suite runs millions and millions of test cases involving hundreds of millions of individual SQL statements and achieves 100% branch test coverage. SQLite responds gracefully to memory allocation failures and disk I/O errors. Transactions are ACID even if interrupted by system crashes or power failures. All of this is verified by the automated tests using special test harnesses which simulate system failures. Of course, even with all this testing, there are still bugs. But unlike some similar projects (especially commercial competitors) SQLite is open and honest about all bugs and provides bugs lists and minute-by-minute chronologies of code changes.
# The SQLite code base is supported by an international team of developers who work on SQLite full-time. The developers continue to expand the capabilities of SQLite and enhance its reliability and performance while maintaining backwards compatibility with the published interface spec, SQL syntax, and database file format. The source code is absolutely free to anybody who wants it, but professional support is also available.
# The SQLite project was started on 2000-05-09. The future is always hard to predict, but the intent of the developers is to support SQLite through the year 2050. Design decisions are made with that objective in mind.
# We the developers hope that you find SQLite useful and we entreat you to use it well: to make good and beautiful products that are fast, reliable, and simple to use. Seek forgiveness for yourself as you forgive others. And just as you have received SQLite for free, so also freely give, paying the debt forward.


# Create Database
import sqlite3

# filebase Database
newdb = sqlite3.connect("./data/newdb.sqllite")

# temorary database in memory
tempdb_mem = sqlite3.connect(":memory:")

# temporary database in file
tempdb_file = sqlite3.connect("")

# Connect the database
print("Connect the database")
db = sqlite3.connect("./data/kitaplar.sqlite")
print("Database Method List")
print(dir(db))
print("-" * 30)

print("Cursor Method List")
cur = db.cursor()
print(dir(cur))

# Create Table
create_sql = "CREATE TABLE IF NOT EXISTS personel(isim, soyisim, memleket, eposta)"
cur.execute(create_sql)

# insert (add records to table
insert_sql = "INSERT INTO personel VALUES ('Ahmet', 'Paralı', 'Adana', 'ahmetkayali@adana.com')"
cur.execute(insert_sql)

# database commit
db.commit()

# close the database
db.close()
print("-" * 30)
print()
##############
# auto close connection
with sqlite3.connect("./data/kitaplar.sqlite") as db:
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS personel (isim, soyisim, memleket, eposta)""")

    lst = [('Hasan', 'Köz', 'Kayseri'),
           ('Hüseyin', 'Söz', 'Trabzon'),
           ('Veli', 'Göz', 'Ankara'),
           ('Mehmet', 'Paralı', 'İstanbul')]
    for data in lst:
        cur.execute("""INSERT INTO personel(isim, soyisim, memleket) 
                    VALUES (?, ?, ?)""", data)

    db.commit()
#############################
print("-" * 30)
print()
# select table
print("SELECT TABLE")

import os

db_name = "./data/kitaplar.sqlite"
file_exists = os.path.exists(db_name)

db = sqlite3.connect(db_name)
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS faturalar
    (fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi)""")
# if not file_exists:
cur.execute("""INSERT INTO faturalar VALUES
    ("Elektrik", 45, "23 Ocak 2010", "30 Ocak 2010")""")

db.commit()
print("-" * 30)
print()
##############################
# fetcall() Method
print("> fetcall() Method")
cur.execute("SELECT * FROM faturalar")
all_data = cur.fetchall()
print(all_data)
print("-" * 30)
print()
##########################################
# all table list
print("> all table list")
cur.execute("SELECT name FROM sqlite_master")
print(cur.fetchall())
print("-" * 30)
print()
##############################
# fetchone() Method
print("> fetchone() Method")
db2 = sqlite3.connect("./data/kitaplar.sqlite")
cur = db.cursor()
cur.execute("SELECT * FROM kitaplar")
print(cur.fetchone())
print("-" * 30)
print()
##############################
# fetchmany() Method
print("> fetchmany() Method")
print("5 records")
print(cur.fetchmany(5))
print(*cur)
print("-" * 30)
print()
##############################
# data filtering

# select table columns
cur.execute("SELECT sql FROM sqlite_master WHERE name = 'kitaplar' ")
print(*cur)
# ('CREATE TABLE "kitaplar" (\n\t`KitapAdi`\tTEXT,\n\t`Yazar`\tTEXT,\n\t`Fiyati`\tTEXT\n)',)

print()
print("kitaplar where")
cur.execute("""SELECT * FROM kitaplar 
    WHERE KitapAdi = 'ADOBE AİR'""")

# print(*cur)
# or
for i in cur:
    print(i)

print("-" * 30)
print()
###########################################333
# database security
print("database security")
cur.execute("""CREATE TABLE IF NOT EXISTS kullanicilar
    (kullanici_adi, parola)""")
users = [("ahmet123", "12345678"),
         ("mehmet321", "87654321"),
         ("selin456", "123123123")]

for i in users:
    cur.execute("""INSERT INTO kullanicilar VALUES %s""" % (i,))

db.commit()

username = "ahmet123"
password = "12345678"
cur.execute("""SELECT * FROM kullanicilar WHERE
kullanici_adi = '%s' AND parola = '%s'""" % (username, password))

data = cur.fetchone()
if data:
    print("username and password input are correct")
else:
    print("username and password incorrect")
##################################################################
# SQL injection
# x' OR '1' = '1
# bad way
cur.execute("""SELECT * FROM kullanicilar WHERE
kullanici_adi = '%s' AND parola = '%s'""" % (username, password))

username = "x' OR '1' = '1"
password = "x' OR '1' = '1"

"""SELECT * FROM kullanicilar WHERE 
kullanici_adi = 'x' OR '1' = '1' 
AND parola = 'x' OR '1' = '1'"""

######
# good
cur.execute("""SELECT * FROM kullanicilar WHERE
kullanici_adi = ? AND parola = ? """, (username, password))

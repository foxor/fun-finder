#!/usr/bin/env python

from fun_finder_pb2 import *
from password import password

import MySQLdb


num_params = 31

def seed_db():
  conn = MySQLdb.connect(host = "localhost", user = "root", passwd = password, db = "spacecow")
  cursor = conn.cursor()
  seed = FunGuessServer()
  for funProperty in [0x7FFFFFFF for x in xrange(num_params)]:
    seed.baseline.append(funProperty)
  cursor.execute("DROP TABLE IF EXISTS guesses");
  cursor.execute("""
    CREATE TABLE guesses (
      id int NOT NULL AUTO_INCREMENT,
      guess varbinary(1024),
      PRIMARY KEY(id)
    )
  """);
  cursor.execute("DROP TABLE IF EXISTS ratings");
  cursor.execute("""
    CREATE TABLE ratings (
      id int NOT NULL AUTO_INCREMENT,
      rating varbinary(1024),
      PRIMARY KEY(id)
    )
  """);
  cursor.execute("INSERT INTO guesses (guess) VALUES ('%s')" % seed.SerializeToString());
  cursor.close()
  conn.commit()
  conn.close()

def test_seed():
  conn = MySQLdb.connect(host = "localhost", user = "root", passwd = password, db = "spacecow")
  cursor = conn.cursor()
  fgs = FunGuessServer()
  cursor.execute("SELECT * FROM guesses ORDER BY id DESC LIMIT 1")
  fgs.ParseFromString(str(cursor.fetchone()[1]))
  cursor.close()
  conn.close()

def etl():
  conn = MySQLdb.connect(host = "localhost", user = "root", passwd = password, db = "spacecow")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM ratings");
  for row in cursor.fetchall():
    print row
  cursor.close()
  conn.commit()
  conn.close()

if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1 and sys.argv[1] == "test":
    seed_db()
    test_seed()
  else:
    etl()

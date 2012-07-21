#!/usr/bin/env python

from fun_finder_pb2 import *
from flask import Flask, request
from password import password

import math
import MySQLdb
import random
import uuid

con = MySQLdb.connect (host = "localhost", user = "root", passwd = password, db = "spacecow", use_unicode=True, charset='utf8')
cursor = con.cursor()
app = Flask(__name__)

def fetch_fun_guess():
  cursor.execute("SELECT * FROM guesses ORDER BY id DESC LIMIT 1")
  fgs = FunGuessServer()
  fgs.ParseFromString(str(cursor.fetchone()[1]))
  return fgs

@app.route("/")
def accept_score():
  fm = FunMessage()
  fm.gameId = "hello"
  fm.funScore = 200
  string = fm.SerializeToString()
  fm2 = FunMessage()
  fm2.ParseFromString(string)
  return string

@app.route("/gameInit")
def game_init():
  def conductClientExperiment(serverExperiment):
    clientExperiment = FunExperimentClient()
    clientExperiment.index = serverExperiment.index
    clientExperiment.newProperty.value = math.max(0, math.min(0xFFFFFFFF, math.round(random.gauss(serverExperiment.default.value, serverExperiment.deviation))))
    return clientExperiment
  cur_fun_guess = fetch_fun_guess()
  gim = GameInitMessage()
  gim.initialConfig.baseline.extend(cur_fun_guess.baseline)
  gim.initialConfig.changes.extend(conductClientExperiment(x) for x in cur_fun_guess.changes)
  gim.gameId = str(uuid.uuid4())
  return gim.SerializeToString()

@app.route("/gameFinish", methods=["GET", "POST"])
def game_finish():
  #TODO de-duplication
  # at scale, this will be: just record fun message and return, then an etl de-dups
  cursor.execute("INSERT INTO ratings (rating) VALUES ('%s')" % request.form["rating"])
  con.commit()
  return ""

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

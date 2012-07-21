#!/usr/bin/env python

from fun_finder_pb2 import *

import math
import urllib

def propertyWrapper(gim):
  mapping = dict((x.index, x.funProperty) for x in gim.initialConfig.changes)
  index = 0
  for fp in gim.initialConfig.baseline:
    yield (mapping.get(index, fp), index in mapping)
    index += 1

class client(object):

  def client(self):
    self.gameId = ""
    self.values = []
    self.changed = []

  def start(self):
    con = urllib.urlopen("http://localhost:5000/gameInit")
    gim = GameInitMessage()
    gim.ParseFromString(con.read())
    self.values, self.changed = zip(*propertyWrapper(gim))
    self.gim = gim

  def rate(self):
    score = 0
    for i in xrange(len(self.values)):
      score += 10000 - min(10000, abs((1 << i) - self.values[i]))
    return score

  def end(self):
    fm = FunMessage()
    fm.gameId = self.gim.gameId
    fm.config.ParseFromString(self.gim.initialConfig.SerializeToString())
    fm.funScore.append(self.rate())
    con = urllib.urlopen("http://localhost:5000/gameFinish", urllib.urlencode({"rating": fm.SerializeToString()}))
    con.read()

if __name__ == '__main__':
  #import pdb;pdb.set_trace()
  c = client()
  c.start()
  c.end()

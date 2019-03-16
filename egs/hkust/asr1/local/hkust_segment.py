#!/usr/bin/env python
#coding:utf-8

from __future__ import print_function
import sys
import jieba

for line in sys.stdin:
  blks = str.split(line)
  out_line = blks[0]
  for i in range(1, len(blks)):
    if blks[i] in ["[VOCALIZED-NOISE]", "[NOISE]", "[LAUGHTER]"]:
      out_line += " " + blks[i]
      continue
    out_line += ' ' + " ".join(jieba.cut(blks[i]))
  print(out_line)

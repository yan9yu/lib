#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../")

from comlib import algo
from comlib import date
from comlib import util


if __name__ == "__main__":
    # unittest.main()

    # algo.py
    s = 'This is a test string for testing'
    hash1 = algo.simhash(s.split())
    s = 'This is a test string for testing also'
    hash2 = algo.simhash(s.split())
    s = 'nai nai ge xiong cao'
    hash3 = algo.simhash(s.split())

    print(hash1.hamming_distance(hash2), "   ", hash1.similarity(hash2))
    print(hash1.hamming_distance(hash3), "   ", hash1.similarity(hash3))

    # api.py

    # cache.py

    # conv.py

    # date.py
    print date.getHourList(1, 23)
    print date.getDateList("20140101", "20140110")
    print date.getAfterXDay(3, start="20140101")

    # decorator.py


    # file.py

    # hash.py

    # net.py

    # prof.py

    # rand.py

    # reg.py

    # scp.py

    # sort.py

    # sql.py

    # thread.py

    # util.py
    util.import_test()

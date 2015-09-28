#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

sys.path.append("../")

import date

if __name__ == "__main__":
    # unittest.main()

    # algo.py
    s = 'This is a test string for testing'
    # hash1 = algo.simhash(s.split())
    # s = 'This is a test string for testing also'
    # hash2 = algo.simhash(s.split())
    # s = 'nai nai ge xiong cao'
    # hash3 = algo.simhash(s.split())
    #
    # print(hash1.hamming_distance(hash2), "   ", hash1.similarity(hash2))
    # print(hash1.hamming_distance(hash3), "   ", hash1.similarity(hash3))

    # api.py

    # cache.py

    # conv.py

    # date.py
    # print date._convert("20150101")
    # print date._convert("150201", with_hour=True)
    # print date._convert("20150102325687", with_hour=True)
    # print date.day_list("150101", "2015-01-20")
    # print date.day_pair_list("20150102", "2015-01-20")
    # x = date.convert_to_datetime("20150101", delimiter="")
    # print x, type(x)
    # print date.day_delta("150101", "2015-02-01")
    # # decorator.py
    print date.day_list("20150101", "20150301")
    print date.tomorrow()
    print date.yesterday()
    print date.now()
    print date.hour_list("150101")
    print date.hour_delta("150101010203", "20150102020304")

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

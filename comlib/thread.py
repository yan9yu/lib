#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
thread module provide thread-relevant functions


Required Library
    - multiprocessing


TODO:
    -



"""


from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool


def multiProcess(func, args, size=None):
    """
    Multi-processing using map, adapted for CPU-Intensive process
        Input:
               func: function name
               args: list of data that will be processed by func. Each item can be either one variable or a tuple(var_a, var_b, var_c)
               size: Thread Pool size
        Output:
    """

    if not isinstance(args, list):
        print "[THREAD] ERROR: Invalid data list"
    if size <= 0 or size == None:
        print "[THREAD] WARNING: Invalid Process Pool size! Use the default value: size=5"
        size = 5

    try:
        pool = ProcessPool(size)
        results = pool.map(func, args)
        pool.close()
        pool.join()
    except Exception, e:
        print e.message


def multiThread(func, args, size=None):
    """
    Multi-threading using map, adapted for IO-Intensive process
        Input:
               func: function name
               args: list of data that will be processed by func. Each item can be either one variable or a tuple(var_a, var_b, var_c)
               size: Thread Pool size
        Output:
    """

    if not isinstance(args, list):
        print "[THREAD] ERROR: Invalid data list!"
    if size <= 0 or size == None:
        print "[THREAD] WARNING: Invalid Thread Pool size! Use the default value: size=5"
        size = 5
    try:
        pool = ThreadPool(size)
        results = pool.map(func, args)
        pool.close()
        pool.join()
        return results
    except Exception, e:
        print e.message

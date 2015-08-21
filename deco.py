#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Decorator Module provides several decorator


Required Library:
    - sys
    - time
    - functools


TODO:
    - 
    



"""

import sys
import time
import functools
import logging

try:
    from line_profiler import LineProfiler
except Exception, e:
    print "[ERROR] line_profiler: %s" % (e.message)


def timeUsage(func):
    """
    Time decorator. calculate function time usage.
    """

    @functools.wraps(func)
    def _time():
        start = time.clock()
        func()
        end = time.clock()
        print "%s() time usage: %ss" % (func.__name__, end - start)

    return _time


def log(func):
    """
    Log decorator.
    """

    @functools.wraps(func)
    def _log():
        logging.basicConfig(filename='../log/debug.log', level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(module)s %(message)s')
        func(*args, **kwargs)

    return _log


def cache(func):
    """
    Cache decorator. cache computed results for further usage
    """
    caches = {}

    @wraps(func)
    def wrap(*args):
        if args not in caches:
            caches[args] = func(*args)
        return caches[args]

    return wrap


def funcCompleted2(func):
    """
    Completed decorator. print func complete message + time usage message
    """

    def _completed():
        start = time.time()
        func()
        end = time.time()
        usage = end - start
        start = time.strftime("%Y%m%d %H:%M:%S", time.localtime(start))
        end = time.strftime("%Y%m%d %H:%M:%S", time.localtime(end))

        print "\n%s %s() completed! %s\nstarts at:\t%s\nends at:\t%s\ntime usage:\t%.3f s " % (
            "=" * 29, func.__name__, "=" * 29, start, end, usage)

    return _completed


def funcCompleted(funcName):
    """
    Completed decorator. print func complete message + time usage message
    """

    def _funcCompleted(func):
        def __funcCompleted(*args, **kwargs):
            start = time.time()
            print "%s %s start! %s" % ("-" * 29, funcName, "-" * 29)
            func(*args, **kwargs)
            end = time.time()
            usage = end - start
            start = time.strftime("%Y%m%d %H:%M:%S", time.localtime(start))
            end = time.strftime("%Y%m%d %H:%M:%S", time.localtime(end))

            print "\n%s %s completed! %s\nstarts at:\t%s\nends at:\t%s\ntime usage:\t%.3f s \n" % (
                "=" * 29, funcName, "=" * 29, start, end, usage)

        return __funcCompleted

    return _funcCompleted


def exeTime(func):
    """
    Completed decorator. print func complete message + time usage message
    """

    def newFunc(*args, **args2):
        start = time.time()
        back = func(*args, **args2)
        ss = int(str((time.time() - start)).split(".")[0])
        print time.time() - start, ss, ss
        # 时间长度太长则显示分钟秒, 否则显示毫秒
        if ss > 60:
            print "[Time Usage] %s: %.2fm" % (func.__name__, (time.time() - start) / 60)
        if 0 < ss <= 60:
            print "[Time Usage] %s: %.2fs" % (func.__name__, (time.time() - start))
        if ss <= 0:
            print "[Time Usage] %s: %.2fms" % (func.__name__, (time.time() - start) * 1000)
        return back

    return newFunc


def progressBar(func):
    """
    Progress bar decorator. print a progress bar for func.
    """

    def _progressBar(*args, **kwargs):
        toolbar_width = 77
        sys.stdout.write("|%s|" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width + 1))

        for ii in xrange(toolbar_width):
            ret = func(*args, **kwargs)

            sys.stdout.write("#")
            sys.stdout.flush()

        sys.stdout.write("\n")

        return ret

    return _progressBar

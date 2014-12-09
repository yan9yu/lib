#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Date Module provide date-relevant functions
    - getDateList(start, end=None)
    - getWeekList(start, end=None)
    - getMonthList(start, end=None)


Required Library
    - time
    - datetime

TODO:
    -



"""

import time

from datetime import timedelta
from datetime import datetime


def getDateList(start, end=None):
    """
    Return a date list between start~end. If end is None, then end will be start+1
        Input: start = '20140101', end = '20140105'
        Output: ['20140101','20140102','20140103','20140104']
    """

    start_date_time = datetime.strptime(start, "%Y%m%d")
    if end == None:
        oneday = timedelta(days=1)
        end_date_time = start_date_time + oneday
        end = end_date_time.strftime("%Y%m%d")
        return start, end
    else:
        end_date_time = datetime.strptime(end, "%Y%m%d")
        delta = (end_date_time - start_date_time).days
        # dateList = []
        # for ii in xrange(0, delta + 1):
        # next = timedelta(days=ii)
        # dateList.append((start_date_time + next).strftime("%Y%m%d"))
        # return dateList[:-1]
        return [(start_date_time + timedelta(days=ii)).strftime("%Y%m%d") for ii in xrange(0, delta + 1)][:-1]


def getWeekList(start, end=None):
    """
    Return a week list between start~end. If end is None, then end will be the next week of start
        Input: start = '20140101', end = '20140108'
        Output: ['20140101','20140102','20140103','20140104','20140105','20140106','20140107']
    """
    delta = 7
    if end is None or abs(getDayDelta(start, end)) > delta:
        end = getAfterXDay(delta, start)
    return getDateList(start, end)


def getMonthList(start, end=None):
    """
    Return a month list between start~end. If end is None, then end will be the next month of start
        Input: start = '20140101', end = '20140501'
        Output: ['201401','201402','201403','201404','201405']
    """

    if len(start) == 6:
        start += "20"
    if end == None:
        next_month_first_day = getNextMonthFirstDay(start)
        return start[:-2], next_month_first_day[:-2]
    else:
        if len(end) == 6:
            end += "20"
        dates = getDateList(start, end)
        return sorted(list(set([item[:-2] for item in dates])))


def getDateListByMonth(year_month):
    """
    Return a date list in a month.
        Input: year_month is '201401'
        Output: 
                ['20140101', '20140102', '20140103', '20140104', '20140105', '20140106', '20140107',
                '20140108', '20140109', '20140110', '20140111', '20140112', '20140113', '20140114', '20140115', '20140116', '20140117',
                '20140118', '20140119', '20140120', '20140121', '20140122', '20140123', '20140124', '20140125', '20140126', '20140127',
                '20140128', '20140129', '20140130', '20140131']
    """

    if len(year_month) == 6:
        year = year_month[:4]
        month = year_month[4:]
    elif len(year_month) == 4:
        year = "20" + year_month[:2]
        month = year_month[2:]
    first_day = year + month + "01"
    next_month_first_day = getNextMonthFirstDay(first_day)
    dates = getDateList(first_day, next_month_first_day)
    return dates


def getNextMonthFirstDay(datenow):
    """
    Return the first day of the next month
        Input: datenow = '20140101'
        Output: '20140201'
    """
    year = int(datenow[:4])
    month = int(datenow[4:6])

    next_year = year
    next_month = month + 1
    if month == 12:
        next_year = year + 1
        next_month = 1
    next_month_date = datetime(next_year, next_month, 1)
    return next_month_date.strftime("%Y%m%d")


def getToday():
    """
    Return Today in string
        Input: 
        Output: eg, '20140101'
    """
    return time.strftime("%Y%m%d", time.localtime(time.time()))


def getNow():
    """
    Return Now in string
        Input: 
        Output: eg. '20140101 00:00:00'
    """
    return time.strftime("%Y%m%d %H:%M:%S", time.localtime(time.time()))


def getMonth():
    """
    Return Month in string
        Input: 
        Output: eg. '201401'
    """
    return getToday()[:-2]


def getNowString():
    """
    Return Now in string
        Input: 
        Output: eg. '20140101 00:00:00'
    """
    return time.strftime("%Y%m%d", time.localtime(time.time()))


def getNowDatetime():
    """
    Return Now in datetime
        Input: 
        Output: eg. datetime.datetime(2014, 9, 24, 15, 2, 57, 45000)
    """
    return datetime.now()


def getDateFromDatetime(dat):
    return dat.strftime("%Y%m%d")


def getDetailedDateFromDatetime(dat):
    return dat.strftime("%Y%m%d %H:%M:%S")


def getDayDelta(start, end=None):
    """
    Return time delta between start~end. 
        Input: start = '20140101', end = '20140112'
        Output: delta = 11
    """

    if end is None:
        return 0
    else:
        start = datetime.strptime(start, "%Y%m%d")
        end = datetime.strptime(end, "%Y%m%d")
        delta = end - start
        return delta.days


def getBeforeXDay(delta, start=None):
    """
    Return X day before Today in string
        Input: delta = 1, start = '20140102'
        Output: '20140101'
    """

    if start is None:
        today = datetime.strptime(getToday(), "%Y%m%d")
    else:
        today = datetime.strptime(start, "%Y%m%d")
    x = timedelta(days=delta)
    return (today - x).strftime("%Y%m%d")


def getAfterXDay(delta, start=None):
    """
    Return X day after Today in  string
        Input: delta = 1, start = '20140101'
        Output: '20140102'
    """

    if start is None:
        today = datetime.strptime(getToday(), "%Y%m%d")
    else:
        today = datetime.strptime(start, "%Y%m%d")
    x = timedelta(days=delta)
    return (today + x).strftime("%Y%m%d")

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Date Module provide date-relevant functions


Required Library
    - time
    - datetime
"""

import time
import calendar
from datetime import datetime
from datetime import timedelta

day_format = "%Y-%m-%d"
day_format_full = "%Y-%m-%d %H:%M:%S"


def now():
    return time.strftime(day_format_full, time.localtime(time.time()))


def today():
    return time.strftime(day_format, time.localtime(time.time()))


def tomorrow():
    return after_xday(today(), 1)


def yesterday():
    return before_xday(today(), 1)


def _convert(string, delimiter="-", with_hour=False):
    """ Convert partial date string to full date string

    e.g.
        150101   -> 2015-01-01 00:00:00
        20150101 -> 2015-01-01 00:00:00
        20150101000000 -> 2015-01-01 00:00:00
    """

    new_string = ""
    if with_hour:
        if len(string) is 6:
            string = "20" + string
        if len(string) is 8:
            new_string = "%s%s%s%s%s 00:00:00" % (string[0:4], delimiter, string[4:6], delimiter, string[6:8])
        if len(string) is 10:
            new_string = "%s%s%s%s%s 00:00:00" % (string[0:4], delimiter, string[5:7], delimiter, string[8:10])
        if len(string) is 12:
            string = "20" + string
        if len(string) is 14:
            new_string = "%s%s%s%s%s %s:%s:%s" % (
                string[0:4], delimiter, string[4:6], delimiter, string[6:8], string[8:10], string[10:12], string[12:14])
    else:
        if len(string) is 6:
            string = "20" + string
        if len(string) is 8:
            new_string = "%s%s%s%s%s" % (string[0:4], delimiter, string[4:6], delimiter, string[6:8])
        if len(string) is 10:
            new_string = "%s%s%s%s%s" % (string[0:4], delimiter, string[5:7], delimiter, string[8:10])
        if len(string) is 14:
            new_string = "%s%s%s%s%s" % (string[0:4], delimiter, string[4:6], delimiter, string[6:8])
    return new_string


def convert_to_datetime(string, with_hour=False):
    string = _convert(string, with_hour=with_hour)
    if with_hour:
        formats = day_format_full
    else:
        formats = day_format
    return datetime.strptime(string, formats)


def convert_to_string(dt, with_hour=False):
    if with_hour:
        formats = day_format_full
    else:
        formats = day_format
    return dt.strftime(formats)


def hour_list(date):
    hours = []
    for hour in xrange(0, 25):
        dd = convert_to_datetime(date, with_hour=True)
        delta = timedelta(hours=hour)
        dd = (dd + delta).strftime("%Y-%m-%d %H:%M:%S")
        hours.append(dd)

    return hours


def day_list(start, end=None):
    """ Return a day list between start and end. If end is None, end will be start+1


    """
    start = _convert(start, with_hour=False)
    start_datetime = convert_to_datetime(start)
    if end is None:
        one = timedelta(days=1)
        end = convert_to_string(start_datetime + one)
        return start, end

    else:
        end = _convert(end, with_hour=False)
        end_datetime = convert_to_datetime(end)
        delta = (end_datetime - start_datetime).days
        return [convert_to_string(start_datetime + timedelta(days=ii)) for ii in xrange(0, delta + 1)]


def day_pair_list(start, end=None):
    """ Return a day list with paired date. If end is None, end will be start+1

    """
    days = day_list(start, end)
    pairs = []
    for ii in xrange(0, len(days) - 1):
        first = days[ii]
        second = days[ii + 1]
        pairs.append((first, second))

    return pairs


def week_list(start, end=None):
    """

    """
    delta = 6
    if end is None or abs(day_delta(start, end)) > delta:
        end = after_xday(start, delta)

    return day_list(start, end)


def day_delta(start, end=None):
    """ Return day delta between two date

    """

    if end is None:
        return 0
    else:
        start = convert_to_datetime(start)
        end = convert_to_datetime(end)
        delta = end - start
        return delta.days


def hour_delta(start, end=None):
    """

    """
    if end is None:
        return 0
    else:
        start = convert_to_datetime(start, with_hour=True)
        end = convert_to_datetime(end, with_hour=True)
        delta = end - start

        return delta.days * 24 + delta.seconds // 3600


def before_xday(start, delta):
    """

    """
    start = convert_to_datetime(start)
    x = timedelta(days=delta)
    return convert_to_string(start - x)


def after_xday(start, delta):
    """

    """
    start = convert_to_datetime(start)
    x = timedelta(days=delta)
    return convert_to_string(start + x)

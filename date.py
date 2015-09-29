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
    """ Return Now string with date and hour

    Parameters
    ----------


    Returns
    -------

    out: string
        now string

    """
    return time.strftime(day_format_full, time.localtime(time.time()))


def today():
    """ Return today string

    Parameters
    ----------


    Returns
    -------

    out: string
        today string

    """
    return time.strftime(day_format, time.localtime(time.time()))


def tomorrow():
    """ Return Tomorrow string

    Parameters
    ----------


    Returns
    -------

    out: string
        tomorrow string


    """
    return after_xday(today(), 1)


def yesterday():
    """ Return Yesterday string

    Parameters
    ----------


    Returns
    -------

    out: string
        yesterday string


    """
    return before_xday(today(), 1)


def _convert(string, with_hour=False):
    """ Convert partial date string to full date string

    Parameters
    ----------
    string: String
        partial date string

    with_hour: Bool
        full date or just date


    Returns
    -------

    out: String
        full date in string


    Examples
    --------

    >> print _convert("150101", with_hour=False)
    >> "2015-01-01"
    >>
    >> print _convert("20150101", with_hour=True)
    >> "2015-01-01 00:00:00"
    >>
    >> print _convert("150101")
    >> "2015-01-01 00:00:00"
    >>
    >> print _convert("20150101000000", with_hour=True)
    >> "2015-01-01 00:00:00"
    """

    out = ""
    if with_hour:
        if len(string) is 6:
            string = "20" + string
        if len(string) is 8:
            out = "%s-%s-%s 00:00:00" % (string[0:4], string[4:6], string[6:8])
        if len(string) is 10:
            out = "%s-%s-%s 00:00:00" % (string[0:4], string[5:7], string[8:10])
        if len(out) is 12:
            string = "20" + string
        if len(string) is 14:
            out = "%s-%s-%s %s:%s:%s" % (
            string[0:4], string[4:6], string[6:8], string[8:10], string[10:12], string[12:14])
    else:
        if len(string) is 6:
            string = "20" + string
        if len(string) is 8:
            out = "%s-%s-%s" % (string[0:4], string[4:6], string[6:8])
        if len(string) is 10:
            out = "%s-%s-%s" % (string[0:4], string[5:7], string[8:10])
        if len(string) is 14:
            out = "%s-%s-%s" % (string[0:4], string[4:6], string[6:8])
    return out


def convert_to_datetime(string, with_hour=False):
    """ Convert String to Datetime

    Parameters
    ----------

    string: String
        partial date string

    Returns
    -------

    out: Datetime
        partial datetime or full datetime


    Examples
    --------

    >> print convert_to_datetime("150101")
    >> "2015-01-01 00:00:00"
    >>
    >> print convert_to_datetime("20150101")
    >> "2015-01-01 00:00:00"
    >>
    >> print convert_to_datetime("20150101010203")
    >> "2015-01-01 01:02:03"

    """
    string = _convert(string, with_hour=with_hour)
    if with_hour:
        formats = day_format_full
    else:
        formats = day_format
    return datetime.strptime(string, formats)


def convert_to_string(dt, with_hour=False):
    """ Convert Datetime to string

    Parameters
    ----------

    Returns
    -------

    Examples
    --------



    """
    if with_hour:
        formats = day_format_full
    else:
        formats = day_format
    return dt.strftime(formats)


def hour_list(date):
    """ Return hours of a day

    """
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
    """ Return a day list in a week

    """
    delta = 6
    if end is None or abs(day_delta(start, end)) > delta:
        end = after_xday(start, delta)

    return day_list(start, end)


def hour_delta(start, end=None):
    """ Return hour delta between two date

    """
    if end is None:
        return 0
    else:
        start = convert_to_datetime(start, with_hour=True)
        end = convert_to_datetime(end, with_hour=True)
        delta = end - start

        return delta.days * 24 + delta.seconds // 3600


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


def before_xday(dat, delta):
    """ Return a date before x day of the given day

    """
    dat = convert_to_datetime(dat)
    x = timedelta(days=delta)
    return convert_to_string(dat - x)


def after_xday(dat, delta):
    """ Return a date after x day of the given day

    """
    dat = convert_to_datetime(dat)
    x = timedelta(days=delta)
    return convert_to_string(dat + x)

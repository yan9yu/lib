#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
sort Module provide order-relevant functions


Required Library
    - collections
    - random

TODO:
    -



"""


def getSortedDictBykey(d, increasing=False):
    """
    Sort a dict in decreasing order.
        Input:
        Output:
    @note: this function might have sideeffects
    """

    d = [(k, d[k]) for k in d]
    d.sort()
    if not increasing:
        d.reverse()
    return d


def getSortedDictByValue(d, increasing=False, top=None):
    """
    Sort a dict in decreasing order.
    @note: this function might have sideeffects
    """

    d = [(d[k], k) for k in d]
    d.sort()
    if not increasing:
        d.reverse()
    if top is None:
        return d
    else:
        dd = {}
        for item in d[:top]:
            dd[item[1]] = item[0]
        return dd


def getThresholdDict(dict, min):
    """
    Remove from dict all keys less than this value, and return it.
    @note: this function might have sideeffects
    """

    keys = dict.keys()
    for k in keys:
        if dict[k] < min:
            del dict[k]
    return dict


def getReversedDict(d):
    """
    Reverse a {Key:Value} dict to {Value:Key} dict
    """
    return dict(zip(d.values(), d.keys()))


def sumDictValue(d):
    return sum([int(d[item]) for item in d])


def getDictMaxValue(d):
    return getSortedDictByValue(d)[0][1]


def getDictMinValue(d):
    return getSortedDictByValue(d, increasing=True)[0][1]


def getCommonElement(lst, n=1):
    """
    Return the most top n elements and times in a list
    """

    from collections import Counter

    if isinstance(lst, list):
        return Counter(lst).most_common(n)
    else:
        return []


def getSortedList(lst, increasing=False):
    return lst.sort(reverse=increasing)


def getReversedList(lst):
    """
    Return a reversed list. For example: getReversedList([1,2,3]) = [3,2,1]
    """
    return list(reversed(lst))


def getFlattenList(lst):
    """
    Return a flatten list. For example: getReversedList([1, [2], [3, [4, 5] ] ]) = [1, 2, 3, 4, 5]
    """
    return [y for l in lst for y in getFlattenList(l)] if type(lst) is list else [lst]


def getShuffledList(lst):
    """
        Return a shuffled list
    """
    import random

    return random.shuffle(lst)

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Conv Module provides several methods for different type of variables convert

Required Library
    - os
    - sys
    - math
    - itertools

TODO:
    -



"""

import os
import sys



def convertBytes(fileSize):
    """
    Convert file length to readable numbers.
    """
    import math
    if fileSize == 0:
        return "0 Bytes"
    sizename = [" Bytes", " KB", " MB", " GB", " TB", " PB", " EB", " ZB", " YB"]
    k = int(math.floor(math.log(fileSize, 1024)))
    return "%.2f%s" % (round(fileSize / math.pow(1024, k), 2), sizename[k])


def convertSeconds(seconds):
    """
    Convert seconds to readable numbers
    """
    pass


def lst2Str(list, sep):
    result = ""
    for item in list:
        result += str(item) + sep
    return result[:-1]


def str2Lst(str, sep):
    sep = "%s" % (sep)
    return str.split(sep)


def lists2Dict(keyList, valueList):
    return dict(zip(keyList, valueList))


def json2Str():
    pass


def str2Json():
    pass


def matrix2List(matrix):
    import itertools
    return list(itertools.chain.from_iterable(matrix))


def list2Matrix(lst, m, n):
    pass



def list2Dict(lst, dft):
    d = {}
    for item in lst:
        item = str(item).strip()
        if item not in d:
            d[item] = dft
        d[item] += dft
    return d



def group(n, sep=','):
    s = str(abs(n))[::-1]
    groups = []
    i = 0
    while i < len(s):
        groups.append(s[i:i + 3])
        i += 3
    retval = sep.join(groups)[::-1]
    if n < 0:
        return '-%s' % retval
    else:
        return retval




base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


def bin2dec(string_num):
    """
        二进制 to 十进制: int(str,n=10)
    """
    return str(int(string_num, 2))


def hex2dec(string_num):
    """
        十六进制 to 十进制
    """
    return str(int(string_num.upper(), 16))


def dec2bin(string_num):
    """
        十进制 to 二进制: bin()
    """
    num = int(string_num)
    mid = []
    while True:
        if num == 0:
            break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


def dec2hex(string_num):
    """
        # 十进制 to 八进制: oct()
        # 十进制 to 十六进制: hex()    
    """
    num = int(string_num)
    mid = []
    while True:
        if num == 0:
            break
        num, rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


def hex2bin(string_num):
    """
        十六进制 to 二进制: bin(int(str,16))
    """
    return dec2bin(hex2dec(string_num.upper()))


def bin2hex(string_num):
    """
        二进制 to 十六进制: hex(int(str,2))
    """
    return dec2hex(bin2dec(string_num))

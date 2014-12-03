#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
hash Module provide hash-relevant functions


Required Library
    - comlib.conv
    - hashlib

TODO:
    -



"""


import hashlib
import conv


def strMD5(str):
    """
    Return MD5 checksum of a string
        Input: string
        Output: MD5 checksum
    """
    return hashlib.md5(str.encode("utf-8")).hexdigest()


def fileMD5(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()

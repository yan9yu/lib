#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Algo Module provides several common algorithms
    - simHash Algorithm


Required Library:
    - itertools


TODO:
    - implement tfidf algorithm



"""

from __future__ import division


class simhash:
    """
    Algorithm based on [Similarity estimation techniques from rounding algorithm](http://dl.acm.org/citation.cfm?id=509965)
        Usage: Detecting duplicated documents
        Input: a doc contains several tokens or long-long string
        Output: a 128-bit hash code of input doc
    """


    # 构造函数
    def __init__(self, tokens='', hashbits=128):
        self.hashbits = hashbits
        self.hash = self.simhash(tokens)

    # toString函数
    def __str__(self):
        return str(self.hash)

    # 生成simhash值
    def simhash(self, tokens):
        v = [0] * self.hashbits
        for t in [self._string_hash(x) for x in tokens]:  # t为token的普通hash值
            for i in range(self.hashbits):
                bitmask = 1 << i
                if t & bitmask:
                    v[i] += 1  # 查看当前bit位是否为1,是的话将该位+1
                else:
                    v[i] -= 1  # 否则的话,该位-1
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        print fingerprint
        return fingerprint  # 整个文档的fingerprint为最终各个位>=0的和

    # 求海明距离
    def hamming_distance(self, other):
        """
        """
        x = (self.hash ^ other.hash) & ((1 << self.hashbits) - 1)
        tot = 0
        while x:
            tot += 1
            x &= x - 1
        return tot

    # 求相似度
    def similarity(self, other):
        """
        """
        a = float(self.hash)
        b = float(other.hash)
        if a > b:
            return b / a
        else:
            return a / b

    # 针对source生成hash值   (一个可变长度版本的Python的内置散列)
    def _string_hash(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** self.hashbits - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            return x


def rmPunctuation(data):
    """
    """
    punctuation = [" ", "，", "。", "【", "】", "《", "》", "：", "；", "（", "）",
                   "、", "！", "？", "．", ",", ".", "+", "-", "*", "/", "|", "#", "!", "&", "?", "—", ":", ";", "\\", "br",
                   "nbsp"]

    for pun in punctuation:
        data = data.replace(pun, "")
    return data


def ngrams(lst, n):
    """
    """
    from itertools import islice

    if n <= 1:
        print "[ALGO] ERROR: Invalid n-grams value! Use default value."
    result = (islice(lst, ii, None) for ii in xrange(n))
    return zip(*result)


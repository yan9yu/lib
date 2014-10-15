#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
API Module provides several external API-wrappers
    - getLocationByIP

Required Library
    - comlib.net
    - simplejson

TODO:
    -



"""

import random

import net
import date

try:
    import simplejson as json
except Exception, e:
    import json


class IPLocation():
    def __init__(self, ip):
        self.ip = ip
        self.api_format = "json"
        self.freegeoip_url = "http://freegeoip.net/%s/%s" % (self.api_format, self.ip)
        self.taobao_url = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % (self.ip)
        self.qq_url = "http://ip.qq.com/cgi-bin/searchip?searchip1=%s" % (self.ip)

        self.results = []

        self.country = None
        self.region = None
        self.city = None

        self.getGeoInfo()
        self.getCountry()
        self.getRegion()
        self.getCity()

    def getGeoInfo(self):
        """
        Get geo information from apis, return a dict about the location
            Input: IP address
            Output: geo info based on ip-services
        """
        urls = [self.freegeoip_url, self.taobao_url, self.qq_url]
        random.seed(date.getNow())
        random.shuffle(urls)

        for url in urls:
            respose = net.getHTMLContent(url)
            if respose:
                resposedict = json.loads(respose, encoding="utf-8")
                if url == self.taobao_url:
                    self.results.append(resposedict["data"])
                else:
                    self.results.append(resposedict)
            break

    def getCountry(self):
        """
        Return country information
            Input: response info
            Output: country info
        """
        for respose in self.results:
            if "country_name" in respose:
                self.country = respose.get("country_name")
            elif u"country" in respose:
                self.country = respose.get(u"country")

        return self.country

    def getRegion(self):
        """
        Return region information
            Input: response info
            Output: region info
        """
        for respose in self.results:
            if "region" in respose:
                self.region = respose.get("region")

        return self.region

    def getCity(self):
        """
        Return city information
            Input: response info
            Output: city info
        """

        for respose in self.results:
            if "city" in respose:
                self.city = respose.get("city")

        return self.city

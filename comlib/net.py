#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Net Module provide net-relevant functions


Required Library
    - smtplib
    - email
    - time
    - random
    - socket
    - requests
    - bs4

TODO:
    -



"""


def sendEmail(subject, content, mailto=None):
    """
    Send email using www.126.com server
    @note: Support HTML content
    """
    import smtplib
    from email.mime.text import MIMEText

    host = "smtp.126.com"
    user = "programalert"
    passwd = "aabbcc123"
    postfix = "126.com"
    mailList = ["programalert@126.com"]

    if mailto is None:
        pass
    elif isinstance(mailList, str):
        mailList.append(mailto)
    elif isinstance(mailList, list):
        mailList.extend(mailto)

    me = user + "<" + user + "@" + postfix + ">"

    msg = MIMEText(content, _subtype="plain", _charset="utf-8")
    msg["Subject"] = subject
    msg["From"] = me
    msg["To"] = ";".join(mailList)

    try:
        server = smtplib.SMTP()
        server.connect(host)
        server.login(user, passwd)
        server.sendmail(me, mailList, msg.as_string())
        server.close()
        print "Email from %s to  %s  send successfully!" % (me, ";".join(mailList))
        return True
    except Exception, e:
        print "[NET] ERROR: %s" % (e.message)
        return False


import time
import random
import socket

try:
    import requests
except:
    print "[NET] ERROR: Can not import Requests package! Please install Requests package by pip install requests."
try:
    import bs4
except:
    print "[NET] ERROR: Can not import bs4 package! Please install Requests package by pip install bs4."


class WebPage():
    def __init__(self, url):
        self.url = url
        self.timeout = 100
        self.html = ""
        self.title = ""
        self.content = ""
        self.soup = None
        self.headers = {'Accept-Encoding': 'identity, deflate, compress, gzip', 'Accept': '*/*', 'User-Agent':
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

    def getHTML(self):
        fail = 0
        while 1:
            if fail >= 5:
                print "[NET] ERROR: Wrong url(%s)" % (self.url)
                break
            try:
                response = requests.get(self.url)
                if response.status_code == 200:
                    self.html = response.content
                else:
                    print "[NET] ERROR: Can not get content(%s)" % (response.status_code)
            except (requests.exceptions.Timeout, Exception), e:
                fail += 1
                time.sleep(random.randint(1, 3))
                print "[NET] ERROR: %s(%s)" % (e.message, self.url)

        return self.html

    def getSoup(self):
        if self.html == "":
            try:
                self.html = self.getHTML()
            except Exception, e:
                print "[NET] ERROR: %s" % (e.message)

        try:
            self.soup = bs4.BeautifulSoup(self.html)
        except Exception, e:
            print "[NET] ERROR: %s" % (e.message)
        return self.soup

    # def getSpecialContentBySoup(self, specTag, specCondition, resTag):
    #     contents = []
    #     if self.soup == None:
    #         try:
    #             self.soup = self.getSoup()
    #         except Exception, e:
    #             print "[NET] ERROR: %s" %(e.message)
    #     else:
    #         try:
    #             for item in self.soup(specTag, specCondition):
    #                 contents.append(item.a)

    def getTitle(self):
        pass

    def getContent(self):
        pass

    def getSpecialContentByReg(self, reg):
        """
            Get specific content using regular expression
        """
        pass


def getHTMLContent(url):
    """
    Ensure get HTML content
    """
    html = ""
    failure = 1
    while 1:
        try:
            if failure >= 3:
                print "Can not get info from: %s" % (url)
                break
            else:
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        html = response.content
                        break
                    else:
                        print "[NET] ERROR: Can not get content from %s(%s)" % (url, response.status_code)
                        time.sleep(3)
                        failure += 1
                except (requests.exceptions.Timeout, Exception), e:
                    print "[NET] ERROR: %s" % (e.message)
                    time.sleep(3)
                    failure += 1

        except Exception, e:
            print e.message
            time.sleep(3)
            failure += 1

    time.sleep(random.randint(1, 5))
    return html


def getHTMLContentSimple(url):
    """
    Try to get HTML content
    """
    html = ""
    response = requests.get(url)
    if response.stats_code == 200:
        html = response.content

    return html


def downloadFile(url, filename):
    """
    Download files
    """
    try:
        r = requests.get(url, stream=True)
        with open(filename, "wb") as fp:
            fp.write(r.content)
    except Exception, e:
        print e

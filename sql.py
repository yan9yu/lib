#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
sql Module provide database-relevant functions


Required Library
    - sys
    - time
    - MySQLdb
    - pymssql


TODO:
    -



"""

import sys
import time
import datetime
from sre_compile import isstring

reload(sys)
sys.setdefaultencoding("utf-8")


class DB:
    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cursor = None
        self.getConn()
        self.query_result = []

    def set(self, config):
        self.config = config
        self.query_result = []

    def getConn(self):

        host = self.config["host"]
        db = self.config["db"]
        type = self.config["type"]
        user = self.config["user"]
        passwd = self.config["passwd"]
        quiet = self.config.get("quiet", "False")

        failure = 1
        while 1:
            try:
                if failure >= 3:
                    print "Failure connect to %s(%s)" % (host, db)
                    break
                else:
                    if type == "MySQL":
                        try:
                            import MySQLdb

                            self.conn = MySQLdb.connect(
                                host=host, db=db, port=3306, user=user, passwd=passwd, use_unicode=False)
                            self.cursor = self.conn.cursor()
                            self.cursor.execute("set names utf8")
                            if quiet == "True":
                                pass
                            else:
                                print "Connect to %s(MySQL: %s) successfully!" % (host, db)
                            break
                        except Exception, e:
                            print "ERROR: cannot connect to %s(MySQL: %s)! %s" % (host, db, e.message)
                            failure += 1
                            time.sleep(3)

                    if type == "MSSQL":
                        try:
                            import pymssql

                            self.conn = pymssql.connect(
                                host=host, database=db, port=1433, user=user, password=passwd, charset="utf8")
                            self.cursor = self.conn.cursor()
                            if quiet == "True":
                                pass
                            else:
                                print "Connect to %s(MSSQL: %s) successfully!" % (host, db)
                            break
                        except Exception, e:
                            print "ERROR: cannot connect to %s(MSSQL: %s)! %s" % (host, db, e.message)
                            failure += 1
                            time.sleep(3)

            except Exception, e:
                print e.message + " and will restart to connect to %s(%s) in 3secs" % (host, db)
                time.sleep(3)
                failure += 1

        return self.conn

    def getCursor(self):

        if self.conn and self.cursor:
            self.cursor = self.conn.cursor()
        else:
            self.cursor = self.getConn().cursor()
        return self.cursor

    def test(self):
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print data

    def where(self, data):
        comm = " where "
        if isstring(data):
            return comm + data
        for key in data:
            if str(data[key]).isdigit():
                comm += "%s=%s and " % (key, data[key])
            else:
                comm += "%s='%s' and " % (key, data[key])
        return comm[0:-4]

    def insert(self, query, params):
        # param = ()
        # length = len(data)
        # count = 0
        # for ii in xrange(0, length):
        # param += (tuple(data[ii].split()),)
        # if (ii + 1) % 1000 == 0 or (ii + 1) == length:
        #         count += self.cursor.executemany(query, param)
        # self.conn.commit()
        # return count
        try:
            self.cursor.executemany(query, params)
        except Exception, e:
            print "Execute %s Error: %s " % (query, e)
        finally:
            self.conn.commit()

    def insertDict(self, data):
        # 拼接 insert 语句
        keys = []
        values = []
        conditions = []
        params = []
        for key in data:
            if isinstance(key, int):
                continue
            if isinstance(data[key], datetime.date):
                if data[key].year < 1900:
                    data[key] = "1900-01-01 00:00:00"
                else:
                    data[key] = data[key].strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(data[key], long) or isinstance(data[key], int) or isinstance(data[key], float):
                data[key] = str(data[key])
            elif isinstance(data[key], unicode):
                data[key] = data[key].encode("utf-8", "ignore")
            keys.append(key)
            values.append("%s")
            conditions.append("%s=%s" % (key, "%s"))
            params.append(data[key])
        tmp = params
        params.extend(tmp)
        keys = ",".join(keys)
        values = ",".join(values)
        conditions = ",".join(conditions)
        comm = "insert into %s(%s) values(%s) on duplicate key update %s" % (data["table"], keys, values, conditions)

        # 尝试插入数据
        try:
            if params == "":
                return self.cursor.execute(comm)
            else:
                return self.cursor.execute(comm, params)
        except Exception, e:
            print e
            return 0
        finally:
            self.conn.commit()

    def update(self, query, params):
        try:
            self.cursor.executemany(query, params)
        except Exception, e:
            print "Execute %s Error: %s " % (query, e)
        finally:
            self.conn.commit()

    def delete(self, query):
        pass

    def select(self, query):
        self.query_result = []
        self.cursor.execute(query)
        while 1:
            result = self.cursor.fetchmany(1000)
            if len(result) == 0:
                break
            for item in result:
                self.query_result.append(list(item))
        return self.query_result, len(self.query_result)

    def flush(self, file, split="\t"):
        try:
            with open(file, "w") as fp:
                length = len(self.query_result)
                for ii in xrange(0, length):
                    out_str = ""
                    item = self.query_result[ii]
                    for jj in xrange(0, len(item)):
                        out_str += str(item[jj]) + split
                    out_str = out_str[:-1]
                    fp.write(out_str.strip() + "\n")
        except Exception, e:
            print e.message

    def close(self):
        self.cursor.close()
        self.conn.close()
        quiet = self.config.get("quiet", "False")
        if quiet == "True":
            pass
        else:
            print "Close connection to %s(%s)." % (self.config["host"], self.config["db"])

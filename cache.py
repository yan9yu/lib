#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Cache Module provides common cache-system-api-wrapper
    - Memcached
    - Redis

Required Library
    - redis
    - memcache

TODO:
    -




"""


class Cache():
    def __init__(self, config):
        self.config = config
        self.conn = None
        self.getConn()

    def set(self, config):
        self.config = config

    def getConn(self):
        host = self.config["host"]
        port = self.config["port"]
        type = self.config["type"]
        if type == "Redis":
            db = self.config["db"]
        else:
            db = None

        failure = 1
        while 1:
            try:
                if failure >= 3:
                    print "Failure to connect to %s:%s(%s) !" % (host, port, type)
                else:
                    if type == "Redis":
                        try:
                            import redis

                            self.conn = redis.Redis(host=host, port=port, db=db)
                            print "Connect to %s:%s(%s) successfully!" % (host, port, type)
                            break
                        except Exception, e:
                            print "ERROR: cannot connect to %s:%s(%s)! %s" % (host, port, type, e.message)
                            time.sleep(3)
                            failure += 1

                    if type == "Memcache":
                        try:
                            import memcache

                            server_port = "%s:%s" % (host, port)
                            self.conn = memcache.Client([server_port], debug=0)
                            print "Connect to %s:%s(%s) successfully!" % (host, port, type)
                            break
                        except Exception, e:
                            print "ERROR: cannot connect to %s:%s(%s)! %s" % (host, port, type, e.message)
                            time.sleep(3)
                            failure += 1

            except Exception, e:
                print e.message + " and will be restart to connect to %s:%s(%s) in 3secs" % (host, port, type)
                time.sleep(3)
                failure += 1

        return self.conn

    def test_conn(self):
        self.client.set("foo", "bar")
        return self.client.get("foo")


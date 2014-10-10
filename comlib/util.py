#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

"""




def import_test():
    try:
        import algo
        print "Import algo.py successfully..."
    except ImportError, e:
        print "Import algo.py failure!"
    try:
        import api
        print "Import api.py successfully..."
    except ImportError, e:
        print "Import api.py failure!"
    try:
        import cache
        print "Import cache.py successfully..."
    except ImportError, e:
        print "Import cache.py failure!"
    try:
        import conv
        print "Import conv.py successfully..."
    except ImportError, e:
        print "Import conv.py failure!"
    try:
        import date
        print "Import date.py successfully..."
    except ImportError, e:
        print "Import date.py failure!"
    try:
        import decorator
        print "Import decorator.py successfully..."
    except ImportError, e:
        print "Import decorator.py failure!"
    try:
        import file
        print "Import file.py successfully..."
    except ImportError, e:
        print "Import file.py failure!"
    try:
        import hash
        print "Import hash.py successfully..."
    except ImportError, e:
        print "Import hash.py failure!"
    try:
        import net
        print "Import net.py successfully..."
    except ImportError, e:
        print "Import net.py failure!"
    try:
        import prof
        print "Import prof.py successfully..."
    except ImportError, e:
        print "Import prof.py failure!"
    try:
        import rand
        print "Import rand.py successfully..."
    except ImportError, e:
        print "Import rand.py failure!"
    try:
        import reg
        print "Import reg.py successfully..."
    except ImportError, e:
        print "Import reg.py failure!"
    try:
        import sort
        print "Import sort.py successfully..."
    except ImportError, e:
        print "Import sort.py failure!"
    try:
        import sql
        print "Import sql.py successfully..."
    except ImportError, e:
        print "Import sql.py failure!"
    try:
        import thread
        print "Import thread.py successfully..."
    except ImportError, e:
        print "Import thread.py failure!"



def main():
    import_test()


if __name__ == "__main__":
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Prof Module provide profile-relevant functions


Required Library
    - memory_profiler
    - line_profiler

TODO:
    -



"""



try:
    """
        Functions relevant with Memory Usage
    """
    from memory_profiler import profile
    from memory_profiler import memory_usage

except ImportError:
    pass

try:
    """
        Functions relevant with CPU Usage
    """
    from line_profiler import LineProfiler

    def do_profile(follow=[]):
        def inner(func):
            def profiled_func(*args, **kwargs):
                try:
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return func(*args, **kwargs)
                finally:
                    profiler.print_stats()

            return profiled_func

        return inner

except ImportError:
    def do_profile(follow=[]):
        "Helpful if you accidentally leave in production!"

        def inner(func):
            def nothing(*args, **kwargs):
                return func(*args, **kwargs)

            return nothing

        return inner

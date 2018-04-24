# -*- coding: utf-8 -*-

import inspect


def myprint(*objs):
    obj = objs[0] if len(objs) == 1 else objs
    print('%3d.\t%s' % (inspect.currentframe().f_back.f_lineno, repr(obj)))

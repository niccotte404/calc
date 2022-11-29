# -*- coding: utf-8 -*-

def ReadingFile():
    f = open("test.txt")
    s = f.readline()
    f.close()
    return s

def Calc(sth):
    return eval(sth)
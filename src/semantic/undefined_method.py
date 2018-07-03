#!/usr/bin/python
# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        pass
    def My(self):
        pass

class B(A):
    def __init__(self):
        pass

def undefined_method():
    a = A()
    a.Myfun()

    b = B()
    b.My()

if __name__ == '__main__':
    pass
#!/usr/bin/python
# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        pass

def undefined_attribute():
    a = A()
    print a.attr


if __name__ == '__main__':
    pass
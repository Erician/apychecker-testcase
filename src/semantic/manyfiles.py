#!/usr/bin/python
# -*- coding: utf-8 -*-

import packagefile

def many_files():
    packagefile.a = 1
    packagefile.mya = 2
    packagefile.fun()
    packagefile.myfun()
    a = packagefile.A()
    b = packagefile.MyA()

if __name__ == '__main__':
    many_files()
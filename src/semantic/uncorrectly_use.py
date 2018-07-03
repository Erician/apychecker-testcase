#!/usr/bin/python
# -*- coding: utf-8 -*-

def un_use_dot():
    a = 1
    a.my = 3

def un_use_brackets():
    a = 1
    a[0] = 1

def un_use_break():
    break
    if 1:
        break



if __name__ == '__main__':
    un_use_dot()
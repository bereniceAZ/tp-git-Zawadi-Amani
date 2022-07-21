#!/usr/bin/env python


import sys

def add(a,b):
    return(a+b)


def main():
    arg=len(sys.argv)-1
    if (arg < 2):
        print("Error")
        x = int(sys.argv[1])
        y = int(input("Enter another values : "))
        print (add(x,y))

    else:
        x= int(sys.argv[1])
        y= int(sys.argv[2])
        print (add(x,y))

main()

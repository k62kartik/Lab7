#!/usr/bin/env python3
# Student ID: kartik
def function1():

    a = 'object_function1'
    print('print() call in function1 on a:',a)

def function2():

    a = 'function2_object'
    print('print() call in function2 on a:',a)

 '''a''' created in function1()
# or function2() with the print() functions after the calling function1() and function2()
# All the print() retrieved the value of object '''
a = 'object_in_main'
print('print() call in main on a:',a)
function1()
print('print() call in main on a:',a)
function2()
print('print() call in main on a:',a)

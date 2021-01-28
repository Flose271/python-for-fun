#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:18:01 2019

@author: TomMacbook
"""

from math import floor

print("Welcome to my base converter.")
print("This converts numbers from base 2 to 36.")
inBase = int(input("Input base: "))
outBase = int(input("Output base: "))       

while True:
    
    inNum = input("Input number: ")
        
    #You can also use X,E instead of A,B for dozenal.
            
    if(inBase == 12):
        inNum = inNum.replace('X','A')
        inNum = inNum.replace('E','B')
        
    #First we will find the location of the point in the input
        
    #We assume the point is at the end of the number:
    pointPos = len(inNum)
        
    #But we check the number to see where it actually is.
    for i in range(len(inNum)):
        if(inNum[i] == '.'):
            pointPos = i
        
    #Now we know where the point is, the point is removed.
    inNum = inNum.replace('.','')
                
    #We will make a function that can convert a single digit to base 10
        
    def digitDown(digit):
        digit = str(digit)
        x = ord(digit)
        if 47<x<58:
            return x-48
        elif 64<x<91:
            return x-55
            
    def digitUp(digit):
        if -1<digit<10:
            return chr(digit+48)
        if 9<digit<36:
            return chr(digit+55)
                
    #Now we convert our number into base 10
        
    tenNum = 0
            
    for i in range(0,len(inNum)):
        tenValue = digitDown(inNum[i])*(inBase**(pointPos-i-1))
        tenNum += tenValue
            
    #print(tenNum)
            
    #Now we convert it to the base we want.
        
    #We start with the integer.
        
    workingNum = floor(tenNum)
    preDigits = []
            
    preNum = 0
    while workingNum != 0:
        remainder = workingNum%outBase
        preDigits.insert(0,digitUp(remainder))
        workingNum = floor(workingNum/outBase)
        preNum = ''.join(preDigits)
        
    #Now we do the float.
            
    workingNum = tenNum - floor(tenNum)
    postDigits = []
            
    postNum = ''
    while workingNum != 0 and len(postDigits)<20:
        x = workingNum*outBase
        postDigits.append(digitUp(floor(x)))
        workingNum = x - floor(x)
        postNum = ''.join(postDigits)
            
    #We add up the result
            
    if(postNum != ''):
        outNum = str(preNum) + '.' + postNum
    else:
        outNum = preNum
            
    #Again, for base 12...
    
    outNum = str(outNum)
    outNum = outNum.replace('A','X')
    outNum = outNum.replace('B','E')
            
    #We finally print the result.
            
    print(outNum)
            
            
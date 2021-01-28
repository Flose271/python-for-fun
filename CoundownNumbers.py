#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 01:21:56 2020

@author: TomMacbook
"""

#To use this program, write countdown([values],target)

def combine(x,y):
    con = []
    for e in x:
        con.append(e not in y)
    if(all(con)==True):
        return(sorted(x+y))
    else:
        return []
    
def add(x,item,test=0):
    if(item not in x):
        x.append(item)

def solve(l,target,limit=1200):
    
    x = []
    
    for e in l:
        if((e,[str(e)]) not in x):
            x.append((e,[str(e)]))
        else:
            x.append((e,[str(e) + 'c']))
    
    working = x.copy()
    new = x.copy()
    
    nums = [e[0] for e in x]
    
    while True:
    
        for one in working:
            for two in working:
                
                if(one[0]+two[0]<limit):  
                    newElement = (one[0]+two[0], combine(one[1],two[1]),[one,two,'+'])
                    if(newElement[1] != []):
                        add(new,newElement)
                        add(nums,newElement[0],1)
                        
                        if(target == newElement[0]):
                            return newElement
                    
                if(one[0]-two[0] >0):
                    newElement = (one[0]-two[0], combine(one[1],two[1]),[one,two,'-'])
                    if(newElement[1] != []):
                        add(new,newElement)
                        add(nums,newElement[0],1)
                
                        if(target == newElement[0]):
                            return newElement
                
                if(one[0]*two[0]<limit):
                    newElement = (one[0]*two[0], combine(one[1],two[1]),[one,two,'*'])
                    if(newElement[1] != []):
                        add(new,newElement)
                        add(nums,newElement[0],1)
                
                        if(target == newElement[0]):
                            return newElement
                    
                if(one[0]/two[0] == one[0]//two[0]): #Divides properly
                    newElement = (one[0]//two[0], combine(one[1],two[1]),[one,two,'/'])
                    if(newElement[1] != []):
                        add(new,newElement)
                        add(nums,newElement[0],1)
                
                        if(target == newElement[0]):
                            return newElement
                    
        
        if(working == new):
            return '0'
        else:
            working = new
    
    
def explain(x):
    
    if(x == '0'):
        return '(No solution found)'
    
    if(len(x[1])==1):
        ans = str(x[0])
    else:
        ans = ('(' + str(x[0]) + '=' + explain(x[2][0]) + str(x[2][2]) + 
                 explain(x[2][1]) + ')')
    
    return ans
        
        
def countdown(x,target):
    return explain(solve(x,target))[1:-1]
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:28:08 2020

@author: TomMacbook
"""

from random import shuffle

import matplotlib.pyplot as plt

denominations = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def insert(deck,table,index):
    for pos in index:
        if(len(deck) != 0):
            card = deck.pop(0)
            table[pos] = card

def find(table,search):
    index = []
    for search_card in search:
        added = False
        for i in range(len(table)):
            if((search_card == table[i]) and 
               (i not in index) and 
               (added == False)):
                   index.append(i)
                   added = True
        if(added == False):
            return False
    return index

def fulldeck():
    deck = []
    for i in range(4):
        deck += denominations
    shuffle(deck)
    return deck

def searchlist():
    search = [['A','10'],['2','9'],['3','8'],['4','7'],['5','6'],['J','Q','K']]
    for card in denominations:
        search.append([card,card,card])
    search.reverse()
    return search

deck = fulldeck()
search_list = searchlist()
table = []

'''
while True:
    print(table)
    alive = False
    for search in search_list:
        if(alive == False):
            index = find(table,search)
            if(index != False):
                insert(deck,table,index)
                alive = True
    if(len(deck) == 0):
        break
    if(alive == False):
        if(len(table)<9):
            new_card = deck.pop(0)
            table.append(new_card)
        else:
            break
'''


def game(show = False, max_cards = 9):
    
    deck = fulldeck()
    search_list = searchlist()
    table = []
    
    while True:
        
        if(show == True):
            print(table)
    
        alive = False
        for search in search_list:
            if(alive == False):
                index = find(table,search)
                if(index != False):
                    insert(deck,table,index)
                    alive = True
        if(len(deck) == 0):
            break
        if(alive == False):
            if(len(table)<max_cards):
                new_card = deck.pop(0)
                table.append(new_card)
            else:
                break
    
    return len(deck)

def many_games(trials=10000,max_cards=9):
    won_games = 0
    for i in range(trials):
        if(game(trials,max_cards) == 0):
            won_games += 1
    return won_games/trials

def dict_games(trials=10000,max_cards=9):
    values = {}
    for i in range(trials):
        g = game(trials,max_cards)
        if(g not in values):
            values[g] = 1
        else:
            values[g] += 1
    return values

def gameplot(trials=10000,max_cards=9):
    d = dict_games(trials,max_cards)
    keys = d.keys()
    values = d.values()
    plt.scatter(keys,values)
    plt.show()
    
def cumulative_value(d,value):
    total = 0
    for cards_left in d:
        if(cards_left<=value and cards_left != 0):
            total += d[cards_left]
    return (d[0])/(d[0]+total)

def percentplot(trials=10000,max_cards=9):
    d = dict_games(trials,max_cards)
    x = [i for i in range(53)]
    y = [cumulative_value(d,element) for 
         element in x]
    plt.axis([52,0,0,1])
    plt.plot(x,y)
    plt.show()
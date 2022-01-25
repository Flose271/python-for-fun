# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from itertools import permutations
from random import choice as random_choice

def compare(first,second):
    
    black = 0
    white = 0
    
    for i, letter in enumerate(first):
        
        if second[i] == letter:
            
            black += 1
        
        elif letter in second:
            
            white += 1
            
    return (black, white)


def bwfilter(original,choices,bw_map):
            
    return [c for c in choices if compare(original,c) == bw_map]


def create_choices(num_colours, num_pegs):
    
    colours = [chr(97 + i) for i in range(num_colours)]
    
    return [''.join(i) for i in list(permutations(colours, num_pegs))]


def create_bws(num_pegs):
    
    bws = list()
    
    for i in range(num_pegs+1):
        
        for j in range(num_pegs-i+1):
            
            bws.append((i,j))
            
    return bws

    

def find_best_choice(choices, bws):
    
    best_choice = choices[0]
    smallest_largest_bw = None
    
    for c in choices:
        
        #for each c we find the length of each bw filter
        
        largest_bw = 0
        
        for bw in bws:
            
            num_new_choices = len(bwfilter(c,choices,bw))
            
            if num_new_choices > largest_bw:
                
                largest_bw = num_new_choices
                
        if smallest_largest_bw == None:
            
            smallest_largest_bw = largest_bw
                
        elif largest_bw < smallest_largest_bw:
            
            best_choice = c
            
    return best_choice


def find_num_cycles(num_colours, num_pegs):
    
    choices = create_choices(num_colours,num_pegs)
    bws = create_bws(num_pegs)
    correct = random_choice(choices)
    
    cycles = 0
    
    while True:
    
        cycles += 1
        
        # the compute makes its guess
        
        if cycles == 1:
            
            guess = choices[0]
            
        else:
            
            guess = find_best_choice(choices, bws)
        
        if guess == correct: return cycles
        
        # the computer is told how right it was
        guess_bw = compare(correct,guess)
        
        # the computer eliminates impossible choices 
        choices = bwfilter(guess,choices,guess_bw)
        
        if cycles > 100:
            
            return 'Failure'
        
def result_dict(num_colours,num_pegs,turns):
    
    results = {}
    
    for i in range(turns):
        
        r = find_num_cycles(num_colours,num_pegs)
        
        if r in results:
            
            results[r] += 1
            
        else:
            
            results[r] = 1
            
    return [(r, results[r]) for r in sorted(results)]

def solve(num_colours,num_pegs):

    choices = create_choices(num_colours,num_pegs)
    bws = create_bws(num_pegs)
    guess_no = 1
    
    while len(choices) > 1:
        
        if guess_no == 1:
            
            guess = choices[0]
        
        else:
    
            guess = find_best_choice(choices,bws)
        
        print('MASTERMIND GUESSES: ' + guess)
    
        b = int(input('Black Pegs: '))
        w = int(input('White Pegs: '))
        
        guess_bw = (b,w)
        
        choices = bwfilter(guess,choices,guess_bw)
        
        guess_no += 1
        
    if len(choices) == 1:
        
        print('MASTERMIND FOUND: ' + choices[0])
        
    else:
        
        print('THERE ARE NO POSSIBLE ANSWERS LEFT.')
    
    
    

    
    
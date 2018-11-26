#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:48:47 2018

@author: griggles
"""


#DEMONSTRATION OF POINT IN RANDOM VARIABLES OVER A DISCRETE SPACE

#LOGIC________

import numpy as np

def inverse_map(f):
    inverse  = {}
    for v in f.values():
        listy = []
        for k in f.keys():
            if f[k] == v:
                listy.append(k)
        inverse[v] = listy
    return inverse

def to_distribution(experiment):
    return dict(zip(experiment['elements'], experiment['probs']))

def get_probability_of_event(experiment, event):
    distribution = to_distribution(experiment)
    p = 0
    for element in set(event):
        p += distribution[element]
    return p

comparators = {'<': lambda x, y: x < y, '==': lambda x, y: x == y, '>': lambda x, y: x > y,\
               '<=': lambda x, y: x <= y, '>=': lambda x, y: x >= y,}


#What is the probability that a random variable is <, <=, ==, >=, > value?
def probability(experiment, random_variable, comparator, value):
    inverse = inverse_map(random_variable)
    
    elements = []
    for v in inverse.keys():
        if (comparators[comparator])(v, value):
            elements += inverse[v]
    return get_probability_of_event(experiment, set(elements))  


def expected_value(experiment, random_variable):
    exp_val = 0
    for value in set(random_variable.values()):
        exp_val += value*probability(experiment, random_variable, '==', value)
    return exp_val

#MODEL_____


#DEFINE SAMPLE SPACE
dice = {'elements': np.array(['one', 'two', 'three', 'four', 'five', 'six'], dtype='<U5'),
          'probs': np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])}

#ENSURE probs is a valid probability distribution!
epsilon = 1/10000000000
sum = 0
for p in dice['probs'].tolist():
    sum += p
if not (1 - epsilon <= sum <= 1 + epsilon):
    raise ValueError('Probability distributions must sum to 1')
    
    
#DEFINE RANDOM VARIABLES FOR ARBITRARY QUESTIONS/PROPERTIES ABOUT/ON SAMPLE SPACE
is_even = {'one': 0, 'two': 1, 'three': 0, 'four': 1, 'five': 0, 'six': 1}
identity = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
money_game = {'one': -50, 'two': -50, 'three': 10, 'four': 20, 'five': 40, 'six': 100}




#ASK QUESTIONS ABOUT YOUR SAMPLE SPACE THROUGH RANDOM VARIABLES!
print(probability(dice, is_even, '==', 1))
print(expected_value(dice, money_game))

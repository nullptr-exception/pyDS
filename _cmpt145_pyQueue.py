#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:52:24 2018

@author: null

@Module :-> PyQueue     ->   F.I.F.O

"""
#import sys

# ConsT
_FRONT = 0


# create a new data structure; Queue that performs the queueing operation(s)
# In this version, Operation(s) include but are not limited to:
# (1) create()      -> creates an empty queue
# (2) is_empty(queue)   -> returns True if the given queue has no data in it
# (3) size(queue)       -> returns the number of data values in the given queue
# (4) enqueue(queue, value)     -> adds a given value to the back of the given queue
# (5) dequeue(queue)    -> remove the value at the front of the given queue and return it
# (6) peek(queue)   -> returns the value at the front of the given queue without remvoing it

# =============================================================================
#             -> Basic Queue Operation(s) <-
# =============================================================================

def isValid_type(queue):
    """
        -> SImply return the type of t
        
        @param : t  -> type to check
        
        @return : -> type of t
    """
    return True if queue['Type'] == 'pyQueue' else False



def create():
    """
        -> Creates an empty queue data structure and return it <-
        
        @param : None
        
        @return :  default initial queue created  (dict)
    """
    return {'Data': [], 'Frequency': {}, 'Length': 0, 'Type': 'pyQueue'}


#_q = _create()


#print(_q)
#
#
#sys.exit(-6)

# =============================================================================
# #print(type(_q))
# 
# print(len(_q[0])); sys.exit(-1)
# =============================================================================

def is_empty(queue):
    """
        -> Given a queue type; return True if empty. False otherwise <-
        
        @param : queue  ->  queue to check   (Queue type ->(dict))
        
        @return :  True if empty; False otherwise  (bool)
    """
    return True if queue['Length'] == 0 else False



#print(_q['Length'])


#_empty = _is_empty(_q)
#
#print(_empty); sys.exit(-2)

def size(queue):
    """
        -> Return the number of data values in queue <-
        
        @param : queue: Queue data structure to operate on ->  (tuple)
        
        @return  : Number of data values in queue  (int)
                : 0 is returned if no element is in the queue
    """
    return queue['Length']


#_s = _size(_q)
#
#print(_s)
#
#sys.exit(-6)


def enqueue(queue, value):
    """
        -> Adds a given value to the back of a given queue  <-
        
        @param : queue  ->  queue to add value in (tuple DT)
        @param : value  -> value to add  (arb.)

        @return :       None
    """
    getattr(queue['Data'], 'append')(value)
    
    # modify the length
    queue['Length'] += 1
    
    # modify the dict rec
    if value in queue['Frequency']:        #  it's been seen before
        queue['Frequency'][value] += 1
    else:       # first time
        queue['Frequency'][value] = 1
        

#enqueue(_q, 3)
#enqueue(_q, 9)
#enqueue(_q, 9)      
#
#print(q)
#
#sys.exit(-7)


def dequeue(queue):
    """
        -> Remove the value from the front of queue and return it <-
        
        @param : queue
        
        @return :  value in front of queue  (??)
    
    """
    _val = queue['Data'][_FRONT]
    queue['Data'].remove(_val)
    
    # modify the length
    queue['Length'] -= 1
    
    # look at the dictionary and keep track
    if _val in queue['Frequency']:
        # check how many
        if queue['Frequency'][_val] == 1:     # it's count 1. delete it !!!
            del queue['Frequency'][_val]
        else:   # it's more than 1. decrement it
            queue['Frequency'][_val]  -= 1
    return _val
    # ....!
            

#_enqueue(_q, 3)
#_enqueue(_q, 9)
#_enqueue(_q, 7)      
#_enqueue(_q, 9)
#_enqueue(_q, 4)
#_enqueue(_q, 5)
#_enqueue(_q, 7)
#_enqueue(_q, 1)
#    
#print(_q)
#
#_dequeue(_q)
#_dequeue(_q)
#
#print(_q)
#            
#sys.exit(-7)



def peek(queue):
    """
        -> Returns the value at the front of the given queue without removing it <-
        
        @param : queue -> queue to look  (tuple DT)
        
        @return :  value in front of queue  (??)
    """
    return queue['Data'][_FRONT]





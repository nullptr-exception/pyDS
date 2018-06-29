#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 04:53:08 2018

@author: nullptr
@module: Node

"""

def create(data, next=None):
    """
        -> creates a new node for the given data <-
        
        @param: data  -> any data value to store in the node
        @param: next  -> another node or None
        
        @return: newly created node
    
    """
    return {'data': data, 'next': next}




def get_data(node):
    """
        -> retrieve the data stored in the given node <-
        
        @param: node  -> node to retrieve data
        
        @return : data stored in the given node
    
    """
    return node['data']




def get_next(node):
    """
        -> retrieve the data stored in the next field of a given node <-
        
        @param: node  -> node to retrieve data
        
        @return: another node or None
    
    """
    return node['next']





def set_data(node, value):
    """
        -> set(assign(s)) the value in the given node data field <-
        
        @param: node  -> node to set/assign value
        @param: value  -> value to store in node data field
        
        @return: None
    
    """
    node['data'] = value


    
    
def set_next(node, value):
    """
        -> set(assign(s)) the value in the given node next field <-
        
        @param: node  -> node to set/assign value
        @param: value  -> value to store in node next field
        
        @return: None
    
    """
    node['next'] = value
    
        
    


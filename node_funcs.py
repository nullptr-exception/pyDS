#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 06:58:12 2018

@author: nullptr
@module: Basic Node Function(s)

"""
import copy
import Node as node
import NodeBased_LinkedList as pylist

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain. E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty
    Post_conditions:
        None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain is None:
        result = 'EMPTY'
    else:
        # walk along the chain
        cur_node = node_chain['head']     # make a copy
        
        value = node.get_data(cur_node)
        # construct the data
        result = '[ ' + str(value) + ' |'
        
        prev_node = None
        while node.get_next(cur_node) is not None:
            
            prev_node = cur_node
            cur_node = node.get_next(cur_node)
            
            if prev_node is not None:
                value = node.get_data(cur_node)
                result += ' *-]-->[ '+str(value)+' |'
            else:
                continue
        # at the end of the chain, use '/'
        result += ' / ]'

    return result





def count_chain(node_chain):
    """
    Purpose:
        Counts the number of nodes in the node chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Return:
        :return: The number of nodes in the node chain.
    """
    count = 0  # initial count
    if node_chain is None:
        return count
    else:
        chain = node_chain['head']
        
        while chain is not None:
            count += 1
            chain = node.get_next(chain)
        return count



def copy_chain(node_chain):
    """
    Purpose:
        Make a new node chain with the same values as in node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly None
    Return:
        :return: A copy of node chain, with new nodes, but the same data.
    """
    if node_chain is None:
        pass
    else:
        # ..
        return copy.deepcopy(node_chain)
            
    
    

def replace(node_chain, target, value):
    """
    Purpose:
        Replace every occurrence of data target in node_chain with data value
        The chain should change data values only!
    Pre-Conditions:
        :param node_chain: a node-chain, possibly empty
        :param target: a data value
        :param value: a data value
    Post-conditions:
        The node-chain is changed, by replacing target with value everywhere.
    Return:
        :return: None
    """
    chain = node_chain['head']
    while chain is not None:
        val = node.get_data(chain)
        
        if val == target:
            node.set_data(chain, value)
        chain = node.get_next(chain)





def split_chain(node_chain):
    """
    Purpose:
        Splits the given node chain in half, returning the second half.
        If the given chain has an odd length, the extra node is part of
        the second half of the chain.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
    Post-conditions:
        the original node chain is cut in half!
    Return:
        :return: A tuple (nc1, nc2) where nc1 and nc2 are node-chains
         each containing about half of the nodes in node-chain
    """

    if node_chain is None:       
        return None, None
    elif node_chain['size'] ==  1:
        return None, node_chain
    else:
        copied_chain = copy_chain(node_chain['head'])
        cur_node = copied_chain
        target = ((node_chain['size'] // 2) - 1)
        counter = 0

        while counter < target:
            
            cur_node = node.get_next(cur_node)
            counter += 1
        second_half = node.get_next(cur_node)
        node.set_next(cur_node, None)

        # nested func 01
        def _construct_node(nc1, nc2):
            """
                ->  <-

                @param: nc1  -> splitted node chain 1
                @param: nc2  -> splitted node chain 2

                @return:
            """
            n1, n2 = {}, {}
            
            # doubly nested func 02
            def __constructor(new_node, old_node):
                """
                    ->  <-

                    @param: n  -> node

                    @return:
                """
                new_node['head'] = old_node
                cur_tail = new_node['head']
                node_count = 1
                
                while node.get_next(cur_tail) is not None:
                    cur_tail = node.get_next(cur_tail)
                    node_count += 1
                new_node['tail'] = cur_tail
                new_node['size'] = node_count
            __constructor(n1, nc1)
            __constructor(n2, nc2)

            return n1, n2
            
        
        return _construct_node(copied_chain, second_half)

            
        
        



def remove_chain(node_chain, val):
    """
    Purpose:
        Remove the first occurrence of val from node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
        :param val: a value to be removed
    Post-conditions:
        The first occurrence of the value is removed from the chain.
        If val does not appear, the node-chain is unmodified.
    Return:
        :return: The resulting node chain with val removed
    """

    pylist.delete_value(node_chain, val)

    return node_chain
            





def insert_at(node_chain, index, value):
    """
    Purpose:
        Insert the given value into the node-chain so that
        it appears at the the given index.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
        :param value: a value to be inserted
        :param index: the index where the new value should appear
        Assumption:  0 <= index <= n
                     where n is the number of nodes in the chain
    Post-condition:
        The node-chain is modified to include a new node at the
        given index with the given value as data.
    Return
        :return: the node-chain with the new value in it
    """

    pylist.insert_value_at_index(node_chain, index, value)

    return node_chain


# --------------------------------------------------
# @Module: Node Based Tree Node Implementation
# @Author: Nullptr Exception (non447@mail.usask.ca)
# @
# @
# @
# @
# @
# @
# ---------------------------------------------------

import Node as node


def create(data, left=None, right=None):
    """
        ->
           Creates a treenode to contain the data value
           and the given left and right values.
           If left and right are not given the value None
           is used by default
        <-

        @param: data  ->
        @param: left  ->
        @param: right  ->

        @return:...
    """
    treenode = {}
    treenode['data'] = data
    treenode['left'] = left
    treenode['right'] = right

    return treenode




def get_data(treenode):
    """
        ->
           Returns the content(s) of the data field in the given
           treenode
        <-

        @param: treenode  ->

        @return:...
    """
    return treenode['data']





def get_left(treenode):
    """
        ->
           Returns the content(s) of the left field of the
           given treenode
        <-

        @param: treenode  ->

        @return:...
    """
    return treenode['left']




def get_right(treenode):
    """
        ->
           Returns the content(s) of the right field of the
           given treenode
        <-

        @param: treenode  ->

        @return:...
    """
    return treenode['right']





def set_data(treenode, value):
    """
        ->
           Given a treenode, set the content(s) of the data
           field to value
        <-

        @param: treenode  ->
        @param: value  ->

        @return:...
    """
    treenode['data'] = value



def set_left(treenode, n):
    """
        ->
           Given a treenode, set(s) the content(s) of the left
           field to n
        <-

        @param: treenode  ->
        @param: n  ->

        @return:...
    """
    treenode['left'] = n





def set_right(treenode, n):
    """
        ->
           Given a treenode, set(s) the content(s) of the
           right field to n
        <-

        @param: treenode  ->
        @param: n  ->

        @return:...
    """
    treenode['right'] = n






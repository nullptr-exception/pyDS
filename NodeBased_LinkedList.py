# -----------------------------------------------------
#
# @ Module -> Node-Based Linked List
# @ Author -> Nullptr Exception (non447@mail.usask.ca)
# @
# @
# @
# @
# @
# 
# ------------------------------------------------------
import Node as node


def create():
    """
        ->  <-

        @param: None

        @return:...
    """
    linked_list = {}
    linked_list['head'] = None
    linked_list['tail'] = None
    linked_list['size'] = 0

    return linked_list





def size(l_list):
    """
        ->  <-

        @param: l_list  ->

        @return:...
    """
    return l_list['size']




def is_empty(l_list):
    """
        ->  <-

        @param: l_list  ->

        @return:...
    """
    return l_list['size'] == 0




def add_to_front(alist, value):
    """
        ->  <-

        @param: alist  ->
        @param: value  ->

        @return: None
    """
    new_node = node.create(value, alist['head'])
    alist['head'] = new_node
    cur_last_node = alist['head']
    alist['size'] += 1
    while node.get_next(cur_last_node) is not None:
        cur_last_node = node.get_next(cur_last_node)
    alist['tail'] = cur_last_node
    




def remove_from_front(alist):
    """
        -> <-

        @param: alist  ->

        @return:...
    """
    next_head = None
    cur_head = alist['head']
    value = node.get_data(cur_head)
    next_head = node.get_next(cur_head)
    alist['head'] = next_head
    alist['size'] -= 1
    return value




def add_to_back(alist, value):
    """
        ->  <-

        @param: alist  ->
        @param: value  ->

        @return:...
    """
    new_node = node.create(value)   # next = None

    if not alist['size'] == 0: # at least one node
        cur_back = alist['tail']   
        node.set_next(cur_back, new_node)
    else:   # its the first node  
        alist['head'] = new_node
    alist['tail'] = new_node 
    alist['size'] += 1



def remove_from_back(alist):
    """
        ->  <-

        @param: alist  ->

        @return:...
    """
    cur_node = alist['head']
    prev_node = None

    while node.get_next(cur_node) is not None:
        prev_node = cur_node
        cur_node = node.get_next(cur_node)
    node.set_next(prev_node, None)
    alist['tail'] = prev_node
    alist['size'] -= 1
    return node.get_data(cur_node)





def get_data_at_index(alist, idx):
    """
        ->  <-

        @param: alist  ->
        @param: idx  ->

        @return:...
    """
    # boundary check(s)
    assert idx >= 0 and idx < size(alist), '[ ERROR ] Index {} Out-Of-Range\
'.format(idx)
    # keep track of the current index
    cur_index = 0
    cur_node = alist['head']
    
    # special case
    if cur_index == idx: # idx == 0
        return node.get_data(cur_node)
    # general case
    while node.get_next(cur_node) is not None:
        cur_index += 1
        if cur_index == idx:
            return node.get_data(node.get_next(cur_node))
        cur_node = node.get_next(cur_node)
    
        
        



def set_data_at_index(alist, idx, value):
    """
        ->  <-

        @param: alist  ->
        @param: idx  ->
        @param: value  ->

        Note: list structure is Unchanged

        @return: None
    """
    # boundary check(s)
    assert idx >= 0 and idx < size(alist), '[ ERROR ] Out-of-range'
    
    new_node = node.create(value)
    cur_node = alist['head']
    cur_index = 0 # keep track of the current index

    # special case(s)
    if cur_index == idx:    # 0 == idx? (front of list)
        _ = remove_from_front(alist)
        add_to_front(alist, node.get_data(new_node))
    elif idx == size(alist) - 1:  # (back of list)
        _ = remove_from_back(alist)
        add_to_back(alist, node.get_data(new_node))
    else:
        # general case
        while node.get_next(cur_node) is not None:
            cur_node = node.get_next(cur_node)
            cur_index += 1

            if cur_index == idx:
                node.set_data(cur_node, node.get_data(new_node))
                return  # break off loop early




def value_is_in(alist, value):
    """
        ->  <-

        @param: alist  ->
        @param: value  ->

        @return:...
    """
    cur_node = alist['head']
    match_found = False

    cur_index = 0
    while cur_index < size(alist):
        cur_data =  get_data_at_index(alist, cur_index)

        if cur_data == value:
            match_found = True
            return match_found
        cur_index += 1
    return match_found
    

    


def get_index_of_value(alist, value):
    """
        ->  <-

        @param: alist  ->
        @param: value  ->

        @return:...
    """
    val_is_in = (False, None)   # initial state
    cur_index = 0

    while cur_index < size(alist):
        ret_val = get_data_at_index(alist, cur_index)

        if ret_val == value:
            val_is_in = (True, cur_index)
            return val_is_in
        cur_index += 1
    return val_is_in    # tuple






def insert_value_at_index(alist, idx, value):
    """
        ->  <-

        @param: alist  ->
        @param: value  ->
        @param: idx  ->

        Note: list structure is changed
        
        @return: None
    """
    assert idx >= 0 and idx < size(alist), '[ OUT ] Error: Out-Of-Range'
    
    # special case(s)  
    if idx == size(alist) -1:   # back
        add_to_back(alist, value)
    elif idx == 0:  # front
        add_to_front(alist, value)
    else:
        # general case
        cur_node = alist['head']
        prev_node = None
        cur_index = 0
        while node.get_next(cur_node) is not None:
            prev_node = cur_node
            cur_node = node.get_next(cur_node)

            cur_index += 1

            if cur_index == idx:
                new_node = node.create(value) # next = None                
                node.set_next(prev_node, new_node)
                node.set_next(new_node, cur_node)
                alist['size'] += 1
                return  # break out of the loop early
            




def delete_item_at_index(alist, idx):
    """
        ->  <-

        @param: alist  ->
        @param: idx  ->

        @return:...
    """
    assert idx >= 0 and idx < size(alist), '[ OUT ] Error: Out-Of-Range'

    # special case(s)
    if idx == 0:    # front
        remove_from_front(alist)
    elif idx == size(alist) -1: # back
        remove_from_back(alist)
    else:
        # general case
        cur_index = 0
        cur_node = alist['head']
        prev_node = None

        while node.get_next(cur_node) is not None:
            prev_node = cur_node
            cur_node = node.get_next(cur_node)
            cur_index += 1

            if cur_index == idx:
                next_node = node.get_next(cur_node)
                node.set_next(prev_node, next_node)
                alist['size'] -= 1
                return # break off early
            




def delete_value(alist, value):
    """
        ->  <-

        @param: alist  ->
        @param: value  ->

        @return:...
    """
    deleted =  False
    is_in, value_index = get_index_of_value(alist, value)

    if is_in:
        delete_item_at_index(alist, value_index)
        deleted = True
    return deleted





##llist = create()
##add_to_front(llist, 88)
##add_to_front(llist, 5)
##add_to_front(llist, 19)
##add_to_front(llist, 27)


##print((llist))
##
##print()

##print('[ OUT ] removed {} from front\
##'.format(remove_from_front(llist)))
##print()
##add_to_back(llist, 100)
##add_to_back(llist, 132)
##add_to_back(llist, 215)
##add_to_back(llist, 600)
##print()
##print('[ OUT ] added item to back')
##print()
##print(llist)
##print()
##print('[ OUT ] removed {} from front\
##'.format(remove_from_front(llist)))
##print()
##print(llist)
##print()
##print('[ OUT ] removed {} from back\
##'.format(remove_from_back(llist)))
##print()
##print(llist)
##print()
##print('[ OUT ] got {}\
##'.format(get_data_at_index(llist, 5)))
##
##print()
##
##print('[ OUT ] length = {}\
##'.format(size(llist)))
##add_to_front(llist, 512)
##add_to_back(llist, 1024)
##print()
##print(llist)


##set_data_at_index(llist, 2, 51255)
##print()
##
##print(llist)

##print()
##
##print(value_is_in(llist, 5))
##
##print(get_index_of_value(llist, 88))
##
##insert_value_at_index(llist, -1717, 0)
##insert_value_at_index(llist, 10000, size(llist) -1)
##insert_value_at_index(llist, 990, 2)
##
##
##print()
##print(llist)

##delete_item_at_index(llist, 2)


##print('[ OUT ] deleted: {}\
##'.format(delete_value(llist, 19)))
##print()
##
##print(llist)






    

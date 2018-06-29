from NodeBased_LinkedList import *
from node_funcs import *

import random as rand

"""
    Available Function(s) + Return Value(s)
    ---------------------------------------
    (1) create() : Dict
    (2) size(l_list) : Int
    (3) is_empty(l_list) : Bool
    (4) add_to_front(alist, value) : None
    (5) remove_from_front(alist) : Ret
    (6) add_to_back(alist, value) : None
    (7) remove_from_back(alist) : Ret
    (8) get_data_at_index(alist, idx) : Ret
    (9) set_data_at_index(alist, idx, value) : None
   (10) value_is_in(alist, value) : Bool
   (11) get_index_of_value(alist, value) : Tuple
   (12) insert_value_at_index(alist, idx, value) : None
   (13) delete_item_at_index(alist, idx) : None
   (14) delete_value(alist, value) : Bool

   (15) to_string(node_chain) : Str
   (16) count_chain(node_chain) : Int
   (17) copy_chain(node_chain) : Node
   (18) replace(node_chain, target, value) : None
   (19) split_chain(node_chain) : Tuple
   (20) remove_chain(node_chain, val): Node
   (21) insert_at(node_chain, index, value) : Node

"""

collection  = create()

for i in range(0, 15):
    add_to_back(collection, rand.randint(1, 25))

##add_to_back(collection, 3)
##add_to_back(collection, 1)
##add_to_back(collection, 4)
##add_to_back(collection, 1)
##add_to_back(collection, 5)

##pylist.insert_value_at_index(collection, 0, -1)

##print('[ OUT ] Original Collection:\n\n {}'.format(collection))
print()

c1, c2 = split_chain(collection)

##c2 = (remove_chain(c2, 14))

##insert_at(c2, 3, 100)

print(to_string(collection))
print()
print(to_string(c1))
print()
print(to_string(c2))
print()






##print(collection)

##print(c1)
print()
##print(c2)

##print()
##print(collection)

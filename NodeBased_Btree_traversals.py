
import NodeBased_BTreeNode as treenode
import NodeBased_Queue as pyqueue
import NodeBased_Stack as pystack


# ---------------------------------
#   Traversal(s)
# ---------------------------------

def pre_order(tnode):
    """
        ->  <-

        @param: tnode  ->

        @return:...
    """
    if tnode is None:
        return
    else:
        print(treenode.get_data(tnode), end=' ')
        pre_order(treenode.get_left(tnode))
        pre_order(treenode.get_right(tnode))





def in_order(tnode):
    """
        ->  <-

        @param: tnode  ->

        @return:...
    """
    if tnode is None:
        return
    else:
        in_order(treenode.get_left(tnode))
        print(treenode.get_data(tnode), end=' ')
        in_order(treenode.get_right(tnode))




def post_order(tnode):
    """
        ->  <-

        @param: tnode  ->

        @return:...
    """
    if tnode is None:
        return
    else:
        post_order(treenode.get_left(tnode))
        post_order(treenode.get_right(tnode))
        print(treenode.get_data(tnode), end=' ')





def breadth_first_order(tnode):
    """
        ->  <-

        @param: tnode  ->

        @return:...
    """
    explore =  pyqueue.create()
    pyqueue.enqueue(explore, tnode)
    while pyqueue.size(explore) > 0:
        current = pyqueue.dequeue(explore)
        print(treenode.get_data(current), end=' ')

        left =  treenode.get_left(current)
        if left is not None:
            pyqueue.enqueue(explore, left)
        right = treenode.get_right(current)
        if right is not None:
            pyqueue.enqueue(explore, right)




def height(tnode):
    """
        -> <-

        @param: tnode  ->

        @return: the height of a given tree node (int)
    """
    if tnode is None:
        return 0
    else:
        left_h = height(treenode.get_left(tnode))
        right_h = height(treenode.get_right(tnode))
        return 1 + max(left_h, right_h)



def count(tnode):
    """
        ->  <-

        @param: tnode  -.

        @return:
    """
    if tnode is None:
        return 0
    else:
        return (1 + count(treenode.get_left(tnode))
                  + count(treenode.get_right(tnode)))




def member(tnode, value):
    """ 
        ->  <-

        @param: tnode  ->
        @param: value  ->

        @return:...
    """
    if tnode is None:
        return False
    else:
        return (treenode.get_data(tnode) == value
                or member(treenode.get_left(tnode), value)
                or member(treenode.get_right(tnode), value))





print(pystack)




root = treenode.create(2)

a = treenode.create(7)
b = treenode.create(5)
c = treenode.create(11)
d = treenode.create(6)

treenode.set_left(root, a)
treenode.set_right(root, b)
treenode.set_left(a, c)
treenode.set_right(a, d)

##print(root)


##breadth_first_order(root)

print(member(root, 4))

##pre_order(root)
##print()
##in_order(root)
##print()
##post_order(root)

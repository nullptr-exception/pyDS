import Node as node

# L.I.F.O


def create():
    """
        ->  <-

        @param: None

        @return: stack created
    """
    stack = {}
    stack['top'] = None
    stack['size'] = 0

    return stack




def size(stack):
    """
        ->  <-

        @param: stack  ->

        @return: ...
    """
    return stack['size']




def is_empty(stack):
    """
        ->  <-

        @param: stack  ->

        @return:...
    """
    return stack['size'] == 0




def peek(stack):
    """
        ->  <-

        @param: stack  ->

        @return:...
    """
    assert not is_empty(stack), '[ ERROR ] Peeked on empty stack'

    first_node = stack['top']
    data = node.get_data(first_node)
    return data




def pop(stack):
    """
        ->  <-

        @param: stack  ->

        @return:...
    """
    assert not is_empty(stack), '[ ERROR ] Popped an empty stack'

    prev_first_node = stack['top']
    data = node.get_data(prev_first_node)
    stack['top'] = node.get_next(prev_first_node)
    stack['size'] -= 1

    return data
        



def push(stack, value):
    """
        ->  <-

        @param: stack  ->
        @param: value  ->

        @return: None
    """
    new_node = node.create(value, stack['top'])
    stack['top'] = new_node

    stack['size'] += 1

    

        

# Test(s)
#--------


##astack = create()
##
##push(astack, 1)
##push(astack, 2)
##push(astack, 3)
##push(astack, 4)
##push(astack, 5)
##
##print(astack)
##
##print()
##
##print('[ OUT ] Popped {}'.format(pop(astack)))
##
##print('[ OUT ] Peeked {}'.format(peek(astack)))
##
##
##
##print(is_empty(astack))





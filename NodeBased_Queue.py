import Node as node

# F.I.F.O

def create():
    """
        ->   <-

        @param: None

        @return: an empty queue
    """
    queue = {}
    queue['size'] = 0
    queue['front'] = None
    queue['back'] = None

    return queue





def size(queue):
    """
        ->  <-

        @param: queue  -> a queue created by create()

        @return: Number of data item(s) in the queue
    """
    return queue['size']




def is_empty(queue):
    """
      ->  <-

      @param: queue  -> a queue created by create()

      @return: True if queue is empty, False otherwise
    """
    return queue['size'] == 0




def peek(queue):
    """
        ->  <-

        @param: queue  -> a queue created by create()

        @return: data value in front of the queue without
                 removing it
    """
    assert not is_empty(queue), '[ ERROR ] Peeked into an empty queue'

    front_node = queue['front']
    return node.get_data(front_node)




def dequeue(queue):
    """
        ->  <-

        @param: queue  -> a queue created by create()

        @return: value in front of the queue
    """
    datum = None
    if is_empty(queue):
        return datum    # None is returned
    else:
        # more than 1 data(s)
        firstNode = queue['front']
        datum = node.get_data(firstNode)
        queue['front'] = node.get_next(firstNode)
        queue['size'] -= 1

        if queue['size'] == 0:
            queue['back'] = None
    return datum



def enqueue(queue, value):
    """
        ->  <-

        @param: queue  -> a queue created by create()
        @param: value  -> data to add in queue

        @return: None
    """
    new_node = node.create(value)

    if is_empty(queue):
        queue['front'] = new_node
        queue['back'] = new_node
    else:
        prev_last_node = queue['back']
        node.set_next(prev_last_node, new_node)
        queue['back'] = new_node
    queue['size'] += 1
        

#  Test(s)
#---------

##aqueue = create()
##
##enqueue(aqueue, 5)
##enqueue(aqueue, 4)
##enqueue(aqueue, 3)
##enqueue(aqueue, 2)
##enqueue(aqueue, 1)




































        






















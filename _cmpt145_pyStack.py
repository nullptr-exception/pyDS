#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 02:20:05 2018

@author: nullptr exception

@Module :-> PyStack    ->   Protocol: L.I.F.0

"""

## ConsT
_BACK = -1  # to access the back (end) of the list data(s)


# create a new data structure; Stack that performs the stack-(ing) operation(s)
# In this version, Operation(s) include but are not limited to:
# (0) isValid_type(stack)  -> returns True if stack is a valid stack type False otherwise
# (1) create()      -> creates an empty stack
# (2) is_empty(stack)   -> returns True if the given stack has no data in it
# (3) size(stack)       -> returns the number of data values in the given stack
# (4) push(stack, value) -> adds a given value to the top of the given stack
# (5) pop(stack)    -> remove the value at the front of the given stack and return it
# (6) peek(stack)   -> returns the value at the front of the given stack without remvoing it


# ADT type-check
def isValid_type(stack):
    """
        -> returns True if stack is a valid stack type; False otherwise <-
        
        @param: stack  -> stack ADT to check    (dict)
        
        @return: True if stack is a valid type; False otherwise     (bool)
    
    """
    
    # =============================================================================
    #           -> Nested (Assumed) Private Function <-
    # =============================================================================
    def _get_type(stck):        
        """
            -> SImply return the stack type of t
            
            @param : stck -> type to check  (dict)
            
            @return : -> type of stck   (str)
        """
        
        if type(stck) is dict:
            assert stck['Type'] == 'pyStack', 'TypeError: Expected _pyStack but got {0}'.format(str(type(stck)))
            return stck['Type']
        else:
            assert False, 'TypeError: Expected _pyStack but got {0}'.format(str(type(stck)))
    # =============================================================================
    #         ~ End;
    # =============================================================================
    
    return True if _get_type(stack) == 'pyStack' else False
        



# =============================================================================
#             -> Basic Stack Operation(s) <-
# =============================================================================

def create():
    """
        -> Creates an empty _stack data structure and return it <-
        
        @param : None
        
        @return :  initial _stack created  (dict)
        
    """    
    return {'Data': [], 'Frequency': {}, 'Length': 0, 'Type': 'pyStack'}



def is_empty(stack):
    """
        -> Given a _stack type; return True if _stack is empty. False otherwise <-
        
        @param : _stack  ->  _stack to check   (stack type ->(dict))
        
        @return :  True if empty; False otherwise  (bool)
    """
    if isValid_type(stack):
        return True if stack['Length'] == 0 else False
    else:
        assert False, 'TypeError: Expected _pyStack but got {}'.format(type(stack))
    


def size(stack):
    """
        -> Return the number of data values in _stack <-
        
        @param : _stack: stack data structure to operate on ->  (dict)
        
        @return  : Number of data values in _stack  (int)
                : 0 is returned if no element is in the _stack
    """
    return stack['Length']




def push(stack, value):
    """
        -> Adds a given value to the back of a given _stack  <-
        
        @param : stack  ->  _stack to add value in _stack(dict DT)
        @param : value  -> value to add  (??)
        
        @return :    None
    """
        
    # append the value at the back of the stack. The opposite operation _pop()
    # MUST remove values starting from the back. This obeys the L.I.F.O principle
    getattr(stack['Data'], 'append')(value)  # stack is modified (in-place)
    
    stack['Length'] += 1
    
    # modify the dict rec
    stack['Frequency'][value] = stack['Frequency'].get(value, 0) + 1
    
        


def pop(stack):
    """
        -> Remove the value from the back of _stack and return it <-
        
        @param : _stack  -> stack to remove value from
        
        @return :  value at back of _stack  (??)
    
    """
    try:
        _val = stack['Data'].pop()
        stack['Length'] -= 1
                
        if _val in stack['Frequency']:
        # check how many
            if stack['Frequency'][_val] == 1:     # it's count 1. delete it !!!
                del stack['Frequency'][_val]
            else:   # it's more than 1. decrement it
                stack['Frequency'][_val]  -= 1
        
        return _val     # ( first out )

    except IndexError as e:
        return None
        # ....!

            


def peek(stack):
    """
        -> Returns the value at the back of a given _stack without removing it <-
        
        @param : _stack -> _stack to look into (dict DT)
        
        @return :  value in back of _stack  (??)
    """
    return stack['Data'][_BACK]




# =============================================================================
#       -> Implement basic _Stack Dictionary Operation(s) <-
# =============================================================================
    
def histogram(stack, char='*', show_tab=False):  # returns x,y cords by default
    """
        -> Displays the histogram of a given _stack. Useful for plotting <-
        -> _stack remains unchanged / unmodified <-
        
        @param : _stack  -> _stack to analyze  (dict DT)
        @param : _char  -> choice of character to represent histogram. Default='*'
        @param: _show_tab  -> default = False. A tuple of 2 list(s) is returned
                          : first list is data value(s) pushed to the stack
                          : second list is the number of occurance for each corresponding
                          ... value
                : if _show_tab = True; Nothing is returned and the histogram
                : for each corresponding value is displayed to the console
        
        @return : (~ determinant ~)
    """
    _star = '\t\t ' + ' *' * (len(' [ ~ PyStack : Histogram ~ ] ') // 2)
    _title = '\t\t ' + ' [ ~ PyStack : Histogram ~ ] '
    
    # after all these operations and we have say; 1k+ data, how are we able to represent
    # this using the histogram visually without messing up the output?
    # for the purpose of this project, we will use tripple Qs (QQQ+) to represent 
    # 10+ datas. You are able to see the exact amount at the int tab value(s)
         
    analysis = stack['Frequency']
      
    if show_tab:
        print(); print(_star); print(_title); print(_star); print()                       
        _hist_len = 15
        # no modification to data structure. So we use only the dict type here                        
        print('{0:>16} {1:>24} {2:>25}\
              '.format('_ValUe', '#_oCCuranCe', 'INT_VaL'))
        print('{0:>16} {1:>24} {2:>25}\
              '.format(('*' * len('_VaLue')), ('*' * len('#_oCCuranCe')), '*' * len('INT_VaL')))
        print()
              
        for freq in sorted(analysis):
            if freq is ' ':    # pass on space
                continue
            print('[ OUT ] {0:>5} : {1:>15} [ {2:^4} ] \
                  '.format(freq, ((char * analysis[freq]) if analysis[freq] < _hist_len else 'QQQ+'), analysis[freq]))                
        #...
    else:
        # sequencial mapping
        _sortd_x = []
        _sortd_y = []
        # for now, manually sort the dict. (Hopefully data is not too big)
        # heres one way to sequencially  map an unordered dict key-value pair
        # without losing track of structure
        for i in sorted(analysis):
            getattr(_sortd_x, 'append')(i)
            getattr(_sortd_y, 'append')(analysis[i])
            
        return _sortd_x, _sortd_y



# =============================================================================
#                    ->  TeSt OperaTions <-
# =============================================================================
    
# =============================================================================
#import random as rand
#
#stack = create()
#
#for i in range(1, 30):
#    push(stack, rand.randint(1, 30))
#
#
#histogram(stack, show_tab=True)

# 
# # =============================================================================
# #               -> Text <-
# # =============================================================================
# #print()
# #print('[ OUT ] Original EntRy : [ {0} ]'.format(_s))
# #print()
# #print('[ OUT ] PoPed : [ {0} ] '.format(_pop(_s)))
# #print()
# #print('[ OUT ] PeeKed : [ {0} ]'.format(_peek(_s)))
# #print()
# #print('[ OUT ] EntRy after PeeKed : [ {0} ]'.format(_s))
# #print()
# 
# 
# # =============================================================================
# #                    -> Graph <-
# # =============================================================================
#import matplotlib.pyplot as plt
#x, y = _histogram(stack)
# 
#plt.figure()
# 
#plt.xlabel(' -> Value(s) <-')
#plt.ylabel(' -> N Occurance(s) <-')
# 
# 
#plt.title('[ ~ pyStack Histogram ~ ]')
#plt.grid()
# 
#plt.plot(x, y, 'bo')
# 
#plt.show()
# =============================================================================




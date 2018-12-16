from __future__ import absolute_import
from itertools import ifilter
from robot.libraries.BuiltIn import BuiltIn


def remove_at_index(lst, index):
    """
        Creates a new list which is a copy of the input one with a single element removed from it
    """
    removed = lst[:]
    del removed[index]
    return removed


def match_sequence(lst1_lists, lst2_lists):
    """
        Try to find the best possible match possible that is recursively-contained
        by traying diffenrent combinations of items in list of lists/dictionaries in the best way possible.
    """
    
    # Anything is a superset of an empty set, be it a list of a dictionary
    if len(lst1_lists) == 0: return True
    
    if len(lst1_lists) > len(lst2_lists):
      # There are more elements in subset its supposed superset
      return False
    
    head = lst1_lists[0]
    tail = lst1_lists[1:]

    for index, item in enumerate(lst2_lists):
      if recursively_contains(head, item) and match_sequence(tail, remove_at_index(lst2_lists, index)):
        return True
    return False


def list_recursively_contains(lst1, lst2):
    """
        Recursively-contains logic specifically for lists

    # Use deque for the second lists as we'll be rotating them
    # deque is optimised for pushing/popping on both ends
    """
    from collections import deque
    
    # Group items by their types
    lst1_scalars = list(ifilter(is_scalar_type, lst1))
    lst2_scalars = list(ifilter(is_scalar_type, lst2))
    
    lst1_lists = list(ifilter(lambda x: type(x)==list, lst1))
    lst2_lists = list(ifilter(lambda x: type(x)==list, lst2))
    
    lst1_dicts = list(ifilter(lambda x: type(x)==dict, lst1))
    lst2_dicts = list(ifilter(lambda x: type(x)==dict, lst2))
    
    
    # Ensure scalar values are all contained, fail otherwise
    if lst1_scalars != []:
        if len(lst1_scalars) > len(lst2_scalars): 
            BuiltIn().log("List of scalars has more items than its supposed superset", 'DEBUG')
            return False
        for l1 in lst1_scalars:
            try:
                index = lst2_scalars.index(l1)
                # Remove item 
                lst2_scalars.pop(index)
            except ValueError as e:
                BuiltIn().log("%s is not in the list. we should stop here" % l1)
                return False
            
    # Compare lists and dictionaries together
    return match_sequence(lst1_lists, lst2_lists) and match_sequence(lst1_dicts, lst2_dicts)
    

def is_scalar_type(val):
    """
    Is given value of a simple non-sequence scalar type
    """
    return type(val) in [bool, str, unicode, int, float, complex, long]


def recursively_contains(val1, val2, parent_key=None):
    """
    Returns True if val1 is a subset of val2 both in its items as
    well as the items's items if it's a list or a dictionary.
    Returns False if there are items within val1 but not in val2.
    """
    # If not same data type, fail
    if type(val1) != type(val2):
        if parent_key != None:
            BuiltIn().log("Types %s and %s are NOT the same, for key %s" % (type(val1), type(val2), parent_key))
        else:
            BuiltIn().log("Types %s and %s are NOT the same, for expected value %s" % (type(val1), type(val2), val1))
        return False

    # If simple scalar type, just compare values
    if is_scalar_type(val1):
        is_contained = val1==val2
        if not is_contained: BuiltIn().log("Scalar values aren't equal", 'DEBUG')
        return is_contained
    
    # If dictionary type
    elif type(val1) is dict:

        # All keys must be in 
        missing_keys = set(val1.keys()) - set(val2.keys())
        if missing_keys != set():
            BuiltIn().log("The keys %s are missing in other dictionary: \n%s" % (missing_keys, val2))
            return False
        else:
        
            # All dictionary's values must be contained in other dictionary with same keys
            # Use lazy evaluation to stop at first failure
            
            # E.g. all( (x for x in [True, True, False, True, True] if print(x)==print()))
            #   will print True, True, False. It won't process the later 2x True.
            return all(( (recursively_contains(v, val2[k], parent_key=k)) for k,v in val1.items() ))
    
    elif type(val1) in [list, set, tuple]:
        BuiltIn().log("About to check list %s" % val1)
        
        return list_recursively_contains(val1, val2)

    else:
        BuiltIn().log("Type not handled", 'WARN')
    BuiltIn().log("Should never get here", 'ERROR')

from recursively_contains import recursively_contains


def is_subset(subset, superset):
    """

    Throws error if any elements or sub-elements of object1 are not present in object2.
    Used in exceptional cases where it's ok to ignore extra fields of a response message.
    See "Dictionary Should Contain Key" for general cases.

    :param subset:
    :param superset:
    :return: nothing if condition is true, raise exception otherwhise.

    >>> subset = [{ 'output': [ { 'data': [{'id':'AAA'}] } ]  }]
    >>> superset = [{},{ 'aaa':[0], 'output': [ { 'data': [{'id':'AAA', 'x':1}] } ]  },{}]
    >>> is_subset(subset, subset)
    >>> is_subset(subset, superset)
    """
    if not recursively_contains(subset, superset):
        raise AssertionError("Not all elements in %s were found in %s" % (subset, superset))
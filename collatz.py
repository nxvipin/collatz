"""
3n+1 Problem

Cycle length of each number is calculated recursively and stored in the hash
table(HT). If any input reduces to a number present in the HT, that values is
used to calculate the cycle length and the recursive function is stopped.
"""

import gevent
collatz_dict = {1 :1}

def memoized_collatz(n):
    """
    Recursively calculates the Collatz cycle length of number 'n'.
    Results are stored in a HT and will be used when called subsequently.
    """
    if collatz_dict.has_key(n):
        return collatz_dict[n]
    elif n%2 == 0:
        collatz_dict[n] = memoized_collatz(n/2) +1
        return collatz_dict[n]
    else:
        collatz_dict[n] = memoized_collatz(3*n+1) + 1
        return collatz_dict[n]

def range_collatz(range):
    """
    For a given range, return the max cycle length of any number in that range.
    Cycle length of each number in that range is calculated *serially*. Range
    is a tuple of form (min, max)
    """
    (Min, Max) = range
    result = map(lambda n : memoized_collatz(n),
                 xrange(Min, Max+1))
    return max(result)

def p_range_collatz(range):
    """
    For a given range, return the max cycle length of any number in that range.
    Cycle length of each number in that range is calculated *concurrently*. Range
    is a tuple of form (min, max)
    """
    (Min, Max) = range
    threads = map(lambda n : gevent.spawn(memoized_collatz, n),
                  xrange(Min, Max+1))
    gevent.joinall(threads)
    return max([thread.value for thread in threads])

def collatz(data):
    """
    Take a list of ranges as input and returns a list of max cycle length
    for each range in the input list. Result for each range is calculated
    *serially* and cycle for each number in a range is calculated *serially*.
    """
    return map(range_collatz, data)

def p_collatz(data):
    """
    Take a list of ranges as input and returns a list of max cycle length
    for each range in the input list. Result for each range is calculated
    *concurrently* and cycle for each number in a range is calculated *serially*.
    Concurrent calculation for each number in a range was also tried but it was
    found to be too slow.
    """
    threads = map(lambda range : gevent.spawn(range_collatz, range), data)
    gevent.joinall(threads)
    return [thread.value for thread in threads]

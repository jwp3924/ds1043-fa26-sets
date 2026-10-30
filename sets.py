"""sets

Some introductory exercises using sets and dictionaries

"""
import sys
import timeit
import random
from string import ascii_letters

random.seed()

# We've used dictionaries already, but we haven't discussed sets. You can think
# of sets as a dictionary that only has keys, no values. Why would we do this?

# Let's do an experiment. Read the following function to get an idea of what we're
# testing. Then run it a few times to see what the results are. Finally, set a
# breakpoint at the point indicated and hit 'debug' to take a look at our haystacks.
# Do this by clicking the line number of the specified line in PyCharm and clicking
# the green "bug" icon.

def find_needle() -> None:
    """Demonstration of the relative performance of sets and lists for searching"""
    haystack_set = set(''.join(random.choice(ascii_letters) for _ in range(6))
                       for _ in range(1000000))
    haystack_set.add('Needle')
    haystack_list = list(haystack_set)
    # Set a breakpoint on the following line and take a look at the values of
    # haystack_set and haystack_list
    print(f"| data structure | size    |\n" + \
          f"| :------------- | ------: |\n" + \
          f"| haystack_list  | {len(haystack_list):>7n} |\n" + \
          f"| haystack_set   | {len(haystack_set):>7n} |\n")
    size_ratio = round(sys.getsizeof(haystack_set) / sys.getsizeof(haystack_list))
    print(f'A set haystack uses {size_ratio} times the memory of a list haystack')
    list_time = timeit.timeit("'Needle' in haystack_list",
                              globals=locals(), number=100)
    set_time = timeit.timeit("'Needle' in haystack_set",
                             globals=locals(), number=100)
    print(f'Searching a list takes {round(list_time / set_time):,} times ' +\
    'the time it takes to find an element in a set')

# A classic application of dictionaries is as a store of previously completed work.
# This is exceptionally helpful when computation is costly (either directly or
# because it requires a slow resource, like a network request) or repetitive.

# A toy example of repetitive computation is a recursive implementation of
# calculating a given Fibonacci number:
def fib(n: int) -> int:
    "Calculate the n-th member of the Fibonacci Sequence"
    if n < 0:
        raise ValueError("The Fibonacci Sequence is not defined for n < 0")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Rewrite this function to use a dictionary to cache repetitive work
def memo_fib(n: int, memo: dict) -> int:
    "Calculate the n-th member of the Fibonacci Sequence, but save work using a dictionary"
    if n in memo:
        return memo[n]
    if n < 0:
        raise ValueError("The Fibonacci Sequence is not defined for n < 0")
    if n < 2:
        return n
    memo[n] = memo_fib(n - 1, memo) + memo_fib(n - 2, memo)
    return memo[n]

# Run an experiment using the debugger to compare the stack usage of the basic
# recursive version with your version that uses a dictionary. Set a breakpoint on
# the first line of the function and watch the stack view on the left side of the
# debugger tool window as you step through the execution of the function.

# You will want to modify the if name main block to run `fib` and `memo_fib` for debugging

if __name__ == '__main__':
    find_needle()
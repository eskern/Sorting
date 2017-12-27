#!/usr/bin/python
import math
import sys

def countSort(A):
    # use sys.maxsize to get the largest integer value
    ## WORKS FOR PYTHON3
    # if using Python2, use sys.maxint
    maximum = -sys.maxsize - 1
    for i in range(len(A)):
        # get max value so we can make an appropriate size array (count)
        maximum = max(maximum, A[i])

    # good ol' initialization
    # count is as long as the maximum number's value
    # where each index represents a number potentially in A
    # each index holds the number of occurrences of the index found in A
    # sort is as long as the number of elements found in A
    count = [0 for i in range(maximum+1)]
    sort = [0 for i in range(len(A))]

    # for each element in the given array A
    for x in A:
        # count[x] holds the number of occurences of x in A
        count[x] += 1

    curr = 0

    # for all elements in count[]
    for i in range(len(count)):
        # the number in question is equal to what we're looking at in count[i]
        # note that num = count[i] is the number of occurrences of the index i
        # curr acts as a counting index for sort[]
        num = count[i]
        for j in range(num):
            # if count[i] holds a value of 0 (i.e. there's no occurrence)
            # no need to worry; "skip" over this loop
            sort[curr] = i
            curr += 1
            
    return sort



if __name__ == '__main__':
    print("Type in any amount of integers separated by a space.")
    print("When done, press 'enter' and then 'control'+'d'")
    print("Example: 1 5 2 6 3 7 4 8")
    input = sys.stdin.read()
    a = list(map(int, input.split()))
    print(countSort(a))

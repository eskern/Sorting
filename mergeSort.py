#!/usr/bin/python
import math
import sys

# We are basically breaking an array into subarrays until len(subarray) == 1
# From that point, we merge the subarrays with the merge(b, c) function
# Doing this builds new (sub)arrays that are sorted, culminating into the sorted array
# To better visualize the algorithm, think of it this way:
### We recursively call mergeSort(A) until we have only one element in a subarray of A
### At the start of the algorithm, we end up with b being assigned to the very first element in A
### because it is always in the left-half of the subarray of A
### Thus, we move on to assigning c to an element of A; that element is assigned to the previous recursion's midpoint (mid)
### which is in the index to the right of our first b
### We merge(b, c) these two subarrays, thus sorting them into a two-element subarray
### But what about the other elements?! After merging the first subarray, we sort (via merge(b, c)) the other subarrays
### thanks to that c variable we left hanging in earlier recursions, so when we try to assign a variable to c,
### it is clear we call mergeSort(A) again, this time with the upper half of the subarray
### This upper half is split into left and right halves, reducing to a single element for b and eventually c
### This process continues until we have a fully sorted list!
# Hopefully this explanation helped, as I tried to explain it in plain English rather than in algorithm-speak,
# but there are several visualizations online that help make more sense out of this
# I recommend this one: https://www.youtube.com/watch?v=_r0gV2hQYf0

# TL;DR MERGESORT ALL THE HALVES-OF-HALVES-OF-HALVES-OF-HALVES....... until done!

def mergeSort(A):
    if len(A) == 1:
        # Base case; if the length of the array is 1,
        # return the array
        return A
    
    # Gets midpoint of given array
    mid = math.floor(len(A)/2)
    
    # Left-half of given array;
    # Recursively builds said array
    b = mergeSort(A[0:mid])
    
    # Right-half of given array
    # Recursively builds said array
    c = mergeSort(A[mid:])
    
    # When base-case reached for both halves of orignal array,
    # merge the two arrays into a sorted array
    return merge(b, c)
    
def merge(B, C):
    # Empty array that will hold the new sorted array
    x = []

    # While there are still elements in both array B and C
    while len(B) > 0 and len(C) > 0:

        # Variables m and n point to first element of
        # array B and C respectively
        m, n = B[0], C[0]

        # If first element in B <= element in C
        if m <= n:
            # add element m to x
            x.append(m)
            # delete that element from B; decreases len(B)
            del B[0]
        else:
            # add element n to x
            x.append(n)
            # delete that element from C; decreases len(C)
            del C[0]

    # If B still has elements in it (and therefore C has none)
    if len(B) > 0:
        # Append the rest of the elements in B to array x;
        # remaining elements in B were > greatest value in C
        for i in B:
            x.append(i)

    # If C still has elements in it (and therefore B has none)
    elif len(C) > 0:
        # Append the rest of the elements in C to array x;
        # remaining elements in C were > greatest value in B
        for i in C:
            x.append(i)
    return x
              
if __name__ == '__main__':
    print("Type in any amount of integers separated by a space.")
    print("When done, press 'enter' and then 'control'+'d'")
    print("Example: 1 5 2 6 3 7 4 8")
    input = sys.stdin.read()
    a = list(map(int, input.split()))
    print(mergeSort(a))

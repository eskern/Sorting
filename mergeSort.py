#!/usr/bin/python
import math
import sys

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

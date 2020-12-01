from datetime import datetime
from timeit import default_timer as timer

def mergeSort(list):
    if len(list) > 1:
        m = len(list)//2                          # Determine the midpoint of the list
        Left = list[:m]                           # Then split the list into two halves
        Rght = list[m:]                           # and then call mergeSort on the halves
        mergeSort(Left)
        mergeSort(Rght)

        i,j,k=0,0,0

        while len(Left) > i and len(Rght) > j:      # To sort, add the split lists back together
            if Left[i] > Rght[j]:                   # lower values first
                list[k] = Rght[j]                   # Keep track of three separate iterators:
                j+=1                                # i for Left, j for Rght, and k for list
            else:
                list[k] = Left[i]
                i+=1
            k+=1
        while i < len(Left):                        # At one point, the first loop will end and
            list[k] = Left[i]                       # that could happen before one of the arrays are empty
            i+=1                                    # Empty the remaining values into the list
            k+=1
        while j < len(Rght):
            list[k] = Rght[j]
            j+=1
            k+=1

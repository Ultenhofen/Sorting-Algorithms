num_of_vals = 100000

def insertionSort(list):
    for i in range(1, len(list)):           # Starting with the second value,
        x = list[i]                       # Compare the selected value with
        j = i-1                             # the values that come before it
        while j >= 0 and x < list[j] :    # Then place the selected value in
                list[j + 1] = list[j]       # the first index that it is less than
                j -= 1                      # To sort Greatest to Least, flip the '<'
        list[j + 1] = x

def mergeSort(list):
    if len(list) > 1:
        mid = len(list)//2                          # Determine the midpoint of the list
        Left = list[:mid]                           # Then split the list into two halves
        Rght = list[mid:]                           # and then call mergeSort on the halves
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

def quicksort(list):
    l = 0                                           # Set low and high positions
    h = len(list)-1
    if l < h:
        part = partition(list,l,h)
        quicksort_helper(list, l, part-1)           # This is a recursive solution
        quicksort_helper(list,part+1,h)

def partition(list , l , h):
    pivot = list[h]                                 # Set the pivot
    i = l-1                                         # Determining pivots can be done
                                                    # in multiple ways
    for j in range(l,h):
        if list[j] < pivot:
            i=i+1
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    temp = list[i+1]
    list[i+1] = list[h]
    list[h] = temp
    return(i+1)

def quicksort_helper(list,l,h):
    if l < h:
        part = partition(list,l,h)
        quicksort_helper(list, l, part-1)
        quicksort_helper(list,part+1,h)

# Main
# generate random integer values
from random import seed
from random import randint
from datetime import datetime
from timeit import default_timer as timer
# seed random number generator
d = datetime.now()
seed(d)
value = []
# generate some integers
for i in range(num_of_vals):
	value.append(randint(0, 50000))
ins_n = value
mrg_n = value
qs_n = value

# Call insertionSort
start = timer()
insertionSort(ins_n)
e_t = timer() - start
# Call mergeSort
start = timer()
mergeSort(mrg_n)
e_t1 = timer() - start
start = timer()
insertionSort(ins_n)
e_t2 = timer() - start
delta = e_t - e_t1
print("Insertion Sort time = ", e_t)
print("Merge Sort time = ", e_t1)
print("Delta = ", delta)
print("Quick Sort time = ", e_t2)
# Clear insert.out
open("insert.out" , "w").close()
file = open("insert.out" , "a+")

# Fill insert.out with the sorted values
for i in range(len(ins_n)):
    file.write(str(ins_n[i]) + " ")
file.close()

# Clear merge.out
open("merge.out" , "w").close()

file = open("merge.out" , "a+")
# Fill merge.out with the sorted values
for i in range(len(mrg_n)):
    file.write(str(mrg_n[i]) + " ")
file.close()

# Clear quick.out
open("quick.out" , "w").close()
file = open("quick.out" , "a+")

# Fill quick.out with the sorted values
for i in range(len(qs_n)):
    file.write(str(qs_n[i]) + " ")
file.close()

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

# Main
# Pull data from data.txt
file = open("data.txt" , "r")
mrg = file.readline()
file.close()
mrg = mrg.split(" ")
mrg_n = []

for i in range(len(mrg)):
    mrg_n.append(int(mrg[i]))

# Call mergeSort
start = timer()
mergeSort(mrg_n)
e_t1 = timer() - start
print(e_t1)

# Clear merge.out
open("merge.out" , "w").close()

file = open("merge.out" , "a+")
# Fill merge.out with the sorted values
for i in range(len(mrg_n)):
    file.write(str(mrg_n[i]) + " ")
file.close()

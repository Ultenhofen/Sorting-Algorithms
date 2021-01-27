from datetime import datetime
from timeit import default_timer as timer

def quicksort(list):
    l = 0
    h = len(list)-1
    if l < h:
        part = partition(list,l,h)
        quicksort_helper(list, l, part-1)
        quicksort_helper(list,part+1,h)

def partition(list , l , h):
    pivot = list[h]
    i = l-1

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
# Pull data from data.txt
file = open("data.txt" , "r")
qs = file.readline()
file.close()
qs = qs.split(" ")
qs_n = []

for i in range(len(qs)):
    qs_n.append(int(qs[i]))

# Call quicksort
start = timer()
quicksort(qs_n)
e_t1 = timer() - start
print(e_t1)
print(qs_n)

# Clear quick.out
open("quick.out" , "w").close()

file = open("quick.out" , "a+")
# Fill quick.out with the sorted values
for i in range(len(qs_n)):
    file.write(str(qs_n[i]) + " ")
file.close()

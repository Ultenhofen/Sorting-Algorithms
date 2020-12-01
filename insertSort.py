from datetime import datetime
from timeit import default_timer as timer

def insertionSort(list):
    for i in range(1, len(list)):           # Starting with the second value,
        x = list[i]                       # Compare the selected value with
        j = i-1                             # the values that come before it
        while j >= 0 and x < list[j] :    # Then place the selected value in
                list[j + 1] = list[j]       # the first index that it is less than
                j -= 1                      # To sort Greatest to Least, flip the '<'
        list[j + 1] = x

# Main
# Pull data from data.txt
file = open("data.txt" , "r")
ins = file.readline()
file.close()
ins = ins.split(" ")
ins_n = []
for i in range(len(ins)):
    ins_n.append(int(ins[i]))

# Call Insetion Sort
start = timer()
insertionSort(ins_n)
e_t = timer() - start
print(e_t)
# Clear insert.out
open("insert.out" , "w").close()
file = open("insert.out" , "a+")

# Fill insert.out with the sorted values
for i in range(len(ins_n)):
    file.write(str(ins_n[i]) + " ")
file.close()

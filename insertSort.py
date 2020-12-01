def insertionSort(list):
    for i in range(1, len(list)):           # Starting with the second value,
        x = list[i]                       # Compare the selected value with
        j = i-1                             # the values that come before it
        while j >= 0 and x < list[j] :    # Then place the selected value in
                list[j + 1] = list[j]       # the first index that it is less than
                j -= 1                      # To sort Greatest to Least, flip the '<'
        list[j + 1] = x

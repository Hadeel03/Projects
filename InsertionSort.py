def InsertionSort(list_sort): # defined a function that a list gets passed into to be sorted
    for i in range(1, len(list_sort)):
        key = list_sort[i] # takes a copy from list_sort[1] to be compared
        j = i - 1 # stores the value of the previous index
        while (j>= 0 and list_sort[j] > key):
            list_sort[j+1] = list_sort[j]
            j = j -1
        list_sort[j+1] = key
    print (list_sort)

def main():
    my_list = [3, 5, 7, 8, 1, 9]
    InsertionSort(my_list)

main()
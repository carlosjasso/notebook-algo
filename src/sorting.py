def bubble(arr: list[int]) -> list[int]:
    n = len(arr) # take the length of the array to wotk with
    for i in range(n): # traverse through all elements in array by index (0~n)
        swapped = False # Optimization to prevent unnecesary iterations
        for j in range(0, n - i - 1): # go from index 0 to n - alreadySortedElements - 1
            if arr[j] > arr[j + 1]: # if current number is greater then the one in the next index
                arr[j], arr[j + 1] =  arr[j + 1], arr[j] # swap current number with next one
                swapped = True
        if not swapped:
            break
    return arr

def insert(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        j = i
        while j >= 0 and j < (len(arr) - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                j -= 1
            else:
                break
    return arr

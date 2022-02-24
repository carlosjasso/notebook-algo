class Sorting:
    def bubbble_sort(arr: list[int]) -> list[int]:
        result = arr.copy() # Copy the entered array for it not to be modified
        n = len(result) # take the length of the array to wotk with
        for i in range(n): # traverse through all elements in array by index (0~n)
            swapped = False # Optimization to prevent unnecesary iterations
            for j in range(0, n - i - 1): # go from index 0 to n - alreadySortedElements - 1
                if result[j] > result[j + 1]: # if current number is greater then the one in the next index
                    result[j], result[j + 1] =  result[j + 1], result[j] # swap current number with next one
                    swapped = True
            if not swapped:
                break
        return result

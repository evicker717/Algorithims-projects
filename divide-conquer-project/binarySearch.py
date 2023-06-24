def binarySearch(arr, searchval):
    min = 0
    max = len(arr) -1
    med = 0
    while min <= max:
        med = (max + min) // 2
        if arr[med]< searchval:
            min = med + 1
        elif arr[med]>searchval:
            max = med - 1
        else:
            return med 
        
    return -1


arr = [ 2, 3, 4, 10, 40 ]
searchval = 10
 
result = binarySearch(arr, searchval)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
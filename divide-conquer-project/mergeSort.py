
def mergeSort(arr):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        mergeSort(left)
        mergeSort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i+=1

            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k]= left[i]
            i+=1
            k+=1
        while j< len(right):
            arr[k] = right[j]
            j +=1
            k +=1
 
    return arr


def tests():
    arr1 = [ 40, 2, 10, 6, 20 ]
    result1 = mergeSort(arr1)
    print(result1)
    arr2 = [ 40 ]
    result2 = mergeSort(arr2)
    print(result2)
    arr3 = [ 40, 2, 10, 6, 20, 40, 90, 80 , 6 ,23 ,22 ,77 ,18, 34 ,73 ,62, 93 ] 
    result3 = mergeSort(arr3)
    print(result3)

tests()
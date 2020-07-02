def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [151,5,21,52,100]
print(bubbleSort(arr))
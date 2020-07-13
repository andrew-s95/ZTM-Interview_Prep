def mergeSort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(mergeSort(left),mergeSort(right))

def merge(left, right):
    result = []
    leftidx = 0
    rightidx = 0
    while leftidx < len(left) and rightidx < len(right):
        if left[leftidx] < right[rightidx]:
            result.append(left[leftidx])
            leftidx += 1
        else:
            result.append(right[rightidx])
            rightidx += 1
    return result + left[leftidx:] + right[rightidx:]

x = mergeSort([1,23,4,5,3])
print(x)
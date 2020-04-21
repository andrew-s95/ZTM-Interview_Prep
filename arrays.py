#Reverse a string
def reverseString(str):
    if len(str) == 0:
        return "There is no string to reverse"
    index = len(str)
    backwards = []
    while index > 0:
        backwards += str[index - 1]
        index -= 1
    return "".join(backwards)

print(reverseString(""))

#Merge two sorted arrays
def mergeTwo(arr1, arr2): 
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    merged = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            merged.append(arr2[j])
            j += 1
    return merged+arr[i:]+arr[j:] #in order to go through the entirety of both arrays

print(mergeTwo([],[2,4,5,6]))

#Two Sum w/ Arrays
def twoSum(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
            return "No pairs return sum"

print(twoSum([1,2,3,6,7],3))

def twoSum2(arr, target):
    complementMap = {}
    for i in range(len(arr)):
        num = arr[i]
        complement = target - num
        if num in complementMap:
            return [complementMap[num], i] #or True (depending on what wants to be returned)
        else:
            complementMap[complement] = i 

print(twoSum2([1,2,3,6,7],3))

#Max Subarray
def maxSubArray(self, nums: List[int]) -> int:   
    if len(nums) == 0:
        return 0
    res = nums[0]
    currMax = 0
    for n in nums:
        if currMax + n < 0:
        currMax = 0
        res = max(n, res)
        else:
        currMax += n
        res = max(currMax, res)
    return res
            



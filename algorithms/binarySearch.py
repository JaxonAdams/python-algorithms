import math

# This is a simple binary search algorithm.
# Dataset defined here
numberList = [1,2,4,7,9,13,16,21,23,24,25,29,30,35,70,90]

def binarySearch(arr, num, start, end):
    # Return -1 if num not found in array
    if (start > end):
        return print('Number not found in array.')

    mid = math.floor((start + end) / 2)

    if (arr[mid] == num):
        print('Found number: ')
        print(num)
        print('Found at index: ')
        print(mid)
    elif (arr[mid] > num):
        return binarySearch(arr, num, start, mid - 1)
    elif (arr[mid] < num):
        return binarySearch(arr, num, mid + 1, end)

binarySearch(numberList, 21, 0, len(numberList) - 1)
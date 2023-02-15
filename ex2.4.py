import json
import sys
import time
import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    mid = (start + end) // 2
    pivot = sorted([array[start], array[mid], array[end]])[1]
    if pivot == array[start]:
        p = start
    elif pivot == array[mid]:
        p = mid
    else:
        p = end
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[p], array[high] = array[high], array[p]
    return high


def sort_data(data):
    start = time.time()
    for sub_list in data:
        func1(sub_list, 0, len(sub_list)-1)
    end = time.time()
    return end - start

if __name__ == "__main__":
    with open('Q2.json') as json_file:
        data = json.load(json_file)
        
        # Keep track of timing results
        x = []
        y = []
        for i in range(1, len(data)+1):
            sub_data = data[:i]
            sorting_time = sort_data(sub_data)
            x.append(len(sub_data))
            y.append(sorting_time)
          
        
        # Plot the results
        plt.plot(x, y)
        plt.xlabel('Number of elements')
        plt.ylabel('Time (s)')
        plt.title('Sorting Time Result')
        plt.show()

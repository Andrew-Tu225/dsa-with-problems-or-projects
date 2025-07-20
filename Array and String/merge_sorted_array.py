"""
merge two sorted arrays into one sorted array

ex:
input:
array1 = [1,3,7,9,12,15,16]
array2 = [1,5,6,8,13,15]

output:
[1, 1, 3, 5, 6, 7, 8, 9, 12, 13, 15, 15, 16]

"""
import heapq
def merge_sorted_array(sorted_array1:list[int], sorted_array2:list[int]) -> list[int]:
    merged_array = []
    while len(sorted_array1) != 0 and len(sorted_array2) != 0:
        if sorted_array1[0] >= sorted_array2[0]:
            merged_array.append(sorted_array2[0])
            sorted_array2.pop(0)
        else:
            merged_array.append(sorted_array1[0])
            sorted_array1.pop(0)
    
    if len(sorted_array1) == 0:
        for i in sorted_array2:
            merged_array.append(i)
    elif len(sorted_array2) == 0:
        for i in sorted_array1:
            merged_array.append(i)
    return merged_array


def k_way_merge(sorted_arrays:list[list[int]]) -> list[int]:
    minHeap = []
    for array in sorted_arrays:
        heapq.heappush(minHeap, (array[0], array, 0))

    result = []
    while minHeap:
        smallest = heapq.heappop(minHeap)
        result.append(smallest[0])
        array, index = smallest[1:]
        if index < len(array) - 1:
            heapq.heappush(minHeap, (array[index+1], array, index+1))
    return result



if __name__ == "__main__":
    sorted_array1 = [1,3,7,9,12,15,16]
    sorted_array2 = [1,5,6,8,13,15]

    sorted_arrays = [[1,3,7,9,12,15,16], [1,5,6,8,13,15], [3,5,6,7,8,12,20]]

    print("output from two pointers merge: ", merge_sorted_array(sorted_array1, sorted_array2))
    print("output from k way merge: ", k_way_merge(sorted_arrays))

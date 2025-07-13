"""
rotate the array left by k elements

ex:
inputs: 
array = [1,2,3,4,5,6,7]
k = 3

output:
[4, 5, 6, 7, 1, 2, 3]

thought process:
1. select the first k elements from the start
and move them to the end of array
time complexity: O(n), space complexity: O(n)

2. juggling algorithm: determine the num of cycles through
gcd(length of array, k), and we update current element to element 
at index (i+d)%n until the start index is the same as next index
time complexity:O(n), space complexity: O(1)
"""
import math

def roatate_array(array:list[int], k:int):
    n = len(array)
    k%=n

    temp = [0]*n

    for i in range(n-k):
        temp[i] = array[k+i]
    for i in range(k):
        temp[n-k+i] = array[i]

    for i in range(len(array)):
        array[i] = temp[i]
    return array

def rotate_array_with_juggling(array:list[int], k:int):
    n = len(array)
    num_cycles = math.gcd(n, k)

    for i in range(num_cycles):
        start_index = i
        start_element = array[i]

        while True:
            next_index = (start_index+k) % n
            if next_index == i:
                break

            array[start_index] = array[next_index]
            start_index = next_index
        
        array[start_index] = start_element

    return array

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7]
    k = 3

    print("rotated array from rotate array function: ", roatate_array(array.copy(), k))
    print("rotated array from juggling algorithm", rotate_array_with_juggling(array.copy(),k))
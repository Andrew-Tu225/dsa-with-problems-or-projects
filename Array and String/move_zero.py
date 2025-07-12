"""
Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

input: [1,2,4,0,1,2,3,0,2,0,0,3]
output: [1,2,4,1,2,3,2,3,0,0,0,0]

-----------------------------------------------------------------
initial thought process:
to maintain the order of non-zero element, we need to keep
track of the first zero index in the array(the index to swap).
So find the index of first zero and update it in every swap

more optimized solution(only do it in one pass):
traverse the array once and update the zero_index when iterating element 
is not zero and do the swap when zero_index is different from iterating index
"""


def move_zero(array:list[int]) -> list[int]:
    if 0 not in array or array.index(0)==len(array)-1:
        return array
    else:
        swap_index = array.index(0)
        iterating_index = swap_index + 1

        while iterating_index < len(array):
            if array[iterating_index] == 0:
                iterating_index += 1
            else:
                array[swap_index], array[iterating_index] = array[iterating_index], array[swap_index]
                swap_index += 1
                iterating_index += 1
        return array
    
def optimized_move_zero(array:list[int]):
    zero_index = 0
    for i in range(len(array)):
        if array[i] != 0:
            if i != zero_index:
                array[zero_index], array[i] = array[i], array[zero_index]
            zero_index += 1
    return array


if __name__=="__main__":
    array = [1,2,4,0,1,2,3,0,2,0,0,3]
    print("output from move_zero function: ", move_zero(array))
    print("output from optimized_move_zero function: ", optimized_move_zero(array))

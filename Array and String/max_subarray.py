"""
maximize the subarray sum:
find a subarray that gives maximum sum

input:
[2, 3, -8, 7, -1, 2, 3]

output:
11

thought process:
using Kadane's algorithm, which track of maximum sum(result) and 
current max continuous sum(current_max). The algorithm decides whether
to add current element to subarray or restart a new subarray from this 
element, and the current_max is compared with result to keep the maximum sum
updated.

"""

def max_subarray(array:list[int]) -> int:
    current_max = 0
    result = 0

    for i in array:
        current_max = max(current_max + i, i)
        result = max(result, current_max)
    return result



if __name__=="__main__":
    array = [2, 3, -8, 7, -1, 2, 3]
    print(max_subarray(array))
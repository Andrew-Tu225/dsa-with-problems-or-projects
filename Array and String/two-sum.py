"""
given the array and target, find the index of two elements in
array that add up to the target

ex:
input:
array = [1,2,3,5,3,6,7,9,-1,-3]
target = 6

output:[0,3]
"""

def two_sum(array:list[int], target:int) -> list[int]:
    map = dict()
    for i, val in enumerate(array):
        if val in map:
            return [map[val], i]
        else:
            complement = target - val
            map[complement] = i
    return []

"""
find all unique index pair for two sum problem
(discard the duplicate index pair)
"""

def two_sum_with_all_pairs(array:list[int], target:int):
    map = dict()
    results = []
    for i, val in enumerate(array):
        if val in map:
            results.append((map[val], i))
        else:
            complement = target - val
            map[complement] = i
    return results

if __name__ == "__main__":
    array = [1,2,3,5,3,6,7,9,-1,-3]
    target = 6
    print("two sum output: ", two_sum(array, target))
    print("two sum with all index pairs output: ", two_sum_with_all_pairs(array, target))
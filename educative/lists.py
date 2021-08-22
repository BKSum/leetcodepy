from typing import List
from functools import reduce

def merge_lists(lst1, lst2):
    # Write your code here
    mergedList = []
    while True:
        if lst1 and lst2:
            if lst1[0] < lst2[0]:
                item = lst1.pop(0)
                mergedList.append(item)
            else:
                item = lst2.pop(0)
                mergedList.append(item)
        elif lst1 and not lst2:
            mergedList.extend(lst1)
            return mergedList
        elif not lst1 and lst2:
            mergedList.extend(lst2)
            return mergedList
        else:
            return mergedList


def multiply_list(lst: List[int]) -> int:
    return reduce(lambda x, y: x*y, lst)


def find_product(lst):
    results = []
    for i in range(len(lst)):
        tmpList = lst[:i] + lst[i+1:]
        print(tmpList)
        results.append(multiply_list(tmpList))
    return results


def find_second_maximum(lst):
    # Write your code here
    if not lst or len(lst)<2:
        return None
    lst.sort()
    return lst[-2]

def right_rotate_once(lst):
    if lst and len(lst)==1:
        return lst
    if not lst:
        return lst
    last = [lst[-1]]
    shift_right = lst[0:len(lst)-1]
    last.extend(shift_right)
    return last


def right_rotate(lst, k):
    for x in range(k):
        lst = right_rotate_once(lst)
    return lst

lst = [4,2,1,5,0]

x = right_rotate(lst)
print('final: ' + str(x))

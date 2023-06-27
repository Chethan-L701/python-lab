# MergeSort : divides the array | list into 2 parts.
import time


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid: int = len(arr) // 2
    left: list = merge_sort(arr[:mid])
    right: list = merge_sort(arr[mid:])
    return merge(left, right)


# Merge Algorithm this fn will merge the 2 divided array into a single array lexicographically
# Use it with only Mergesort Algo
# !! do not try to merge two randomized arrays you may get unexpected result or Exception.
def merge(arr1: list, arr2: list) -> list:
    merged_arr: list = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] < arr2[0]:
            merged_arr.append(arr1.pop(0))
        elif arr2[0] < arr1[0]:
            merged_arr.append(arr2.pop(0))
        else:
            merged_arr.append(arr2.pop(0))
            merged_arr.append(arr1.pop(0))
    while len(arr2) > 0:
        merged_arr.append(arr2.pop(0))
    while len(arr1) > 0:
        merged_arr.append(arr1.pop(0))

    return merged_arr


# Insertion Sort
def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


n: int = int(input("Enter the size of the array to sort : "))
print("Enter the elements : ")
input_list: list = [int(input(f"arr[{i}] : ")) for i in range(0, n)]

mt_start = time.time_ns()
merge_sorted = merge_sort(input_list)
mt_end = time.time_ns()

ins_start = time.time_ns()
isorted = insertion_sort(input_list)
ins_end = time.time_ns()

print(f"The merge sorted list is : {merge_sorted}\nTime taken : {(mt_end - mt_start)} ns")
print(f"The insertion sorted list is : {isorted}\nTime taken : {(ins_end - ins_start)} ns")

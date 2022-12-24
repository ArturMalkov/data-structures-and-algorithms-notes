# O(m+n) time complexity
def merge_sorted_arrays(list1: list[int], list2: list[int]) -> list[int]:
    sorted_array = []
    l1_pointer = l2_pointer = 0

    while l1_pointer < len(list1) and l2_pointer < len(list2):
        if list1[l1_pointer] < list2[l2_pointer]:
            sorted_array.append(list1[l1_pointer])
            l1_pointer += 1
        else:
            sorted_array.append(list2[l2_pointer])
            l2_pointer += 1

    if l1_pointer < len(list1):
        sorted_array.extend(list1[l1_pointer:])
    elif l2_pointer < len(list2):
        sorted_array.extend(list2[l2_pointer:])

    return sorted_array


print(merge_sorted_arrays([1, 3, 4, 5, 7], [1, 2, 4, 6, 8]))


# less optimized approach
def merge_sorted_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    merged_list = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0

    for k in range(len(merged_list)):
        if first1 != len(nums1) and (first2 == len(nums2) or nums1[first1] < nums2[first2]):
            merged_list[k] = nums1[first1]
            first1 += 1
        else:
            merged_list[k] = nums2[first2]
            first2 += 1

    return merged_list


print(merge_sorted_arrays([1, 3, 4, 5, 7], [1, 2, 4, 6, 8]))

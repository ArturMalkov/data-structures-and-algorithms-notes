"""
Time complexity - O(N)
Space complexity - O(M) - where M is the number of different elements
"""

my_list = [1, 3, 4, 5, 7, 7, 7, 3, 2, 2, 5, 9, 6, 4, 3]


# frequency analysis
frequency_list = [0] * len(my_list)
print(frequency_list)

for i in my_list:
    frequency_list[i] += 1

print(frequency_list)

# for i in range(len(my_list)):
#     frequency_list[]


# my_dict = {}
#
# for i in my_list:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
#
# print(my_dict)

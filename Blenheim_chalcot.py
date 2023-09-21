# def is_palindrom(string: str) -> bool:
#     right_idx = len(string)
#     left_idx = 0
#     palindrome = True
#     while right_idx <= left_idx:
#         if string[right_idx] == string[left_idx]:
#             right_idx -= 1
#             left_idx += 1
#         else:
#             palindrome = False
#     return palindrome
#


################################################################
# array = [(, [, {, {, (, }, }, )]

# def balenced(array: list) -> bool:
#     count = {}
#     for item in array:
#         if item not in count:
#             count[item] = 1
#         else:
#             count[item] = count[item] + 1
#     return count


################################################################
# array = [2, 4, 3, 7, 5, 9, 1]
#
# def is_leader(array: list) -> list:
#     leaders = []
#     for idx, item in enumerate(array[0:-1]):
#         if item < array[idx+1]:
#             leaders.append(array[idx+1])
#     leaders.append(array[-1])
#     return leaders
#
# print(is_leader(array))


#############################################################
# array = [2, 4, 3, 7, 5, 9, 1]
# def get_min_max(array: list):
#     min = array[0]
#     max = array[0]
#     for num in array:
#         if num > max:
#             max = num
#         elif num < min:
#             min = num
#     return min, max
#
# get_min_max(array)


##################################################

# string = "my name is adam"

# def check_count(string: str, target: str) -> int:
#     for idx in range(len(string) - len(target) + 1):
#         if

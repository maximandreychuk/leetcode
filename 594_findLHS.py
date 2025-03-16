def findLHS(nums):
    # r = []
    # for i in range(len(nums)):
    #     current = [nums[i]]
    #     for j in range(i+1, len(nums)):
    #         if abs(nums[i] - nums[j]) == 1:
    #             current.append(nums[j])
    #     if len(r) < len(current):
    #         r = current
    # return r
    longest_harmonious_subsequence_length = 0
    for i in range(len(nums)):
        current_harmonious_subsequence_length = 1  # Начинаем с 1, т.к. nums[i] - уже элемент
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == 1:  # Проверка на гармоничность
                current_harmonious_subsequence_length += 1
        longest_harmonious_subsequence_length = max(longest_harmonious_subsequence_length, current_harmonious_subsequence_length)
    return longest_harmonious_subsequence_length


print(findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
print(findLHS([1,2,3,4]))


# r = p = []
# counter = i = 0
# while counter < len(nums):
#     nums[0], nums[i] = nums[i], nums[0]
#     p.append(nums[0])
#     for j in range(1, len(nums)):
#         if nums[0] + 1 == nums[j] or nums[j] == nums[0]:
#             p.append(nums[j])
#     if len(r) < len(p):
#         r = p
#     counter += 1
#     i += 1
#     p = []
# return r


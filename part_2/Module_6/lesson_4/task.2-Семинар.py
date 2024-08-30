import random

nums_1 = {29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1}

nums_2 = {16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21}
print(min(nums_1))
print(min(nums_2))
print()
print()
print(list(nums_1)[random.randint(0, len(nums_1))])
print(list(nums_2)[random.randint(0, len(nums_2))])
print()
print()
summ = nums_1 | nums_2
print(nums_1 & nums_2)
print(nums_2 - nums_1)
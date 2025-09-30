"""
Dado un listado de números, encuentra el SEGUNDO más grande
"""


def sec_max(nums: list) -> float:

    if len(nums) < 2:
        raise ValueError("List must have 2 or more elements")

    nums.sort()

    if nums[0] == nums[-1]:
        raise ValueError("All items in the list are equal")

    for i in range(-1, -len(nums), -1):
        if nums[i-1] != nums[i]:
            return nums[i-1]

    return nums[-1]


print(sec_max([5, 8, 3, 9, 1]))
print(sec_max([8, 5, 8]))
print(sec_max([2, 2, 2]))
print(sec_max([2]))
print(sec_max([]))

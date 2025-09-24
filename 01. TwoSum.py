def twoSum(nums: list[int], target: int) -> list[int]:
    output = []
    for i in range(len(nums)):
        if output != []:
            if nums[output[0]] + nums[output[1]] == target:
                break
        else:
            for n in range(len(nums)):
                # if nums[i] != nums[n]:
                if nums[i] + nums[n] == target:
                    output.append(i)
                    output.append(n)
    return output


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))


# def test(nums):
#     for i in range(len(nums)):
#         print(nums[i])


# print(test([2, 3, 6]))

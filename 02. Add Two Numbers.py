# def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
def addTwoNumbers(l1, l2):
    outputL1 = []
    outputL2 = []
    for i in range(len(l1) - 1, -1, -1):
        outputL1.append(l1[i])
    for i in range(len(l2) - 1, -1, -1):
        outputL2.append(l2[i])

    num1 = ""
    num2 = ""

    for i in range(len(outputL1)):
        num1 = num1 + str(outputL1[i])
    for i in range(len(outputL2)):
        num2 = num2 + str(outputL2[i])

    numSum = int(num1) + int(num2)
    numSum = str(numSum)
    returnVal = []
    for i in range(len(numSum)):
        returnVal.append(numSum[i])
    return returnVal


nums = [4, 0, 7]
nums2 = [2, 2, 5]
output = []

# for i in range(len(nums) - 1, -1, -1):
#     output.append(nums[i])

# print(output)

print(addTwoNumbers(nums, nums2))

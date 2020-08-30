# 第一次提交的代码，代码比较繁琐
def plusOne(digits: List[int]) -> List[int]:
    divisor = 0
    for i in range(len(digits) - 1, -1, -1):
        if divisor == 1:
            digits[i] = digits[i] + 1
        if i == len(digits) - 1:
            digits[i] = digits[i] + 1
            if digits[i] < 9:
                return digits
        re = digits[i] % 10
        divisor = int(digits[i] / 10)
        digits[i] = re
    if re == 0 and divisor == 1:
        return [divisor] + digits
    return digits
        
# 其他同学的极简风格代码，值得学习
def plus_one(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1, -1, -1):
        nums[i] += 1
        nums[i] = nums[i] % 10
        if nums[i] != 0:
            return nums
    return [1] + nums

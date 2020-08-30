
def two_sum(nums: List[int], target: int):
    d = {}
    for index, val in enumerate(nums):
        tmp = target - val
        if tmp in d:
            return d[tmp], index
        else:
            d[val] = index
    return []

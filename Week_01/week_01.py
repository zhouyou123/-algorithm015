# day 1 爬楼梯
#本质上就是求斐波拉契数列 
def jump_steps(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b


# 动态规划 （目前还不太能理解，什么是动态规划）
def jump_steps_v1(n):
    a, b, c = 0, 1, 0
    for i in range(n):
        c = a + b
        a = b
        b = c
    return b


# day 2  加一

def plus_one(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1, -1, -1):
        nums[i] += 1
        nums[i] = nums[i] % 10
        if nums[i] != 0:
            return nums
    return [1] + nums

# 练习了将数组打乱顺序的习题
def shuffle(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n):
        rd = int(random.random() * n)
        nums[n - 1], nums[rd] = nums[rd], nums[n - 1]
    return nums


# day 3 两数之和
def two_sum(nums: List[int], target: int):
    d = {}
    for index, val in enumerate(nums):
        tmp = target - val
        if tmp in d:
            return d[tmp], index
        else:
            d[val] = index
    return []

# 判断数字中重复的数字 (来自剑指offer)
def duplicate(nums: List[int]) -> int:
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            swap(nums, i, nums[i])

def swap(nums, i, j):
    k = nums[i]
    nums[i] = nums[j]
    nums[j] = k
    
    
# day 4 交换链表元素顺序
def swapPairs(self, head: ListNode) -> ListNode:
    pre = head
    nx = pre.next
    while nx:
        pre.val, nx.val = nx.val, pre.val
        pre = nx.next
        if pre is None:
            break
        nx = pre.next
    return head

# day 5 合并两个链表
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    node = ListNode(None)
    tmp = node
    while l1 and l2:
        if l1.val < l2.val:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next
    if l1:
        tmp.next = l1
    if l2:
        tmp.next = l2
    return node.next

# day 6  括号生成
# 对递归的理解还是停留在暴力穷举阶段，对于递归类型的题目还得多加练习
def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    def gen(left, right, strs):
        if left == right == n:
            ans.append(strs)
            return
        if left < n:
            gen(left + 1, right, strs + "(")
        if right < left:
            gen(left, right + 1, strs + ")")

    gen(0, 0, "")
    return ans

# day7 反转字符串中的单词 III
# python 用 + 来进行字符串拼接是一种比较低效的方式，拼接的字符串越长，效率越低
def reverse_words(self, words):
    stack = []
    reverse_str = ''
    size = len(words)
    for i in range(size + 1):
        if i != size and words[i] != ' ':
            stack.append(words[i])
        else:
            tmp = ""
            for _ in range(len(stack)):
                tmp += stack.pop()
            if i != size:
                tmp += ' '
            reverse_str += tmp
    return reverse_str




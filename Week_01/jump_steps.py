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

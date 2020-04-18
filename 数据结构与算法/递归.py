#!/usr/bin/python3


def factorial(i):
    """阶乘"""
    if i < 0:
        return
    elif i <= 2:
        return i
    else:
        return i * factorial(i-1)


def fibonacci(i):
    """斐波那契数列"""
    if i <= 2:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)


def hanoi(n, a, b, c):  # a为初始位，b为过渡位，c为目标位
    """汉诺塔"""
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n-1, a, c, b)  # 初始位为a,通过c移动到b
        print(a, '-->', c)
        hanoi(n-1, b, a, c)  # 初始位为b,通过a移动到c


def monkey(n):
    """猴子分桃"""
    if n == 1:
        return 1
    else:
        return (monkey(n-1)+1)*2

def 递归(n):
    print("递进：" + str(n))
    if n > 0:
        递归(n-1)
    print("回归：" + str(n))


if __name__ == "__main__":
    # ans = factorial(-2)
    # ans = fibonacci(3)
    # hanoi(7, 'a', 'b', 'c')
    # ans = monkey(10)
    递归(3)
    # print(ans)


# def f(mode):
#     if end_condition:  # 递归出口
#         end
#     else:
#         f(mode_small)  # 递归本身，递归

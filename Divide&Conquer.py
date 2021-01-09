#!/bin/python3

'''
分治法（Divide and Conquer）
- 將大問題分割成多個子問題以便處理
- ex. quick sort、recursion

練習：計算第n項費伯納序列的遞迴
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif  n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':

    n = int(input('請輸入要計算第幾個費式數列：'))

    result = fibonacci(n)
    print(result)
#!/bin/python3

'''
動態規劃法（Dynamic Programming Algorithm）
- 跟分治法很像
- 但會讓每一個子問題的答案被存下來，以供下次求解使用
- 可以解決重複計算的問題

練習：計算第n項費伯納序列的遞迴（動態規劃法版本）
'''
output=[None]*1000 #暫存區
def fibonacci(n):
    result = output[n]

    if result== None:
        if n == 0:
            result = 0
        elif  n == 1 or n == 2:
            result = 1
        else:
            result = fibonacci(n-1) + fibonacci(n-2)
        output[n] = result
    return result

if __name__ == '__main__':

    n = int(input('請輸入要計算第幾個費式數列：'))

    result = fibonacci(n)
    print(result)
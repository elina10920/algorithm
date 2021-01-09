#!/bin/python3

'''
輾轉相除法 求 最大公因數(g.c.d)
'''
def GCD(num1, num2):
    while num2:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1


if __name__ == '__main__':

    num1 = int(input('請輸入第一個數字'))
    num2 = int(input('請輸入第二個數字'))

    result = GCD(num1, num2)
    print(result)
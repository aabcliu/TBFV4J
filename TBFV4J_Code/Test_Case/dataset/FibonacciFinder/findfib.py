import math

def fibonacci(k):
    phi = (1 + math.sqrt(5)) / 2  # 黄金比例
    psi = (1 - math.sqrt(5)) / 2  # 负的黄金比例
    return (phi**k - psi**k) / math.sqrt(5)

def findFib(n):
    k = 0
    fib = 0

    # 找到第一个大于 n 的斐波那契数
    while fib <= n:
        fib = fibonacci(k)
        k += 1
        
    return k - 1  # 返回索引

if __name__ == "__main__":
    n = int(input("请输入一个整数 n: "))
    
    index = findFib(n)
    result = fibonacci(index)

    print(f"第 {index} 项斐波那契数: {result:.0f}")
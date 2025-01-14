def bisection_sqrt(N, epsilon):
    
    if epsilon <= 0:
        return -2  # 精度非法
    elif N < 0:
        return -1  # 输入非法
    
    low, high = 0, max(1, N)  # 初始化区间
    while high - low > epsilon:
        mid = (low + high) / 2
        if mid * mid < N:
            low = mid
        else:
            high = mid
    
    return (low + high) / 2  # 返回近似解

# 示例调用
if __name__ == "__main__":
    N = float(input("请输入一个数 N: "))
    epsilon = float(input("请输入精度 epsilon: "))
    result = bisection_sqrt(N, epsilon)
    if result == -1:
        print("输入非法，负数没有实数平方根")
    elif result == -2:
        print("精度输入非法")
    else:
        print("Result:", result)

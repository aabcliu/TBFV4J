def newton_sqrt(N, epsilon):
    if N < 0:
        Error = -1
        return Error  # 输入非法，负数没有实数平方根
    elif epsilon <= 0:
        Error = -2
        return Error  # 精度输入非法
    x_n = N / 2.0  # 初始猜测
    while abs(x_n * x_n - N) >= epsilon:  # 当平方误差大于精度时
        x_n = 0.5 * (x_n + N / x_n)  # 牛顿迭代公式

    return x_n  # 返回计算得到的平方根

# 示例调用
if __name__ == "__main__":
    N = float(input("请输入一个数 N: "))
    epsilon = float(input("请输入精度 epsilon: "))
    result = newton_sqrt(N, epsilon)
    if result == -1:
        print("输入非法，负数没有实数平方根")
    elif result == -2:
        print("精度输入非法")
    else:
        print("Result:", result)

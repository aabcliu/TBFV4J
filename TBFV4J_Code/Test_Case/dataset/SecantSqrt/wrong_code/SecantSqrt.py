def secant_sqrt(N, epsilon):
    if N < 0:
        return -1  # 输入非法
    elif epsilon <= 0:
        return -1  # 精度非法

    x0, x1 = N / 2.0, N / 3.0  # 初始化两个点
    while abs(x1 * x1 - N) >= epsilon:
        f_x0 = x0 * x0 - N
        f_x1 = x1 * x1 - N
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)  # 割线法公式
        x0, x1 = x1, x2

    return x1  # 返回近似解

# 示例调用
if __name__ == "__main__":
    N = float(input("请输入一个数 N: "))
    epsilon = float(input("请输入精度 epsilon: "))
    result = secant_sqrt(N, epsilon)
    if result == -1:
        print("输入非法，负数没有实数平方根")
    elif result == -2:
        print("精度非法")
    else:
        print("Result:", result)

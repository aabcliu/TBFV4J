def sum_finder(x):
    if x < 0:
        print("Result: none")  # 如果 x 小于 0，则输出 "none"
    elif x == 0:
        print("Result: 0")  # 如果 x 等于 0，则输出 0
    else:
        sum = 0
        n = 1

        # 累加自然数，直到累加和 >= x
        while sum < x:
            sum += n
            n += 1

        # 在循环结束后，将 n 减去 1，使其符合条件
        n -= 1  # 确保 n 是满足条件的最小值

        # 输出当前自然数 n
        print(f"Result: {n}")

# 示例输入
x = int(input("请输入一个数 x: "))
sum_finder(x)

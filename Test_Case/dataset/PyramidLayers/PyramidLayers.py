def max_pyramid_layers(N):
    # 如果 N 小于等于 0，直接返回 0
    if N <= 0:
        return 0

    result = 0

    while True:
        # 计算当前层数的砖块需求
        current_bricks = (result * (result + 1) * (2 * result + 1)) // 6
        # 计算下一层的砖块需求
        next_bricks = ((result + 1) * (result + 2) * (2 * (result + 1) + 1)) // 6
        # 检查当前砖块需求是否在范围内
        if current_bricks <= N < next_bricks:
            break
        # 增加层数
        result += 1

    return result

if __name__ == "__main__":
    N = 14  # 你可以修改这个值来测试不同的输入
    print("可以构建的金字塔层数:", max_pyramid_layers(N))
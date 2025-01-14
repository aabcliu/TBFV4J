def free_fall_speed_at_distance():
    # 常量定义
    g = 9.8  # 重力加速度（m/s^2）

    # 获取用户输入的初始高度和目标下落距离
    h0 = float(input("Enter the initial height (h0) in meters: "))
    y = float(input("Enter the fall distance (y) in meters: "))

    # 检查目标下落距离是否合理
    if y < 0:
        print("Distance cannot be negative.")
    elif y > h0:
        print("Fall distance exceeds initial height.")
    else:
        # 初始化下落距离和时间
        current_distance = 0
        t = 0  # 初始时间
        V = 0  # 速度

        # 循环计算下落过程，每次时间 t 增加 1 秒
        while current_distance < y:
            t += 1  # 增加 1 秒时间

            # 计算当前时间 t 的下落距离
            current_distance = 0.5 * g * t * t  # y = 1/2 * g * t^2

            # 计算当前时刻的速度
            V = g * t  # v = g * t

            # 如果下落距离已经超过目标距离，跳出循环
            if current_distance >= y:
                break

        # 输出结果
        print(f"Time after falling {current_distance} meters from initial height {h0} meters: {t} seconds.")
        print(f"Speed at that moment: {V} m/s.")

# 调用函数
free_fall_speed_at_distance()
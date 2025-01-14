import time

# 定义常量
UINT32_MAX = 0xFFFFFFFF  # uint32_t 最大值
TIME_INTERVAL = 5000     # 时间间隔 5 秒 (5000 毫秒)
start_tick = 0           # 用于记录上次操作时间点

# 获取当前时间戳（模拟 HAL_GetTick 的行为）
def get_tick():
    return int(time.time() * 1000) & UINT32_MAX  # 模拟 uint32_t 溢出行为

# 检查是否满足读取温度的时间间隔
# 为了模拟规约，只好将 cur_tick 作为参数传入
def is_get_temp_time(cur_tick=None):
    global start_tick
    #模拟代码cur_tick = get_tick()
    read_flag = False

    if cur_tick >= start_tick:
        # 正常情况，无溢出
        if cur_tick - start_tick >= TIME_INTERVAL:
            read_flag = True
    else:
        # 处理时间戳溢出情况
        if (UINT32_MAX - start_tick + cur_tick) >= TIME_INTERVAL:
            read_flag = True

    # 如果时间间隔满足条件，更新 start_tick
    if read_flag:
        start_tick = cur_tick
    return read_flag

# 测试该方法
if __name__ == "__main__":
    print(is_get_temp_time(int(input("请输入当前时间戳："))))
#print(is_get_temp_time())
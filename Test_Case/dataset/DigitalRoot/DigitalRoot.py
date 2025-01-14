def find_max_digital_root(A, n):
    # 错误判断逻辑
    if n > 9 or n < -9 or (A <= 0 and n > 0) or (A < 0 and n >= 0):
        return "error_code"
    
    # n = 0 的特殊情况
    if n == 0 and A >= 0:
        return "0"
    
    # 从 A 开始向下寻找
    for i in range(A, -float('inf'), -1):
        if i == 0:
            digital_root = 0
        elif i > 0:
            digital_root = 1 + (i - 1) % 9
        else:
            digital_root = -(1 + (-i - 1) % 9)
        
        if digital_root == n:
            return str(i)
    
    return "没有找到符合条件的数字"

if __name__ == "__main__":
    A = int(input("请输入整数 A: "))
    n = int(input("请输入整数 n: "))
    
    result = find_max_digital_root(A, n)
    print("结果:", result)
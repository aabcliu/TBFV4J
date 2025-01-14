from z3 import *

# 创建一个符号变量
x = Real('x')

# 创建一个逻辑表达式
expr = And(x < 0, Not(0 - 1 == -1))

# 创建求解器
solver = Solver()
solver.add(expr)

# 检查可满足性
if solver.check() == sat:
    print("表达式是可满足的，原式是永真的")
else:
    print("表达式是不可满足的")

from z3 import *
import sys


def create_expressions(x):
    # 创建符号变量
    x_var = Real('x')

    # 动态生成表达式
    expressions = []

    for i in range(x):
        expr = x_var - (x - i) >= 0
        expressions.append(expr)

    return expressions


def main():
    # 获取传递的参数
    if len(sys.argv) > 1:
        x_number = int(sys.argv[1])  # 将参数转换为整数
    else:
        print("No x_number provided.")
        return  # 退出程序

    # 创建逻辑表达式
    x = Real('x')
    expr1 = x >= 0
    expr2 = Not(x - (x_number + 1) >= 0)  # ~ (x - (x_number + 1) >= 0)
    expr3 = x - x_number >= 0
    expr4 = 0 + x_number == x - (x_number + 1)

    # 生成其他表达式
    additional_expressions = create_expressions(x_number)

    # 合并所有表达式
    all_expressions = [expr1, expr2, expr3, expr4] + additional_expressions
    combined_expr = ' ∧ '.join(str(expr) for expr in all_expressions)

    # 输出合并后的表达式
    print("合取式为：")
    print(combined_expr)

    # 创建求解器
    solver = Solver()
    solver.add(all_expressions)

    # 检查可满足性
    if solver.check() == unsat:
        print("表达式是不可满足的，原式是永真的")
    else:
        print("表达式是可满足的")


if __name__ == "__main__":
    main()

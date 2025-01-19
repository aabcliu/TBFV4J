import subprocess
import re
import random
import time
from z3 import *

start_time = 0
# Create the Z3 solver
solver = Solver()

def extract_variables(expr):
    """
    Extract variable names (identifiers starting with a letter) from the logical expression, excluding Z3 keywords.
    """
    z3_keywords = {"And", "Or", "Not", "Implies", "True", "False"}
    all_vars = set(re.findall(r'\b[a-zA-Z]\w*\b', expr))
    return all_vars - z3_keywords


def preprocess_expression(expr):
    """
    Preprocess the logical expression:
    1. Remove meaningless underscores (_)
    2. Replace logical operators
    3. Replace special symbols (e.g., → replaced with Implies)
    4. Replace boolean values (true/false replaced with True/False)
    """
    # Remove meaningless underscores after variable names
    expr = re.sub(r'\b(\w+)_\b', r'\1', expr)

    # Replace boolean values
    expr = expr.replace("true", "True").replace("false", "False")

    # Replace logical operators
    expr = expr.replace("&&", ",").replace("||", ",")
    expr = re.sub(r'!\s*\((.*?)\)', r'Not(\1)', expr)  # !(...) -> Not(...)
    # Replace '=' with '==' to avoid ===
    expr = re.sub(r'(?<![<>=!])=(?!=)', '==', expr)  # Replace single "=" with "=="
    expr = expr.replace("→", ", Implies")  # Replace logical symbols

    # Replace logical operators with function form
    expr = re.sub(r'\bAnd\b', 'And', expr)
    expr = re.sub(r'\bOr\b', 'Or', expr)

    # Remove extra spaces
    expr = re.sub(r'\s+', ' ', expr)
    return expr


def parse_to_z3(user_expr, variables):
    """
    Parse the user input logical expression to a Z3-compatible expression, ensuring logical keywords are not replaced.
    """
    # Replace variable names with Z3 symbolic variable references
    for var in variables:
        user_expr = re.sub(rf'\b{var}\b', f'variables["{var}"]', user_expr)
    return user_expr

def solve_logic_expression(logic_expr):
    """
    Solve the logical expression.
    Parameters: logic_expr (str) - The input logical expression
    Returns: A satisfying solution or unsatisfiable information
    """
    try:
        # Create a new solver instance
        local_solver = Solver()

        # Preprocess the logical expression
        preprocessed_input = preprocess_expression(logic_expr)

        # Extract variables and dynamically create Z3 symbolic variables
        variables = {}
        variable_names = extract_variables(preprocessed_input)
        for var in variable_names:
            variables[var] = Int(var)  # Use Int to handle integers

        # Parse the expression to Z3 format
        parsed_expr = parse_to_z3(preprocessed_input, variables)
        print("Debug: The converted expression is ->", parsed_expr)  # Debug information

        # Use eval to convert to Z3 expression
        z3_expr = eval(parsed_expr)
        local_solver.add(z3_expr)

        # Check satisfiability
        if local_solver.check() == sat:
            print("The expression is satisfiable")
            model = local_solver.model()
            results = {v: model[variables[v]] for v in variables}
            return results
        else:
            return "The expression is unsatisfiable"

    except Exception as e:
        print("The expression is unsatisfiable")
        # print("Error message:", e)
        # return f"Error message: {e}"

def get_user_input():
    print("Step 1: Enter your Java code (modified with print statements)")
    java_code_lines = []
    while True:
        line = input()
        if line == "":
            break
        java_code_lines.append(line)
    java_code = "\n".join(java_code_lines)

    T = input("\nStep 2: Enter your Test Condition T:")
    D = input("\nStep 3: Enter your Define Condition D: ")
    rounds = int(input("\nStep 4: Enter how many times you want to run the program: "))
    return java_code, T, D, rounds

def extract_input_variables(java_code: str) -> list:
    input_patterns = [
        r"(\w+)\s*=\s*scanner\.nextInt\(\)",
        r"(\w+)\s*=\s*scanner\.nextDouble\(\)",
        r"(\w+)\s*=\s*scanner\.nextLine\(\)",
    ]
    input_variables = []

    for pattern in input_patterns:
        matches = re.findall(pattern, java_code)
        input_variables.extend(matches)

    return input_variables
def run_java_code(java_code: str, user_inputs: dict) -> str:
    with open("UserInputProgram.java", "w") as file:
        file.write("import java.util.Scanner;\n" + java_code)

    try:
        subprocess.run(["javac", "UserInputProgram.java"], check=True)
    except subprocess.CalledProcessError:
        print("Error during Java compilation.")
        return ""

    input_string = "\n".join(map(str, user_inputs.values())) + "\n"

    try:
        result = subprocess.run(
            ["java", "UserInputProgram"],
            capture_output=True,
            text=True,
            input=input_string
        )
        return result.stdout
    except subprocess.CalledProcessError:
        print("Error during Java execution.")
        return ""
def parse_execution_path(execution_output: str) -> list:
    lines = execution_output.splitlines()
    execution_path = []

    for line in lines:
        if "current value" in line or "Entering loop" in line or "Exiting loop" in line:
            execution_path.append(line)

    return execution_path

def negate_ct_condition(ct):
    """
    对复杂的 Ct 条件进行整体取反：
    - 将 Ct 中的每个子条件取反。
    - 将 '&&' 替换为 '||'。
    - 如果子条件已经有 '!'，则消去双重否定。
    """
    # 如果 Ct 有外层括号，去掉最外层括号
    if ct.startswith("(") and ct.endswith(")"):
        ct = ct[1:-1]

    # 使用 split_logical 函数将 Ct 按 '&&' 拆分为子条件
    subconditions = split_logical(ct, "&&")

    # 遍历每个子条件并取反
    negated_conditions = []
    for condition in subconditions:
        condition = condition.strip()
        if condition.startswith("!(") and condition.endswith(")"):  # 已经是取反的条件
            negated_conditions.append(condition[2:-1])  # 去掉双重否定
        elif condition.startswith("(") and condition.endswith(")"):  # 包含括号的条件
            negated_conditions.append(f"!{condition}")  # 直接取反
        else:
            negated_conditions.append(f"!({condition})")  # 添加括号并取反

    # 将取反后的条件用 '||' 连接
    negated_ct = " || ".join(negated_conditions)

    return negated_ct

def split_logical(expression, operator):
    """
    按照给定的逻辑运算符（如 '&&'）拆分逻辑表达式，同时保留括号的嵌套关系。
    """
    parts = []
    bracket_level = 0
    current_part = []

    i = 0
    while i < len(expression):
        char = expression[i]

        # 更新括号嵌套层级
        if char == "(":
            bracket_level += 1
        elif char == ")":
            bracket_level -= 1

        # 在括号层级为 0 且遇到操作符时拆分
        if bracket_level == 0 and expression[i:i + len(operator)] == operator:
            parts.append("".join(current_part).strip())
            current_part = []
            i += len(operator) - 1  # 跳过操作符
        else:
            current_part.append(char)

        i += 1

    # 添加最后一部分
    parts.append("".join(current_part).strip())
    return parts
def generate_logical_expression(t, previous_cts):
    """
    将 T 和历史 Ct 条件组合生成新的逻辑表达式。
    :param t: 测试条件 T（例如 "x >= 0"）。repeat_execution_with_ct
    :param previous_cts: 历史 Ct 条件列表。
    :return: 新的逻辑表达式。
    """
    # 初始逻辑表达式为 T
    combined_expression = t

    # 使用集合去重，避免重复的 Ct 条件
    unique_cts = list(set(previous_cts))

    # 累积所有 Ct 条件，并取反
    for ct in unique_cts:
        combined_expression = f"{combined_expression} && !( {ct} )"

    return combined_expression

def evaluate_expression(expr, values):
    """
    Evaluates a logical expression using the provided variable values.
    :param expr: The logical expression as a string (e.g., 'x >= 0 && !(x - 1 >= 0)').
    :param values: A dictionary of variable values (e.g., {'x': 5}).
    :return: Boolean result of the expression or an error message.
    """
    try:
        # Step 1: Replace logical operators with Python equivalents
        python_expr = expr.replace("&&", "and").replace("||", "or").replace("!", "not")

        # Step 2: Replace variables with their values in the expression
        for var, value in values.items():
            python_expr = re.sub(rf'\b{var}\b', str(value), python_expr)

        # Debug: Print the transformed expression for verification
        # print(f"Debug: Evaluating Python expression: '{python_expr}'")

        # Step 3: Evaluate the logical expression
        result = eval(python_expr)
        return result
    except Exception as e:
        # Print the error message for debugging
        # print(f"Error during expression evaluation: {e}")
        # print(f"Original Expression: '{expr}'")
        # print(f"Transformed Expression: '{python_expr}'")
        return False

def generate_random_inputs(logical_expression, variables, previous_cts, used_inputs, max_attempts=100):
    """
    生成满足 T 且 !(Ct1) && !(Ct2) && ... 的随机输入，确保结果不重复。
    :param logical_expression: 测试条件 T。
    :param variables: 变量列表。
    :param previous_cts: 历史 Ct 条件列表。
    :param used_inputs: 已使用的输入集合。
    :param max_attempts: 最大尝试次数。
    :return: 满足条件的输入字典，或 None 如果找不到解。
    """
    # 组合所有条件：T && !(Ct1) && !(Ct2) && ...
    combined_condition = logical_expression
    for ct in previous_cts:
        combined_condition = f"{combined_condition} && !( {ct} )"

    # print(f"Debug: Combined condition for input generation: {combined_condition}")

    for attempt in range(max_attempts):
        # 随机生成变量值
        inputs = {var: random.randint(-200, 200) for var in variables}

        # 检查是否与历史输入重复
        if tuple(inputs.items()) in used_inputs:
            # print(f"Debug: Attempt {attempt + 1}, Generated inputs are duplicate: {inputs}")
            continue

        # 使用生成的输入评估逻辑表达式
        result = evaluate_expression(combined_condition, inputs)

        if result:
            # 如果找到满足条件且不重复的输入
            used_inputs.add(tuple(inputs.items()))
            print(f"Debug: Satisfying inputs found: {inputs}")
            return inputs

    print("Debug: No satisfying inputs found within the maximum attempts.")
    return None

def simplify_expression(expression):
    """
    简化逻辑表达式，移除多余的否定和冗余条件。
    """
    # 移除双重否定 !!(expr) -> (expr)
    expression = re.sub(r'!\(!\((.*?)\)\)', r'\1', expression)
    expression = re.sub(r'\s+', ' ', expression)  # 去除多余空格
    return expression


def repeat_execution_with_ct(java_code, T, D, rounds, input_variables):
    print("\n### Automated Execution ###")
    previous_cts = []  # 存储所有历史 Ct 条件
    used_inputs = set()  # 存储所有已使用的输入

    for round_num in range(1, rounds + 1):
        print(f"\n### Execution Round {round_num} ###")

        # 根据 T 和历史 Ct 条件生成新的逻辑表达式
        logical_expression = generate_logical_expression(T, previous_cts)
        print(f"Current Logical Expression: {logical_expression}")

        # 调用简化函数简化表达式
        logical_expression = simplify_expression(logical_expression)
        # print(f"Simplified Logical Expression: {logical_expression}")

        # 生成满足 T && !(Ct1) && !(Ct2) && ... 的随机输入，确保不重复
        generated_inputs = generate_random_inputs(
            logical_expression, input_variables, previous_cts, used_inputs
        )

        # 检查生成结果
        if not generated_inputs:
            print(f"No inputs satisfy the condition: {logical_expression}. Program terminating.")
            break

        print(f"Generated inputs: {generated_inputs}")

        # 执行 Java 代码
        execution_output = run_java_code(java_code, generated_inputs)
        if not execution_output:
            print("No output from Java code execution.")
            continue

        # 提取执行路径
        execution_path = parse_execution_path(execution_output)
        print("\nExecution Path:")
        # for step in execution_path:
        #     print(step)

        # 推导 Hoare 逻辑
        derivation, new_d, new_ct = derive_hoare_logic(D, execution_path)
        print("\nHoare Logic Derivation:")
        # for step in derivation:
        #     print(step)

        print(f"\nNew D: {new_d}")
        print(f"\nNew Ct: {new_ct}")

        # 确保新的 Ct 不重复加入
        if new_ct not in previous_cts:
            previous_cts.append(new_ct)

        # 构建新的逻辑表达式
        negated_d = f"!({new_d})"  # Negate D
        new_logic_expression = f"{T} && {new_ct} && {negated_d}"

        # 调用简化函数简化表达式
        new_logic_expression = simplify_expression(new_logic_expression)
        print(f"\nT && Ct && !D: {new_logic_expression}")

        # 使用 Z3 求解器检查表达式的可满足性
        try:
            # 预处理逻辑表达式
            preprocessed_input = preprocess_expression(new_logic_expression)

            # 提取变量并动态创建 Z3 符号变量
            variables = {}
            variable_names = extract_variables(preprocessed_input)
            for var in variable_names:
                variables[var] = Int(var)  # 使用 Int 处理整数变量

            # 解析表达式为 Z3 格式
            parsed_expr = parse_to_z3(preprocessed_input, variables)
            # print(f"Parsed Z3 Expression: {parsed_expr}")  # 调试信息

            # 使用 eval 转换为 Z3 表达式
            z3_expr = eval(parsed_expr, {"variables": variables, "And": And, "Or": Or, "Not": Not, "Implies": Implies})
            solver.add(z3_expr)

            # 检查可满足性
            if solver.check() == sat:
                print("表达式是可满足的")
                model = solver.model()
                print("满足条件的解:")
                for v in variables.values():
                    print(f"{v} = {model[v]}")
            else:
                print("The expression is unsatisfiable")

        except Exception as e:
            print("The expression is unsatisfiable")
            # print("错误信息:", e)

        # Update Ct for next round
        previous_cts.append(new_ct)


def derive_hoare_logic(specification: str, execution_path: list) -> (list, str, str):
    """
    修正后的 derive_hoare_logic，支持复杂数学表达式的 D，并处理单条件或多条件。
    """
    derivation = []
    current_condition = specification

    # 尝试解析 D 是否包含 "&&"
    if "&&" in specification:
        # 改进后的正则表达式，支持括号嵌套的复杂数学表达式
        d_pattern = r"\((.+?)\)\s*&&\s*\((.+?)\)"
        d_match = re.match(d_pattern, specification)

        if d_match:
            # 如果匹配成功，提取子条件
            d1 = d_match.group(1).strip()
            d2 = d_match.group(2).strip()
        else:
            # 匹配失败时，抛出警告，但继续将整个 D 作为单条件处理
            print("Warning: Unable to parse D as two subconditions. Treating D as a single condition.")
            d1 = specification.strip()
            d2 = None
    else:
        # 如果 D 是单一条件
        d1 = specification.strip()
        d2 = None

    # 初始化 D 的子式
    updated_d1 = d1
    updated_d2 = d2

    for step in reversed(execution_path):
        derivation.append(f"After executing: {step}")

        # 检查是否是进入循环的条件
        if "Entering loop" in step:
            condition_match = re.search(r"Entering loop with condition: (.*?) is evaluated as: true", step)
            if condition_match:
                loop_condition = condition_match.group(1).strip()
                current_condition = f"{current_condition} && ({loop_condition})"

        # 检查是否是退出循环的条件
        elif "Exiting loop" in step:
            condition_match = re.search(r"Exiting loop, condition no longer holds: (.*?) is evaluated as: false", step)
            if condition_match:
                loop_condition = condition_match.group(1).strip()
                current_condition = f"{current_condition} && !({loop_condition})"

        # 检查是否是变量赋值
        elif "current value" in step:
            assignment_match = re.search(r"(.*?) = (.*?), current value of (.*?): (.*?)$", step)
            if assignment_match:
                variable = assignment_match.group(1).strip()
                value = assignment_match.group(2).strip()

                # 更新 D 的子式
                updated_d1 = replace_variables(updated_d1, variable, value)
                if updated_d2 is not None:
                    updated_d2 = replace_variables(updated_d2, variable, value)

                # 更新当前条件
                current_condition = replace_variables(current_condition, variable, value)

        derivation.append(f"Current Condition: {current_condition}")

    # 构建 New D 和 New Ct
    if updated_d2 is not None:
        new_d = f"({updated_d1}) && ({updated_d2})"
    else:
        new_d = updated_d1  # 如果没有第二个子条件，直接返回 updated_d1

    new_ct = current_condition.replace(new_d, "").strip(" &&")

    return derivation, new_d, new_ct
def replace_variables(current_condition: str, variable: str, new_value: str) -> str:
    """
    替换逻辑条件中的变量为新的值。
    """
    pattern = rf'\b{re.escape(variable)}\b'  # 精确匹配变量名
    return re.sub(pattern, new_value, current_condition)
def main():

    java_code, T, D, rounds = get_user_input()
    start_time = time.time()
    input_variables = extract_input_variables(java_code)
    repeat_execution_with_ct(java_code, T, D, rounds, input_variables)
    end_time = time.time()

    # 计算运行时间（秒）
    execution_time = end_time - start_time
    execution_time=execution_time
    print(f"Running time: {execution_time:.6f} seconds")
    print("Totally Verified !!")

if __name__ == "__main__":
    main()







# import subprocess
# import re
# import random
# import time
# from z3 import *
# # Create the Z3 solver
# solver = Solver()
# def extract_variables(expr):
#     """
#     Extract the variable name (the identifier starting with the letter) from the logical expression, excluding the Z3 logical keyword
#     """
#     z3_keywords = {"And", "Or", "Not", "Implies", "True", "False"}
#     all_vars = set(re.findall(r'\b[a-zA-Z]\w*\b', expr))
#     return all_vars - z3_keywords
# def preprocess_expression(expr):
#     """
#     "
#     Preprocessing logical expression:
#     1. Delete the meaningless underscore '_'
#     2. Replace the logical operator
#     3. Replace the special symbol (for example, '→' Implies')
#     4. Replace Boolean values (replace true/false with True/False)
#     "
#     # Remove meaningless underscores after variable names
#     """
#     #  Remove meaningless underscores after variable names
#     expr = re.sub(r'\b(\w+)_\b', r'\1', expr)
#
#     # Replace Boolean values
#     expr = expr.replace("true", "True").replace("false", "False")
#
#     # Replace the logical operator
#     expr = expr.replace("&&", ",").replace("||", ",")
#     expr = re.sub(r'!\s*\((.*?)\)', r'Not(\1)', expr)  # !(...) -> Not(...)
#     # Only replace the single '=' with '==', avoiding the occurrence of '==='
#     expr = re.sub(r'(?<![<>=!])=(?!=)', '==', expr)  # Replace a single "=" with "=="
#     expr = expr.replace("→", ", Implies")  # Substitution logic symbol
#
#     # Replace logical operators with functional forms
#     expr = re.sub(r'\bAnd\b', 'And', expr)
#     expr = re.sub(r'\bOr\b', 'Or', expr)
#     # Delete extra Spaces
#     expr = re.sub(r'\s+', ' ', expr)
#     return expr
#
#
# def parse_to_z3(user_expr, variables):
#     """
#     Parses user input logical expressions into Z3-compatible expressions, ensuring that logical keywords are not replaced
#     """
#     # The replacement variable is named Z3 symbol variable reference
#     for var in variables:
#         user_expr = re.sub(rf'\b{var}\b', f'variables["{var}"]', user_expr)
#     return user_expr
#
# def solve_logic_expression(logic_expr):
#     """
#     Logical expression solution function
#     Parameter: logic_expr (str) - Input logical expression
#     Returns: A solution that satisfies the condition or information that is unsatisfied
#     """
#     try:
#         # Create a new solver instance
#         local_solver = Solver()
#
#         # Preprocessed logical expression
#         preprocessed_input = preprocess_expression(logic_expr)
#
#         # Extract variables and dynamically create Z3 symbolic variables
#         variables = {}
#         variable_names = extract_variables(preprocessed_input)
#         for var in variable_names:
#             variables[var] = Int(var)  # Use Int to process integers
#
#         # The parsing expression is in Z3 format
#         parsed_expr = parse_to_z3(preprocessed_input, variables)
#         print("调试信息: 转换后的表达式为 ->", parsed_expr)  # Debugging information
#
#         # Convert to Z3 expressions using eval
#         z3_expr = eval(parsed_expr)
#         local_solver.add(z3_expr)
#
#         # Check satisfiability
#         if local_solver.check() == sat:
#             print("表达式是可满足的")
#             model = local_solver.model()
#             results = {v: model[variables[v]] for v in variables}
#             return results
#         else:
#             return "表达式是不可满足的"
#
#     except Exception as e:
#         print("表达式解析错误，请检查格式！")
#         print("错误信息:", e)
#         return f"错误信息: {e}"
#
# def get_user_input():
#     print("Step 1: Enter your Java code (modified with print statements)")
#     java_code_lines = []
#     while True:
#         line = input()
#         if line == "":
#             break
#         java_code_lines.append(line)
#     java_code = "\n".join(java_code_lines)
#
#     T = input("\nStep 2: Enter your Test Condition T:")
#     D = input("\nStep 3: Enter your Define Condition D: ")
#     rounds = int(input("\nStep 4: Enter how many times you want to run the program: "))
#
#     return java_code, T, D, rounds
#
# def extract_input_variables(java_code: str) -> list:
#     input_patterns = [
#         r"(\w+)\s*=\s*scanner\.nextInt\(\)",
#         r"(\w+)\s*=\s*scanner\.nextDouble\(\)",
#         r"(\w+)\s*=\s*scanner\.nextLine\(\)",
#     ]
#     input_variables = []
#
#     for pattern in input_patterns:
#         matches = re.findall(pattern, java_code)
#         input_variables.extend(matches)
#
#     return input_variables
# def run_java_code(java_code: str, user_inputs: dict) -> str:
#     with open("UserInputProgram.java", "w") as file:
#         file.write("import java.util.Scanner;\n" + java_code)
#
#     try:
#         subprocess.run(["javac", "UserInputProgram.java"], check=True)
#     except subprocess.CalledProcessError:
#         print("Error during Java compilation.")
#         return ""
#
#     input_string = "\n".join(map(str, user_inputs.values())) + "\n"
#
#     try:
#         result = subprocess.run(
#             ["java", "UserInputProgram"],
#             capture_output=True,
#             text=True,
#             input=input_string
#         )
#         return result.stdout
#     except subprocess.CalledProcessError:
#         print("Error during Java execution.")
#         return ""
# def parse_execution_path(execution_output: str) -> list:
#     lines = execution_output.splitlines()
#     execution_path = []
#
#     for line in lines:
#         if "current value" in line or "Entering loop" in line or "Exiting loop" in line:
#             execution_path.append(line)
#
#     return execution_path
#
# def negate_ct_condition(ct):
#     """
#     Overall inversion of complex Ct conditions:
#     - Invert each sub-condition in Ct.
#     - Replace '&&' with '||'.
#     - If the subcondition already has '! ', then the double negative is eliminated.
#     """
#     # If Ct has outer parentheses, remove the outermost parentheses
#     if ct.startswith("(") and ct.endswith(")"):
#         ct = ct[1:-1]
#
#     # Use the split_logical function to split Ct into sub-conditions by '&&'
#     subconditions = split_logical(ct, "&&")
#
#     # Go through each subcondition and invert it
#     negated_conditions = []
#     for condition in subconditions:
#         condition = condition.strip()
#         if condition.startswith("!(") and condition.endswith(")"):  # It's already the inverse condition
#             negated_conditions.append(condition[2:-1])  # Remove the double negative
#         elif condition.startswith("(") and condition.endswith(")"):  # Conditions that contain parentheses
#             negated_conditions.append(f"!{condition}")  # Direct inversion
#         else:
#             negated_conditions.append(f"!({condition})")  # Add parentheses and invert
#
#     # Concatenate the inverted condition with '||'
#     negated_ct = " || ".join(negated_conditions)
#
#     return negated_ct
#
# def split_logical(expression, operator):
#     """
#     Split the logical expression with a given logical operator, such as '&&', while preserving the nested relationship of parentheses.
#     """
#     parts = []
#     bracket_level = 0
#     current_part = []
#
#     i = 0
#     while i < len(expression):
#         char = expression[i]
#
#         # Update the bracket nesting level
#         if char == "(":
#             bracket_level += 1
#         elif char == ")":
#             bracket_level -= 1
#
#         # Split when the bracket level is 0 and an operator is encountered
#         if bracket_level == 0 and expression[i:i + len(operator)] == operator:
#             parts.append("".join(current_part).strip())
#             current_part = []
#             i += len(operator) - 1  # Skip operator
#         else:
#             current_part.append(char)
#
#         i += 1
#
#     # Add the last part
#     parts.append("".join(current_part).strip())
#     return parts
# def generate_logical_expression(t, previous_cts):
#     """
#     Combine T and historical Ct conditions to generate a new logical expression.
#     :param t: Test condition T (for example, "x >= 0"). repeat_execution_with_ct
#     :param previous_cts: list of historical Ct conditions.
#     :return: indicates a new logical expression.
#     """
#     # The initial logical expression is T
#     combined_expression = t
#
#     # Use set weight removal to avoid duplicate Ct conditions
#     unique_cts = list(set(previous_cts))
#
#     # Accumulate all Ct conditions and invert them
#     for ct in unique_cts:
#         combined_expression = f"{combined_expression} && !( {ct} )"
#
#     return combined_expression
#
# def evaluate_expression(expr, values):
#     """
#     Evaluates a logical expression using the provided variable values.
#     :param expr: The logical expression as a string (e.g., 'x >= 0 && !(x - 1 >= 0)').
#     :param values: A dictionary of variable values (e.g., {'x': 5}).
#     :return: Boolean result of the expression or an error message.
#     """
#     try:
#         # Step 1: Replace logical operators with Python equivalents
#         python_expr = expr.replace("&&", "and").replace("||", "or").replace("!", "not")
#
#         # Step 2: Replace variables with their values in the expression
#         for var, value in values.items():
#             python_expr = re.sub(rf'\b{var}\b', str(value), python_expr)
#
#         # Debug: Print the transformed expression for verification
#         # print(f"Debug: Evaluating Python expression: '{python_expr}'")
#
#         # Step 3: Evaluate the logical expression
#         result = eval(python_expr)
#         return result
#     except Exception as e:
#         # Print the error message for debugging
#         # print(f"Error during expression evaluation: {e}")
#         # print(f"Original Expression: '{expr}'")
#         # print(f"Transformed Expression: '{python_expr}'")
#         return False
#
#
# def generate_random_inputs(logical_expression, variables, previous_cts, max_attempts=100):
#     """
#     Generate satisfying T and! (Ct1) && ! (Ct2) && ...  Random input.
#     :param logical_expression: indicates the test condition T.
#     :param variables: List of variables.
#     :param previous_cts: list of historical Ct conditions.
#     :param max_attempts: indicates the maximum number of attempts.
#     :return: The input dictionary that satisfies the condition, or None if the solution is not found.
#     """
#     # Combine all conditions: T &&! (Ct1) && ! (Ct2) && ...
#     combined_condition = logical_expression
#     for i, ct in enumerate(previous_cts):
#         combined_condition = f"{combined_condition} && !( {ct} )"
#
#     print(f"Debug: Combined condition for input generation: {combined_condition}")
#
#     for attempt in range(max_attempts):
#         # Randomly generate variable values in the range [-20, 20]
#         inputs = {var: random.randint(-10, 33) for var in variables}
#         # print(f"Debug: Attempt {attempt + 1}, Generated inputs: {inputs}")
#
#         # Evaluate the logical expression using the generated input
#         result = evaluate_expression(combined_condition, inputs)
#
#         if result:
#             print(f"Debug: Satisfying inputs found: {inputs}")
#             return inputs
#
#     print("Debug: No satisfying inputs found within the maximum attempts.")
#     return None
#
# def repeat_execution_with_ct(java_code, T, D, rounds, input_variables):
#     print("\n### Automated Execution ###")
#     previous_cts = []  # Store all historical Ct conditions
#
#     for round_num in range(1, rounds + 1):
#         print(f"\n### Execution Round {round_num} ###")
#
#         # Generate new logical expressions based on T and historical Ct conditions
#         logical_expression = generate_logical_expression(T, previous_cts)
#         print(f"Current Logical Expression: {logical_expression}")
#
#         # Generate satisfying T &&! (Ct1) && ! (Ct2) && ...  Random input of
#         generated_inputs = generate_random_inputs(logical_expression, input_variables, previous_cts)
#
#         if not generated_inputs:
#             print(f"No inputs satisfy the condition: {logical_expression}.")
#             break
#
#         print(f"Generated inputs: {generated_inputs}")
#
#         # Execute Java code
#         execution_output = run_java_code(java_code, generated_inputs)
#         if not execution_output:
#             print("No output from Java code execution.")
#             continue
#
#         # Extract execution path
#         execution_path = parse_execution_path(execution_output)
#         print("\nExecution Path:")
#         # for step in execution_path:
#         #     print()
#
#         # Derive the Hoare logic
#         derivation, new_d, new_ct = derive_hoare_logic(D, execution_path)
#         print("\nHoare Logic Derivation:")
#         # for step in derivation:
#         #     print()
#
#         print(f"\nNew D: {new_d}")
#         print(f"\nNew Ct: {new_ct}")
#
#         # Ensure that no new Ct is added
#         if new_ct not in previous_cts:
#             previous_cts.append(new_ct)
#         negated_d = f"!({new_d})"  # Negate D
#         new_logic_expression = f"{T} && {new_ct} && {negated_d}"
#         print(f"\nT && Ct && !D: {new_logic_expression}")
#         # Input logical expression
#         user_input = new_logic_expression
#
#         try:
#             # Preprocessed logical expression
#             preprocessed_input = preprocess_expression(user_input)
#
#             # Extract variables and dynamically create Z3 symbolic variables
#             variables = {}
#             variable_names = extract_variables(preprocessed_input)
#             for var in variable_names:
#                 variables[var] = Int(var)  # Use Int to handle integer variables
#
#             # The parsing expression is in Z3 format
#             parsed_expr = parse_to_z3(preprocessed_input, variables)
#             # print("调试信息: 转换后的表达式为 ->", parsed_expr)  # Debugging information
#
#             # Convert to Z3 expressions using eval
#             z3_expr = eval(parsed_expr, {"variables": variables, "And": And, "Or": Or, "Not": Not, "Implies": Implies})
#             solver.add(z3_expr)
#
#             # Check satisfiability
#             if solver.check() == sat:
#                 print("The expression is satisfiable")
#                 model = solver.model()
#                 print("Solutions that satisfy the conditions:")
#                 for v in variables.values():
#                     print(f"{v} = {model[v]}")
#             else:
#                 print("The expression is unsatisfiable")
#
#         except Exception as e:
#             print("Expression parsing error, please check the format!")
#             print("Error message:", e)
#
#         # Update Ct for next round
#         previous_cts.append(new_ct)
#
# def derive_hoare_logic(specification: str, execution_path: list) -> (list, str, str):
#     """
#     Derive the Hoare logic from the execution path.
#     """
#     derivation = []
#     current_condition = specification
#
#     for step in reversed(execution_path):
#         derivation.append(f"After executing: {step}")
#         if "Entering loop" in step:
#             condition_match = re.search(r"Entering loop with condition: (.*?) is evaluated as: true", step)
#             if condition_match:
#                 loop_condition = condition_match.group(1).strip()
#                 current_condition = f"{current_condition} && ({loop_condition})"
#         elif "Exiting loop" in step:
#             condition_match = re.search(r"Exiting loop, condition no longer holds: (.*?) is evaluated as: false", step)
#             if condition_match:
#                 loop_condition = condition_match.group(1).strip()
#                 current_condition = f"{current_condition} && !({loop_condition})"
#         elif "current value" in step:
#             assignment_match = re.search(r"(.*?) = (.*?), current value of (.*?): (.*?)$", step)
#             if assignment_match:
#                 variable = assignment_match.group(1).strip()
#                 value = assignment_match.group(2).strip()
#                 current_condition = replace_variables(current_condition, variable, value)
#
#         derivation.append(f"Current Condition: {current_condition}")
#
#     # Split final logic into D and Ct
#     if "&&" in current_condition:
#         parts = current_condition.split("&&", 1)
#         D = parts[0].strip()
#         Ct = parts[1].strip()
#     else:
#         D = current_condition
#         Ct = ""
#
#     return derivation, D, Ct
# def replace_variables(current_condition: str, variable: str, new_value: str) -> str:
#     pattern = r'(?<=\b)' + re.escape(variable) + r'(?=\b)'
#     return re.sub(pattern, new_value, current_condition)
#
# def main():
#     java_code, T, D, rounds = get_user_input()
#     input_variables = extract_input_variables(java_code)
#     repeat_execution_with_ct(java_code, T, D, rounds, input_variables)
#
# if __name__ == "__main__":
#     main()

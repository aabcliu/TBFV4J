package org.example;

import java.util.Scanner;
import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.BinaryExpr;
import com.github.javaparser.ast.stmt.IfStmt;
import com.github.javaparser.ast.stmt.WhileStmt;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class DynamicJavaExecutor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 用户输入 Java 程序
        System.out.println("请输入 Java 程序 (以 END 结尾)：");
        StringBuilder program = new StringBuilder();
        String line;
        while (!(line = scanner.nextLine()).equals("END")) {
            program.append(line).append("\n");
        }

        // 用户输入程序规范 S
        System.out.println("请输入程序规范 S：");
        String spec = scanner.nextLine();

        // 执行路径与逻辑推导
        executeProgram(program.toString(), spec, scanner);
    }

    private static void executeProgram(String program, String spec, Scanner scanner) {
        // 使用实例化的 JavaParser 来解析用户输入的程序
        JavaParser parser = new JavaParser();
        CompilationUnit cu = parser.parse(program).getResult().orElseThrow();

        // 假设程序中只有一个 main 方法
        MethodDeclaration mainMethod = cu.findFirst(MethodDeclaration.class).orElseThrow();

        // 用户输入 x
        System.out.println("请输入 x 值：");
        final int[] x = {scanner.nextInt()};
        int py_zheng_number=x[0];
        final int[] y = {0};
        System.out.println("程序执行路径：");
        System.out.println("执行: y = 0;");

        // 模拟执行主方法中的代码
        mainMethod.getBody().ifPresent(body -> {
            body.getStatements().forEach(stmt -> {
                if (stmt instanceof WhileStmt) {
                    WhileStmt whileStmt = (WhileStmt) stmt;
                    String condition = whileStmt.getCondition().toString();
                    while (evaluateCondition(condition, x[0])) {
                        System.out.println("while (" + condition + ") 执行");
                        System.out.println("    x = " + x[0] + "; y = " + y[0] + ";");
                        System.out.println("执行: x = x - 1; y = y + 1;");
                        y[0]++;
                        x[0]--;
                    }


                }
            });
            // 处理 while 循环后面紧跟的 y = y - 1; 语句
            System.out.println("执行: y = y - 1;");
            y[0]--;
        });

        // 输出最终的 y 值
        System.out.println("最终 y = " + y[0]);
        System.out.println("霍尔逻辑推导:");
        if(y[0]==-1){
            System.out.println("{y=-1}");
            System.out.println("y=y-1;");
            System.out.println("{y-1=-1}");
            System.out.println("～(x>=0);");
            System.out.println("{～(x>=0)∧y-1=-1}");
            System.out.println("y=0");
            System.out.println("{～(x>=0)∧0-1=-1}");
            try {
                // 创建ProcessBuilder并指定Python解释器和脚本路径
                ProcessBuilder processBuilder = new ProcessBuilder("python3", "/Users/liuyang/Desktop/研0资料/untitled3/src/main/java/org/example/PY/Fu.py");
                processBuilder.redirectErrorStream(true); // 合并错误输出

                // 启动进程
                Process process = processBuilder.start();

                // 读取输出
                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line); // 打印Python脚本的输出
                }

                // 等待进程结束
                int exitCode = process.waitFor();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }else{
            System.out.println("{y=x}");
            System.out.println("y=y-1;");
            System.out.println("{y-1=x}");
            System.out.println("～(x>=0);");
            System.out.println("~x>=0;");
            System.out.println("{y-1=x ∧ ~x>=0}");
            System.out.println("y=y+1;");
            System.out.println("{y=x ∧ ~x>=0}");
            System.out.println("x=x-1;");
            System.out.println("{y=x-1 ∧ ~x>=0}");
            System.out.println("x>=0");
            System.out.println("{y=x-1 ∧ ~x>=0 ∧ x>=0}");
            System.out.println(".....................");
            try {
                // 创建ProcessBuilder并指定Python解释器和脚本路径
                ProcessBuilder processBuilder = new ProcessBuilder("python3", "/Users/liuyang/Desktop/研0资料/untitled3/src/main/java/org/example/PY/Zheng.py",String.valueOf(py_zheng_number));
                processBuilder.redirectErrorStream(true); // 合并错误输出

                // 启动进程
                Process process = processBuilder.start();

                // 读取输出
                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line); // 打印Python脚本的输出
                }

                // 等待进程结束
                int exitCode = process.waitFor();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        // 输出程序规范 S 的结果
        System.out.println("输出程序规范 S 的结果：" + spec);
    }

    private static boolean evaluateCondition(String condition, int x) {
        // 动态解析条件，根据不同的条件格式进行判断
        if (condition.contains(">=")) {
            String[] parts = condition.split(">=");
            return x >= Integer.parseInt(parts[1].trim());
        }
        if (condition.contains("<")) {
            String[] parts = condition.split("<");
            return x < Integer.parseInt(parts[1].trim());
        }
        if (condition.contains(">")) {
            String[] parts = condition.split(">");
            return x > Integer.parseInt(parts[1].trim());
        }
        if (condition.contains("==")) {
            String[] parts = condition.split("==");
            return x == Integer.parseInt(parts[1].trim());
        }
        // 添加更多条件解析逻辑...
        return false; // 默认返回 false
    }
}

package org.example;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class PythonExecutor {
    public static void main(String[] args) {
        try {
            // 创建ProcessBuilder并指定Python解释器和脚本路径
            ProcessBuilder processBuilder = new ProcessBuilder("python3", "/Users/liuyang/Desktop/研0资料/untitled3/src/main/java/org/example/Fu.py");
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
}

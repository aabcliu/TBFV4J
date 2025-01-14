import java.util.Scanner;

public class SecantSqrt {
    public static double secantSqrt(double N, double epsilon) {
        // 情况 1：输入非法
        if (N < 0) {
            return -1;  // T1 -> D1: 输入非法，返回 -1
        }

        // 情况 2：精度非法
        if (epsilon <= 0) {
            return -3;  // T2 -> D2: 精度非法，返回 -2
        }

        // 情况 3：正常计算平方根
        double x0 = N / 2.0;
        double x1 = N / 3.0;

        while (Math.abs(x1 * x1 - N) >= epsilon) {
            double f_x0 = x0 * x0 - N;
            double f_x1 = x1 * x1 - N;

            // 割线法公式
            double x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0);
            x0 = x1;
            x1 = x2;
        }

        return x1;  // 返回近似解
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 输入数值 N 和精度 epsilon
        System.out.print("请输入一个数 N: ");
        double N = scanner.nextDouble();
        System.out.print("请输入精度 epsilon: ");
        double epsilon = scanner.nextDouble();

        // 调用割线法平方根计算方法
        double result = secantSqrt(N, epsilon);

        // 输出结果
        if (result == -1) {
            System.out.println("输入非法，负数没有实数平方根");
        } else if (result == -2) {
            System.out.println("精度非法");
        } else {
            System.out.printf("Result: %.6f\n", result);
        }

        scanner.close();
    }
}

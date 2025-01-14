import java.util.Scanner;

public class NewtonSqrt {
    public static double newtonSqrt(double N, double epsilon) {
        // 检查输入合法性
        if (N < 0) {
            return -1.0; // 返回 -1 表示输入非法
        } else if (epsilon <= 0) {
            return -2.0; // 返回 -2 表示输入非法
        }
        double x_n = N / 2.0; // 初始猜测
        while (Math.abs(x_n * x_n - N) >= epsilon) {
            x_n = 0.5 * (x_n + N / x_n); // 牛顿迭代公式
        }

        return x_n; // 返回最终平方根
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 输入待求平方根的数和精度
        System.out.print("请输入一个数 N: ");
        double N = scanner.nextDouble();
        System.out.print("请输入精度 epsilon: ");
        double epsilon = scanner.nextDouble();

        // 调用牛顿法计算平方根
        Double result = newtonSqrt(N, epsilon);

        if (result == -1.0) {
            System.out.println("输入的数字无效");
        }else if (result == -2.0) {
            System.out.println("输入的精度无效");
        }else {
            System.out.println("计算得到的平方根为: " + result);
        }

        scanner.close();
    }
}

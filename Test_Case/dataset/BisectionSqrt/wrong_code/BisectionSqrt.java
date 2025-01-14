import java.util.Scanner;

public class BisectionSqrt {
    public static double bisectionSqrt(double N, double epsilon) {
        if (epsilon <= 0) {
            return -2;  // 精度非法
        }
        else if (N < 0) {
            return -1;  // 输入非法
        } 

        double low = 0, high = Math.max(1, N);  // 初始化区间
        while (high - low > epsilon) {
            double mid = (low + high) / 2;
            if (mid * mid < N) {
                low = mid;
            } else {
                high = mid;
            }
        }

        return (low + high) / 2;  // 返回近似解
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("请输入一个数 N: ");
        double N = scanner.nextDouble();
        System.out.print("请输入精度 epsilon: ");
        double epsilon = scanner.nextDouble();

        double result = bisectionSqrt(N, epsilon);
        if (result == -1) {
            System.out.println("输入非法，负数没有实数平方根");
        } else if (result == -2) {
            System.out.println("精度非法");
        } else {
            System.out.println("Result: " + result);
        }

        scanner.close();
    }
}

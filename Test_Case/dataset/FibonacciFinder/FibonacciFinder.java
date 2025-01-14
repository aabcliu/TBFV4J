import java.util.Scanner;

public class FibonacciFinder {
    // 计算斐波那契数的通项公式
    public static double fibonacci(int k){
        double phi = (1 + Math.sqrt(5)) / 2; // 黄金比例
        double psi = (1 - Math.sqrt(5)) / 2; // 负的黄金比例
        return (Math.pow(phi, k) - Math.pow(psi, k)) / Math.sqrt(5);
    }
    // 找到第一个大于 n 的斐波那契数
    public static int findFib(int n){
        if(n<=0){
            return 1;
        }
        int k = 0;
        double fib;
        // 找到第一个大于 n 的斐波那契数
        do{
            fib = fibonacci(k);
            k++;
        } while (fib <= n);

        return k - 1; // 返回索引
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入一个整数 n: ");
        int n = scanner.nextInt();

        int index = findFib(n);
        double result = fibonacci(index);

        System.out.printf("第 %d 项斐波那契数: %.0f\n", index, result);
    }
}
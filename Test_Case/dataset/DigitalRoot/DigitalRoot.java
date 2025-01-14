import java.util.Scanner;

public class DigitalRoot{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        // 输入 A 和 n
        System.out.print("请输入整数 A: ");
        int A = scanner.nextInt();
        System.out.print("请输入整数 n: ");
        int n = scanner.nextInt();
        // 计算结果
        String result = findMaxDigitalRoot(A, n);
        System.out.println("结果: " + result);
    }
    private static String findMaxDigitalRoot(int A, int n){
        // 错误判断逻辑
        if(n > 9 || n < -9 || (A <= 0 && n > 0) || (A < 0 && n >= 0)){
            return "error_code";
        }
        // n = 0 的特殊情况
        if(n == 0 && A >= 0){
            return "0";
        }
        // 从 A 开始向下寻找
        for(int i = A; i >= Integer.MIN_VALUE; i=i-1){
            int digitalRoot;
            if(i == 0) digitalRoot = 0;
            else if(i > 0){
                digitalRoot = 1 + (i - 1) % 9;
            }
            else{
                digitalRoot = -(1 + (-i - 1) % 9);
            }
            if(digitalRoot == n){
                return String.valueOf(i);
            }
        }
        return "没有找到符合条件的数字";
    }
}
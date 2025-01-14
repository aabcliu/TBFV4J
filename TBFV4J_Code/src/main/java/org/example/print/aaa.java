package org.example.print;
import java.util.Scanner;
//        long startTime = System.nanoTime();
//        // 计算并输出总的运行时间
//                long endTime = System.nanoTime();
//                long totalTime = endTime - startTime;
//                System.out.println("Total running time: " + totalTime/ 1_000_000_000.0 + " seconds");
//
//

//public class aaa {
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        long startTime = System.nanoTime();
//        int x=scanner.nextInt();
//        System.out.print(x);
//        int y=0;
//        while(x>=0){
//            x=x-1;
//            y=y+1;
//        }
//        y=y-1;
//        System.out.println("  "+y);
//        long endTime = System.nanoTime();
//        long totalTime = endTime - startTime;
//        System.out.println("Total running time: " + totalTime/ 1_000_000_000.0 + " seconds");
//    }
//}

//public class aaa {
//    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        long startTime = System.nanoTime();
//        int x = scanner.nextInt();
//        if(x < 0){
//            System.out.println("Evaluating if condition: x < 0 is evaluated as: " + (x < 0));
//            System.out.println("Result: none");
//        }else{
//            int sum = 0;
//            System.out.println("sum = 0, current value of sum: " + sum);
//            int n = 1;
//            System.out.println("n = 1, current value of n: " + n);
//            boolean breakEncountered = true;
//            while(sum < x){
//                System.out.println("sum = " + sum);
//                System.out.println("x = " + x);
//                System.out.println("Entering loop with condition: sum < x is evaluated as: " + (sum < x));
//                sum=sum+n;
//                System.out.println("sum = sum+n, current value of sum: " + sum);
//                n=n+1;
//                System.out.println("n = n+1, current value of n: " + n);
//            }
//            if (breakEncountered) {
//                System.out.println("Exiting loop, condition no longer holds: sum < x is evaluated as: " + (sum < x));
//            }
//            System.out.println("Result: " + n);
//        }
//        long endTime = System.nanoTime();long totalTime = endTime - startTime;System.out.println("Total running time: " + totalTime/ 1_000_000_000.0 + " seconds");
//        scanner.close();
//    }
//}

//public class aaa{
//    public static void main(String[] args) {
//        final double g = 9.8;
//        Scanner scanner = new Scanner(System.in);
//        long startTime = System.nanoTime();
//        double h0 = scanner.nextDouble();
//        double y = scanner.nextDouble();
//        if(y < 0){
//            System.out.println("Distance cannot be negative.");
//        }else if(y > h0){
//            System.out.println("Fall distance exceeds initial height.");
//        }else{
//            double currentDistance = 0;
//            int t = 0;
//            double V = 0;
//            while(currentDistance < y){
//                t=t+1;
//                currentDistance = 0.5 * (g) * (t) * (t);
//                V = (g) * (t);
//                if(currentDistance >= y){
//                    break;
//                }
//            }
//            System.out.println("Time after falling " + currentDistance + " meters from initial height " + h0 + " meters: " + t + " seconds.");
//            System.out.println("Speed at that moment: " + V + " m/s.");
//        }
//        scanner.close();
//        long endTime = System.nanoTime();long totalTime = endTime - startTime;System.out.println("Total running time: " + totalTime/ 1_000_000_000.0 + " seconds");
//    }
//}





//public class aaa {
//    public static int maxPyramidLayers(int N){
//        // 如果 N 小于等于 0，直接返回 0
//        if(N <= 0){
//            return 0;
//        }
//        int result = 0;
//        while(true){
//            // 计算当前层数的砖块需求
//            int currentBricks = (result * (result + 1) * (2 * result + 1)) / 6;    //
//            // 计算下一层的砖块需求
//            int nextBricks = ((result + 1) * (result + 2) * (2 * result + 3)) / 6;   //n=1  current=0  next=1
//            // 检查当前砖块需求是否在范围内
//            if(currentBricks <= N && N < nextBricks){
//                break;
//            }
//            // 增加层数
//            result=result+1;
//        }
//        return result;
//    }
//    public static void main(String[] args){
//        Scanner scanner = new Scanner(System.in);
//        long startTime = System.nanoTime();
//        int N = scanner.nextInt();; // 你可以修改这个值来测试不同的输入
//        int result=maxPyramidLayers(N);
//        System.out.println("可以构建的金字塔层数: " + result);
//        long endTime = System.nanoTime();long totalTime = endTime - startTime;System.out.println("Total running time: " + totalTime/ 1_000_000_000.0 + " seconds");
//    }
//}


public class aaa{
    // 初始模式，0 表示控制权由开发板管理
    private static int mode = 0;
    // 定义一个内部类用于返回多个值
    public static class Result{
        int mode;
        boolean state;
        public Result(int mode, boolean state){
            this.mode = mode;
            System.out.println("mode = mode, current value of mode: " + mode);
            this.state = state;
            System.out.println("state = state, current value of state: " + state);
        }
        @Override
        public String toString(){
            return "mode: " + mode + ", state: " + state;
        }
    }
    public static Result setLED(int msg){
        boolean state = true;
        System.out.println("state = true, current value of state: " + state);
// 根据不同的 msg 值设置 mode 和 state
        if(msg == 0) {
            System.out.println("Evaluating if condition: msg == 0 is evaluated as: " + (msg == 0));
            mode = 1;
            System.out.println("mode = 1, current value of mode: " + mode);
            state = true;
            System.out.println("state = true, current value of state: " + state);
        }else if(msg == 1){
            System.out.println("Evaluating if condition: msg == 1 is evaluated as: " + (msg == 1));
            mode = 1;
            System.out.println("mode = 1, current value of mode: " + mode);
            state = false;
            System.out.println("state = false, current value of state: " + state);
        }else if (msg == 2){
            mode = 0;  // 控制权返还给开发板
            System.out.println("mode = 0, current value of mode: " + mode);
            state = false;
            System.out.println("state = false, current value of state: " + state);
        }else{
            System.out.println("Invalid command");
            return new Result(mode, false);  // 返回当前 mode 和无效的 state
        }
// 返回 mode 和 tate 的结果
        return new Result(mode, state);
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        long startTime = System.nanoTime();
        System.out.print("请输入指令 (0: 打开, 1: 关闭, 2: 返还控制权): ");
        int msg = scanner.nextInt();
        Result result = setLED(msg);  // 获取返回的结果
        System.out.println("result = setLED(msg), current value of result: " + result);
        System.out.println(result);    // 打印结果
        long endTime = System.nanoTime();long totalTime = endTime - startTime;System.out.println("Total running time: " + totalTime/ 1_000_000_000.0 + " seconds");
        scanner.close();

    }
}
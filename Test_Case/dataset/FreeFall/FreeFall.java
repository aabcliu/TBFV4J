import java.util.Scanner;

public class FreeFallSpeedAtDistanceWithTimeLoop {
    public static void main(String[] args) {
        // 常量定义
        final double g = 9.8;  // 重力加速度（m/s^2）
        // 创建扫描器，读取用户输入的初始高度和目标下落距离
        Scanner scanner = new Scanner(System.in);
        // 输入初始高度 h0
        System.out.print("Enter the initial height (h0) in meters: ");
        double h0 = scanner.nextDouble();
        // 输入目标下落距离 y
        System.out.print("Enter the fall distance (y) in meters: ");
        double y = scanner.nextDouble();
        // 检查目标下落距离是否合理
        if(y < 0){
            System.out.println("Distance cannot be negative.");
        }else if(y > h0){
            System.out.println("Fall distance exceeds initial height.");
        }else{
            // 初始化下落距离和时间
            double currentDistance = 0;
            int t = 0;  // 初始时间
            double V = 0;  // 速度
            // 循环计算下落过程，每次时间 t 增加 1 秒
            while(currentDistance < y){
                t=t+1;  // 增加 1 秒时间
                // 计算当前时间 t 的下落距离
                currentDistance = 0.5 * g * t * t;  // y = 1/2 * g * t^2
                // 计算当前时刻的速度
                V = g * t;  // v = g * t
                // 如果下落距离已经超过目标距离，跳出循环
                if(currentDistance >= y){
                    break;
                }
            }
            // 输出结果
            System.out.println("Time after falling " + currentDistance + " meters from initial height " + h0 + " meters: " + t + " seconds.");
            System.out.println("Speed at that moment: " + V + " m/s.");
        }
        scanner.close();
    }
}

import java.util.Scanner;

public class SetLed {
    // 初始模式，0 表示控制权由开发板管理
    private static int mode = 0;

    // 定义一个内部类用于返回多个值
    public static class Result {
        int mode;
        boolean state;

        public Result(int mode, boolean state) {
            this.mode = mode;
            this.state = state;
        }

        @Override
        public String toString() {
            return "mode: " + mode + ", state: " + state;
        }
    }

    // 控制 LED 的方法
    // on=0, off=1, con=2 表示打开、关闭和控制权返还给开发板
    public static Result setLED(int msg) {
        boolean state = true;
        
        // 根据不同的 msg 值设置 mode 和 state
        if (msg == 0) {
            mode = 0;//wrong code
            state = true;
        } else if (msg == 1) {
            mode = 1;
            state = false;
        } else if (msg == 2) {
            mode = 0;  // 控制权返还给开发板
            state = false;
        } else {
            System.out.println("Invalid command");
            return new Result(mode, false);  // 返回当前 mode 和无效的 state
        }

        // 返回 mode 和 state 的结果
        return new Result(mode, state);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入指令 (0: 打开, 1: 关闭, 2: 返还控制权): ");
        int msg = scanner.nextInt();
        Result result = setLED(msg);  // 获取返回的结果
        System.out.println(result);    // 打印结果
        scanner.close();
    }
}

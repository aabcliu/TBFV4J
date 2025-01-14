import java.util.Scanner;

public class IsGetTempTime {
    // 定义常量
    private static final long UINT32_MAX = 0xFFFFFFFFL;  // uint32_t 最大值
    private static final long TIME_INTERVAL = 5000;      // 时间间隔 5 秒 (5000 毫秒)
    private static long startTick = 0;                   // 用于记录上次操作时间点

    // 获取当前时间戳（模拟 HAL_GetTick 的行为）
    public static long getTick() {
        return System.currentTimeMillis() & UINT32_MAX;  // 模拟 uint32_t 溢出行为
    }

    // 检查是否满足读取温度的时间间隔
    // 为了模拟规约，将 curTick 作为参数传入
    public static boolean isGetTempTime(long curTick) {
        boolean readFlag = false;

        if (curTick >= startTick) {
            // 正常情况，无溢出
            if (curTick - startTick >= TIME_INTERVAL) {
                readFlag = true;
            }
        }
        /*  
        else {
            // 处理时间戳溢出情况
            if ((UINT32_MAX - startTick + curTick) >= TIME_INTERVAL) {
                readFlag = true;
            }
        }
        */
        // 如果时间间隔满足条件，更新 startTick
        if (readFlag) {
            startTick = curTick;
        }
        return readFlag;
    }

    // 主方法，用于测试 isGetTempTime
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入当前时间戳：");
        long curTick = scanner.nextLong();
        boolean result = isGetTempTime(curTick);
        System.out.println("是否满足读取温度的时间间隔条件: " + result);
        scanner.close();
    }
}


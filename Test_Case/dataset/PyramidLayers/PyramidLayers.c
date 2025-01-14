#include <stdio.h>

int maxPyramidLayers(int N) {
    // 如果 N 小于等于 0，直接返回 0
    if (N <= 0) {
        return 0;
    }

    int result = 0;

    while (1) {
        // 计算当前层数的砖块需求
        int currentBricks = (result * (result + 1) * (2 * result + 1)) / 6;
        // 计算下一层的砖块需求
        int nextBricks = ((result + 1) * (result + 2) * (2 * (result + 1) + 1)) / 6;
        // 检查当前砖块需求是否在范围内
        if (currentBricks <= N && N < nextBricks) {
            break;
        }
        // 增加层数
        result++;
    }

    return result;
}

int main() {
    int N = 14; // 你可以修改这个值来测试不同的输入
    printf("可以构建的金字塔层数: %d\n", maxPyramidLayers(N));
    return 0;
}
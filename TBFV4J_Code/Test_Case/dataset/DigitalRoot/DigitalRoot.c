#include <stdio.h>
#include <limits.h>

const char* findMaxDigitalRoot(int A, int n) {
    // 错误判断逻辑
    if (n > 9 || n < -9 || (A <= 0 && n > 0) || (A < 0 && n >= 0)) {
        return "error_code";
    }
    
    // n = 0 的特殊情况
    if (n == 0 && A >= 0) {
        return "0";
    }
    
    // 从 A 开始向下寻找
    for (int i = A; i >= INT_MIN; i--) {
        int digitalRoot;
        if (i == 0) {
            digitalRoot = 0;
        } else if (i > 0) {
            digitalRoot = 1 + (i - 1) % 9;
        } else {
            digitalRoot = -(1 + (-i - 1) % 9);
        }
        
        if (digitalRoot == n) {
            static char result[12]; // 足够大的缓冲区
            snprintf(result, sizeof(result), "%d", i);
            return result;
        }
    }
    
    return "没有找到符合条件的数字";
}

int main() {
    int A, n;
    printf("请输入整数 A: ");
    scanf("%d", &A);
    printf("请输入整数 n: ");
    scanf("%d", &n);
    
    const char* result = findMaxDigitalRoot(A, n);
    printf("结果: %s\n", result);
    return 0;
}
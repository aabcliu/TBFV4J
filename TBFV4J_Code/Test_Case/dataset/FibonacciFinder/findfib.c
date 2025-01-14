#include <stdio.h>
#include <math.h>

// 计算斐波那契数的通项公式
double fibonacci(int k) {
    double phi = (1 + sqrt(5)) / 2; // 黄金比例
    double psi = (1 - sqrt(5)) / 2; // 负的黄金比例
    return (pow(phi, k) - pow(psi, k)) / sqrt(5);
}

int findFirstFibonacciGreaterThanN(int n) {
    int k = 0;
    double fib;

    // 找到第一个大于 n 的斐波那契数
    do {
        fib = fibonacci(k);
        k++;
    } while (fib <= n);

    return k - 1; // 返回索引
}

int main() {
    int n;
    printf("请输入一个整数 n: ");
    scanf("%d", &n);

    int index = findFirstFibonacciGreaterThanN(n);
    double result = fibonacci(index);

    printf("第 %d 项斐波那契数: %.0f\n", index, result);
    return 0;
}
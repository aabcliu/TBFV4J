package org.example.print;

import java.util.Scanner;
import java.math.*;

public class UserInputProgram{
    public static String calculateSquareSumUntilX(int x){
        if(x <= 0){
            System.out.println("Evaluating if condition: x <= 0 is evaluated as: " + (x <= 0));
            return "Invalid input, please enter a number greater than 0";
        }
        long sum = 0;
        System.out.println("sum = 0, current value of sum: " + sum);
        int N = 0;
        System.out.println("N = 0, current value of N: " + N);
        boolean breakEncountered = true;
        while(sum < x){
            System.out.println("sum = " + sum);
            System.out.println("x = " + x);
            System.out.println("Entering loop with condition: sum < x is evaluated as: " + (sum < x));
            N=(N)+1;
            System.out.println("N = (N)+1, current value of N: " + N);
            sum =sum + ((N) * (N) * (N));
            System.out.println("sum = sum + ((N) * (N) * (N)), current value of sum: " + sum);
        }
        if (breakEncountered) {
            System.out.println("Exiting loop, condition no longer holds: sum < x is evaluated as: " + (sum < x));
        }
        System.out.println("N = " + N);
        return "N = " + N;
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        String result = calculateSquareSumUntilX(x);
        scanner.close();
    }
}
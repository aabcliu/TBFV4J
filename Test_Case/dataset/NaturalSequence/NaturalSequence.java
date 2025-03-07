import java.util.Scanner;
public class UserInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Prompts the user for x
        System.out.print("Please enter a number x: ");
        int x = scanner.nextInt();
        int n;
        // Determine if x is less than 0
        if(x < 0){
            n = -1;
            System.out.println("Result: none");  // If x is less than 0, output "none"
        }else if(x == 0){
            n = 0;
            System.out.println("Result: 0");  // If x is equal to 0, it outputs 0
        }else{
            int sum = 0;
            n = 1;
            // Add natural numbers until the sum >= x
            while(sum < x){
                sum =sum + n;
                n=n + 1;
            }
            // At the end of the loop, subtract 1 from n so that it meets the condition
            n=n - 1; // Make sure n is the minimum value that satisfies the condition
            // Output the current natural number n
            System.out.println("Result: " + n);
        }
        scanner.close();  // Turn off Scanner
    }
}

Test Codition: x>0
Define Codition:(n+1)*(n)/2>=x && (n-1)*(n)/2<x
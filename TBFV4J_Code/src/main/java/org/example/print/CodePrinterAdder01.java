package org.example.print;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
//该程序的功能：给出java代码，返回带有打印语句的java代码。

public class CodePrinterAdder01 {

    public static String addPrintStatements(String code) {
        StringBuilder result = new StringBuilder();
        String[] lines = code.split("\n");

        Pattern whilePattern = Pattern.compile("while\\((.*?)\\)");
        Pattern ifBreakPattern = Pattern.compile("if\\((.*?)\\) break;");
        Pattern ifPattern = Pattern.compile("if\\((.*?)\\)");
        Pattern assignmentPattern = Pattern.compile("(\\w+)\\s*(\\+\\+|--|=|\\+=|-=|\\*=|/=)\\s*(.*?);");

        boolean insideLoop = false;
        String loopCondition = "";
        boolean breakEncountered = false;

        for (String line : lines) {
            line = line.trim();
            Matcher whileMatcher = whilePattern.matcher(line);
            Matcher ifMatcher = ifPattern.matcher(line);
            Matcher ifBreakMatcher = ifBreakPattern.matcher(line);
            Matcher assignmentMatcher = assignmentPattern.matcher(line);

            // Skip scanner-related print statements and ensure proper handling of scanner.nextDouble() and nextInt()
            if (line.contains("scanner = new Scanner(System.in)")) {
                result.append(line).append("\n"); // Add the Scanner initialization
                continue;  // Skip adding print statements for the Scanner initialization
            }

            // Skip assignment statements involving scanner.nextInt() or scanner.nextDouble()
            if (line.contains("scanner.nextInt()") || line.contains("scanner.nextDouble()")) {
                result.append(line).append("\n");
                continue;
            }

            // Handle while loops
            if (whileMatcher.find()) {
                insideLoop = true;
                loopCondition = whileMatcher.group(1); // Extract loop condition
                result.append("boolean breakEncountered = true;\n"); // Declare the breakEncountered variable
                result.append(line).append("\n");

                // Print variables in the loop condition
                Matcher variableMatcher = Pattern.compile("\\b([a-zA-Z_][a-zA-Z0-9_]*)\\b").matcher(loopCondition);
                while (variableMatcher.find()) {
                    String variable = variableMatcher.group(1);
                    if (!variable.equals("true") && !variable.equals("false")) {  // Avoid printing for boolean literals
                        result.append("System.out.println(\"" + variable + " = \" + " + variable + ");\n");
                    }
                }

                // Print the loop condition's evaluation
                result.append("System.out.println(\"Entering loop with condition: " + loopCondition + " is evaluated as: \" + (" + loopCondition + "));\n");
                continue;
            }

            // Handle if-break statements
            if (ifBreakMatcher.find()) {
                String condition = ifBreakMatcher.group(1);
                result.append("if(").append(condition).append(") {\n");
                result.append("    System.out.println(\"Condition " + condition + " is met, breaking the loop.\");\n");
                result.append("    breakEncountered = false;\n");
                result.append("    break;\n");
                result.append("}\n");
                continue;
            }

            // Handle if statements (not if-break)
            if (ifMatcher.find() && !line.contains("break;")) {
                String condition = ifMatcher.group(1);
                result.append(line).append("\n");
                result.append("System.out.println(\"Evaluating if condition: " + condition + " is evaluated as: \" + (" + condition + "));\n");
                continue;
            }

            // Handle assignment and updates
            if (assignmentMatcher.find()) {
                String variable = assignmentMatcher.group(1);
                String operator = assignmentMatcher.group(2);
                String expression = assignmentMatcher.group(3);
                result.append(line).append("\n");
                result.append("System.out.println(\"" + variable + " " + operator + " " + expression + ", current value of " + variable + ": \" + " + variable + ");\n");
                continue;
            }

            // Default: append the line without changes
            result.append(line).append("\n");

            // Handle loop exit (closing brace of a while loop)
            if (insideLoop && line.equals("}")) {
                result.append("if (breakEncountered) {\n");
                result.append("    System.out.println(\"Exiting loop, condition no longer holds: " + loopCondition + " is evaluated as: \" + (" + loopCondition + "));\n");
                result.append("}\n");
                insideLoop = false; // Reset loop state
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please enter your Java code (end with an empty line):");
        StringBuilder userInputCode = new StringBuilder();
        String line;
        while (!(line = scanner.nextLine()).isEmpty()) {
            userInputCode.append(line).append("\n");
        }

        // Add print statements to the code
        String codeWithPrints = addPrintStatements(userInputCode.toString());
        System.out.println("Code with added print statements:\n" + codeWithPrints);
    }
}

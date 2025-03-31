package org.example.print;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class CodePrinterAdder {
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

            if (line.contains("scanner = new Scanner(System.in)")) {
                result.append(line).append("\n");
                continue;
            }

            if (line.contains("scanner.nextInt()") || line.contains("scanner.nextDouble()")) {
                result.append(line).append("\n");
                continue;
            }

            if (whileMatcher.find()) {
                insideLoop = true;
                loopCondition = whileMatcher.group(1);
                result.append("boolean breakEncountered = true;\n");
                result.append(line).append("\n");

                Matcher variableMatcher = Pattern.compile("\\b([a-zA-Z_][a-zA-Z0-9_]*)\\b").matcher(loopCondition);
                while (variableMatcher.find()) {
                    String variable = variableMatcher.group(1);
                    if (!variable.equals("true") && !variable.equals("false")) {
                        result.append("System.out.println(\"" + variable + " = \" + " + variable + ");\n");
                    }
                }

                result.append("System.out.println(\"Entering loop with condition: " + loopCondition + " is evaluated as: \" + (" + loopCondition + "));\n");
                continue;
            }

            if (ifBreakMatcher.find()) {
                String condition = ifBreakMatcher.group(1);
                result.append("if(").append(condition).append(") {\n");
                result.append("    System.out.println(\"Condition " + condition + " is met, breaking the loop.\");\n");
                result.append("    breakEncountered = false;\n");
                result.append("    break;\n");
                result.append("}\n");
                continue;
            }

            if (ifMatcher.find() && !line.contains("break;")) {
                String condition = ifMatcher.group(1);
                result.append(line).append("\n");
                result.append("System.out.println(\"Evaluating if condition: " + condition + " is evaluated as: \" + (" + condition + "));\n");
                continue;
            }

            if (assignmentMatcher.find()) {
                String variable = assignmentMatcher.group(1);
                String operator = assignmentMatcher.group(2);
                String expression = assignmentMatcher.group(3);
                result.append(line).append("\n");
                result.append("System.out.println(\"" + variable + " " + operator + " " + expression + ", current value of " + variable + ": \" + " + variable + ");\n");
                continue;
            }

            result.append(line).append("\n");

            if (insideLoop && line.equals("}")) {
                result.append("if (breakEncountered) {\n");
                result.append("    System.out.println(\"Exiting loop, condition no longer holds: " + loopCondition + " is evaluated as: \" + (" + loopCondition + "));\n");
                result.append("}\n");
                insideLoop = false;
            }
        }

        return result.toString();
    }

    public static void writeToFile(String content, String fileName) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            writer.write(content);
            System.out.println("Add the code has been written to the file after print statements " + fileName);
        } catch (IOException e) {
            System.out.println("写入文件时发生错误: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please enter your Java code (end with a blank line) :");
        StringBuilder userInputCode = new StringBuilder();
        String line;
        while (!(line = scanner.nextLine()).isEmpty()) {
            userInputCode.append(line).append("\n");
        }

        String codeWithPrints = addPrintStatements(userInputCode.toString());

        String fileName = "ModifiedUserInputProgram.txt";

        writeToFile(codeWithPrints, fileName);
    }
}


TBFV4J: An automated testing-based formal verification tool for
Java

Step1:Download TBFV4J from github

First, we need to download the project from GitHub to the local environment. The project consists mainly of two components: the first part is the executable source code of TBFV4J--TBFV4J_Code, and the second part is the TBFV4J dataset--Test Case/dataset. After downloading the project to the local environment, extract the files, and upon completion, import TBFV4J into IntelliJ IDEA.

Step2:Run CodePrinterAdder
The specific location of this class is `org/example/print/CodePrinterAdder.java'. Running the CodePrinterAdder class is the first step in TBFV4J.The primary function of the `CodePrinterAdder' class is to analyze user-provided Java code and generate complete code with embedded debugging output statements. We hope that users can directly use the test code provided in our dataset for testing. Of course, users can also use their own Java code for experiments, but the code used for testing must meet the following three requirements:

1. TBFV4J requires that test code should not contain unnecessary empty lines, as empty lines represent the end of input.

2. TBFV4J requires that spaces before and after parentheses in the test code should be removed as much as possible.

3. For variables used in the code, such as variable x, try to enclose the variable in a pair of parentheses.

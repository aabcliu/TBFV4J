
TBFV4J: An automated testing-based formal verification tool for
Java

***Step1:Download TBFV4J from github***

First, we need to download the project from GitHub to the local environment. The project consists mainly of two components: the first part is the executable source code of TBFV4J--TBFV4J_Code, and the second part is the TBFV4J dataset--Test Case/dataset. After downloading the project to the local environment, extract the files, and upon completion, import TBFV4J into IntelliJ IDEA.

***Step2:Run CodePrinterAdder***

The specific location of this class is `org/example/print/CodePrinterAdder.java'. Running the CodePrinterAdder class is the first step in TBFV4J.The primary function of the ：CodePrinterAdder class is to analyze user-provided Java code and generate complete code with embedded debugging output statements. We hope that users can directly use the test code provided in our dataset for testing. Of course, users can also use their own Java code for experiments, but the code used for testing must meet the following three requirements:

1. TBFV4J requires that test code should not contain unnecessary empty lines, as empty lines represent the end of input.

2. TBFV4J requires that spaces before and after parentheses in the test code should be removed as much as possible.

3. For variables used in the code, such as variable x, try to enclose the variable in a pair of parentheses.

The result returned by CodePrinterAdder is the processed Java code, which can be directly copied and executed, or used as input for the next stage.

***Step3:Run Dynamic Testing***

After executing the CodePrinterAdder class, the program generates complete code with embedded debugging output statements (we also provide Java code for the Dynamic Testing class in the dataset, which can be executed directly).  Users can remove redundant debugging statements as needed or use the generated code directly to execute the `Dynamic Testing' class.After the Java code to be validated is entered, TBFV4J will ask the user to input the Testing Condition, Defining Condition, and the maximum number of iterations. In the dataset we provide, complete Z3 specifications have already been included. Users can directly copy and input them.

# TBFV4J: An automated testing-based formal verification tool for Java
# Introduction

## Background

The Test-Based Formal Verification (TBFV) tool presented in this paper integrates Specification-Based Testing and Formal Verification to automate the verification of whether a Java program adheres to its specifications. By employing a grey-box testing approach that leverages path exploration and constraint solving, TBFV eliminates the need for deriving loop invariants. 

Below are some TBFV-related papers also published by our research group:

| Publication                                                  | Published         | Paper Titile                                                 |
| ------------------------------------------------------------ | ----------------- | ------------------------------------------------------------ |
| [Turing-100. The Alan Turing Centenary](https://easychair.org/publications/volume/Turing-100) | June 22, 2012     | [Utilizing Hoare Logic to Strengthen Testing for Error Detection in Programs.](https://easychair.org/publications/paper/476) |
| [IEEE Transactions on Software Engineering](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32) | February 01, 2022 | [Automatic Test Case and Test Oracle Generation Based on Functional Scenarios in Formal Specifications for Conformance Testing](https://ieeexplore.ieee.org/document/9108630) |
| [IEEE Transactions on Software Engineering](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=32) | January 01,  2023 | [Enhancing the Capability of Testing-Based Formal Verification by Handling Operations in Software Packages](https://ieeexplore.ieee.org/document/9712239) |

## 

## Functionality

The tool evaluates functional scenarios and provides either a confirmation that the program meets the specified requirements or a counterexample demonstrating a violation. To manage computational complexity, a limit is set on the maximum number of generated test cases, corresponding to the number of explored paths.

The flow of TBFV4J is:

<p align="center">
  <img width="594" alt="<img width="449" alt="截屏2025-03-23 14 28 16" src="https://github.com/user-attachments/assets/6b1de6de-b93a-4376-aa74-7b9d7e66bc3e/>"
</p>

# Installation

## Download TBFV4J

### Build From Source

```
The GitHub repository: https://github.com/aabcliu/TBFV4J.git
GitHub command: gh repo clone aabcliu/TBFV4J
```
This project consists of two main components: the first component is the executable source code of TBFV4J, and the second component is the TBFV4J dataset. After downloading the project to the local environment, the first step is to extract the files. 

Once extraction is complete, import TBFV4J into the user's local integrated development environment (IDE), such as IntelliJ IDEA, Eclipse, or Visual Studio Code. We will take IntelliJ IDEA as an example and provide detailed installation and running instructions.

## Add TBFV4J to Your Project

Include the following dependency in your project build file:

### Maven

```xml
<dependencies>
        <dependency>
            <groupId>com.github.javaparser</groupId>
            <artifactId>javaparser-core</artifactId>
            <version>3.23.1</version>
        </dependency>
        <dependency>
            <groupId>com.microsoft.z3</groupId>
            <artifactId>z3</artifactId>
            <version>4.13.3</version>
        </dependency>
        <dependency>
            <groupId>org.codehaus.groovy</groupId>
            <artifactId>groovy-all</artifactId>
            <version>2.4.16</version>
        </dependency>
        <dependency>
            <groupId>com.github.jsqlparser</groupId>
            <artifactId>jsqlparser</artifactId>
            <version>3.1</version>
        </dependency>
    </dependencies>
```

# Quick Start

In the video link below, we demonstrate how to run a simple example using TBFV4J.Please watch the video to learn about all the features and capabilities supported by TBFV4J.

Follow the TBFV4J guide to write and run your own tests.

## Demo Video

[Click to view the demo video](https://www.youtube.com/watch?v=CwQAXF2Ki8A)



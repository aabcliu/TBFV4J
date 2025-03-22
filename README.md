
TBFV4J: An automated testing-based formal verification tool for
Java
# Introduction

## Background

The Test-Based Formal Verification (TBFV) tool presented in this paper integrates Specification-Based Testing and Formal Verification to automate the verification of whether a Java program adheres to its specifications. By employing a grey-box testing approach that leverages path exploration and constraint solving, TBFV eliminates the need for deriving loop invariants. 

## Functionality

The tool evaluates functional scenarios and provides either a confirmation that the program meets the specified requirements or a counterexample demonstrating a violation. To manage computational complexity, a limit is set on the maximum number of generated test cases, corresponding to the number of explored paths.

The flow of TBFV4J is:

<p align="center">
  <img width="594" alt="截屏2025-03-21 15 02 55" src="https://github.com/user-attachments/assets/fd924609-c02d-40e0-a823-48f8fd6f6faa" />
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



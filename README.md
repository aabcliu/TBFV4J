
TBFV4J: An automated testing-based formal verification tool for
Java
# Introduction

The Test-Based Formal Verification (TBFV) tool presented in this paper integrates Specification-Based Testing and Formal Verification to automate the verification of whether a Java program adheres to its specifications. By employing a grey-box testing approach that leverages path exploration and constraint solving, TBFV eliminates the need for deriving loop invariants.

The tool evaluates functional scenarios and provides either a confirmation that the program meets the specified requirements or a counterexample demonstrating a violation. To manage computational complexity, a limit is set on the maximum number of generated test cases, corresponding to the number of explored paths.

The flow of TBFV4J is:

<p align="center">
  <img width="594" alt="截屏2025-03-21 15 02 55" src="https://github.com/user-attachments/assets/fd924609-c02d-40e0-a823-48f8fd6f6faa" />
</p>

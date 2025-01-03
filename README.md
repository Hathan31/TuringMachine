Turing Machine: Vending Beverage Machine

Project Overview
This project implements a Turing Machine that simulates the functionality of a vending beverage machine. The machine allows users to select from three different beverages:
Fanta: $2
Coke: $5
Sprite: $8

The user can select one, two, or all three beverages, and the machine verifies the payment before dispensing the selected items. The machine operates based on a formal Turing Machine definition and transition function.

Features
Simulates a Turing Machine: Implements a deterministic Turing Machine with defined states, input, and tape alphabets.
Verifies Payments: Validates the payment for each selected beverage.
Flexible Selection: Allows selecting multiple beverages at once.
State Transitions Visualization: Displays the tape and state transitions step-by-step for educational purposes.
Handles Edge Cases: Automatically adjusts the tape boundaries as needed.

Formal Definition

Set of States: {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, ACCEPTED, REJECT}

Input Alphabet: {F, C, S, 2, 5, 8}

Tape Alphabet: {F, C, S, 2, 5, 8, E, X, Y, Z}

Transition Function: Defined in the TRANSITIONS dictionary.

Start State: q0

Accept State: ACCEPTED

Reject State: REJECT

Transitions

The Turing Machine follows the transitions defined in the TRANSITIONS dictionary. For example:

From q0, reading F transitions to q1, writing F, and moving the head to the right (R).

Payment validation transitions include state changes like q1 to q4 when reading 2 (price of Fanta).

For a detailed list of transitions, refer to the TRANSITIONS dictionary in the code.

How to Use

Run the Program:

python vending_machine.py

Input Beverage Selection:

Enter a string of beverages you wish to purchase (e.g., FCS for Fanta, Coke, and Sprite).

Observe Output:

The program will display the tape and state transitions step-by-step.

The final result will indicate whether the string was accepted (valid payment) or rejected (invalid payment).

Example

Input:

FCS

Output:

Initial Tape: ['F', 'C', 'S', 'E']
q0 [F] C S E q1
q1 [C] S E X q2
q2 [S] E Y q3
q3 [E] Z q6
...
Final Tape: ['X', 'Y', 'Z', 'E']
The string was accepted.

File Structure

vending_machine.py: Main script containing the Turing Machine implementation.

Educational Value

This project is ideal for demonstrating the practical application of Turing Machines in theoretical computation courses. It provides insights into state transitions, tape modifications, and how deterministic machines operate.

# OzQIS

# Full Implementation of Quantum Relative Entropy Calculation

## Overview

The `implementation/full_implementation.py` script calculates the **Quantum Information Science (QIS)** value by using quantum relative entropy to measure the similarity between quantum states. It does this by running a parameterized quantum circuit, computing the quantum state, and evaluating how close this state is to a reference state.

## Functionality

1. **Quantum Device Setup**: A 2-qubit quantum device is created using PennyLane for simulating quantum operations.

2. **Parameterized Quantum Circuit**: The circuit applies **RY** rotations on both qubits and a **CNOT** gate to entangle them. The circuit’s output state depends on the input parameters.

3. **Quantum State Calculation**: The quantum state vector is computed by applying the circuit with the given parameters.

4. **Quantum Relative Entropy**: This value is calculated by comparing the quantum states using the formula for relative entropy, which involves eigenvalue decomposition and logarithmic operations.

5. **Epochs**: The script runs through 50 epochs, randomly modifying the parameters in each epoch. For each new set of parameters, the relative entropy between the updated state and the initial state is computed.

6. **QIS Calculation**: The average relative entropy is normalized by the maximum entropy to compute the final QIS value, which indicates the similarity between the quantum states.

## Purpose

The purpose of the script is to present all operations mentioned in the article as a single, simple example, and it is recommended that you use 'implementation/library_implementation.py' in your own code.


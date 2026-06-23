# ⚛️ Quantum Algorithms Using Qiskit  
### Deutsch • Deutsch–Jozsa • Simon’s • Grover’s Algorithm

---

## 📌 Overview

This repository presents a structured implementation and analysis of foundational quantum algorithms using **Qiskit**. The project demonstrates how quantum computation achieves speedup over classical methods through:

- Quantum superposition  
- Interference  
- Phase kickback  
- Entanglement  
- Oracle-based computation  

The work progresses from basic quantum gates to advanced oracle-based algorithms, providing both theoretical insight and practical simulation results.

---

## 🎯 Objectives

- Implement fundamental quantum gates and visualize their effects  
- Generate and analyze Bell states (entanglement)  
- Demonstrate Deutsch’s Algorithm (1-bit oracle problem)  
- Implement Deutsch–Jozsa Algorithm (n-bit generalization)  
- Solve Simon’s Problem using quantum linear algebra over GF(2)  
- Implement Grover’s Search Algorithm for unstructured search  
- Validate quantum advantage using simulation results  

---

## 🧠 Algorithms Implemented

### 1. Quantum Gates & Bell States
- Pauli-X, Y, Z gates  
- Hadamard gate  
- CNOT gate  
- Bell state generation  
- Bloch sphere visualization  

📌 Demonstrates:
- Superposition
- Entanglement
- Statevector evolution

---

### 2. Deutsch’s Algorithm
Solves the problem of determining whether a function is constant or balanced using a single oracle query.

- Classical complexity: 2 evaluations  
- Quantum complexity: 1 evaluation  

📌 Key idea:
- Phase kickback + interference

---

### 3. Deutsch–Jozsa Algorithm
Generalization of Deutsch’s algorithm for n-bit functions.

- Classical complexity: \( O(2^{n}) \)  
- Quantum complexity: \( O(1) \)

For \( n = 5 \): classical requires 17 evaluations.

📌 Key idea:
- Global phase encoding
- Interference reveals structure

---

### 4. Simon’s Algorithm
Finds a hidden binary string \( s \) such that:

\[
f(x) = f(x \oplus s)
\]

- Classical complexity: exponential  
- Quantum complexity: linear \( O(n) \)

📌 Key idea:
- Measurement produces linear equations over GF(2)
- Solved using linear algebra

---

### 5. Grover’s Search Algorithm
Searches an unstructured database of size \( N \).

- Classical complexity: \( O(N) \)  
- Quantum complexity: \( O(\sqrt{N}) \)

📌 Key idea:
- Amplitude amplification
- Diffusion operator

---

## 🛠️ Tech Stack

- Python 3.x  
- Qiskit  
- Qiskit Aer Simulator  
- NumPy  
- Matplotlib  
- Jupyter Notebooks  

---

## 📁 Repository Structure

```text
notebooks/        → Interactive quantum experiments  
src/              → Modular quantum algorithm implementations  
deutsch-figures/  → Deutsch circuit results  
dj-figures/       → Deutsch–Jozsa results  
docs/             → Full theoretical documentation  

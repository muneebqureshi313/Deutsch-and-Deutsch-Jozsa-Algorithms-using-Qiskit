# Implementation and Analysis of Quantum Gates and Oracle-Based Quantum Algorithms Using Qiskit

**Author:** Muneeb Ur Rehman  
**Date:** 2026  

---

## Table of Contents

- [Quantum Gates and Bell States](#quantum-gates-and-bell-states)
- [Deutsch's Algorithm](#deutschs-algorithm)
- [Deutsch–Jozsa Algorithm](#deutschjozsa-algorithm)

---

# Quantum Gates and Bell States

## Objective

This section introduces fundamental quantum computing concepts using Qiskit, including single-qubit gates, entanglement, and Bell states.

---

## Theoretical Background

A qubit is represented as:

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle
$$

with normalization:

$$
|\alpha|^2 + |\beta|^2 = 1
$$

Quantum gates are unitary transformations that preserve this condition.

---

## Single-Qubit Gates

### Pauli-Y Gate

$$
Y =
\begin{bmatrix}
0 & -i \\
i & 0
\end{bmatrix}
$$

---

### Pauli-Z Gate

$$
Z =
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$

---

### Hadamard Gate

$$
H = \frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
$$

---

## CNOT Gate

$$
CNOT =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$

---

## Bell States

Bell states are maximally entangled quantum states.

### Φ⁺
$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

### Ψ⁺
$$
|\Psi^+\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}
$$

### Φ⁻
$$
|\Phi^-\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}}
$$

### Ψ⁻
$$
|\Psi^-\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}
$$

---

## Visualization Results

### Deutsch Circuit
![Deutsch Circuit](deutsch-figures/circuit.png)

### Deutsch Results
![Deutsch Results](deutsch-figures/result.png)

---

## Conclusion

Quantum gates and entanglement form the foundation of quantum computation. Bell states demonstrate how entanglement emerges from combining Hadamard and CNOT gates.

---

# Deutsch's Algorithm

## Objective

Determine whether a function is constant or balanced using a single oracle query.

---

## Function Definition

$$
f:\{0,1\} \rightarrow \{0,1\}
$$

---

## Classical Complexity

$$
N_{\text{classical}} = 2
$$

---

## Quantum Complexity

$$
N_{\text{quantum}} = 1
$$

---

## Oracle

$$
U_f |x,y\rangle = |x, y \oplus f(x)\rangle
$$

---

## Result

- 0 → Constant  
- 1 → Balanced  

---

# Deutsch–Jozsa Algorithm

## Objective

Generalization of Deutsch’s Algorithm for n-bit functions.

---

## Function

$$
f:\{0,1\}^n \rightarrow \{0,1\}
$$

---

## Classical Complexity

$$
N_{\text{classical}} = 2^{n-1} + 1
$$

For \( n = 5 \):

$$
17
$$

---

## Quantum Complexity

$$
N_{\text{quantum}} = 1
$$

---

## Final State

$$
|\psi\rangle = \frac{1}{\sqrt{2^n}} \sum_x (-1)^{f(x)} |x\rangle
$$

---

## Measurement Rule

- |000…0⟩ → Constant  
- Otherwise → Balanced  

---

## Visualization Results

### Deutsch–Jozsa Circuit
![DJ Circuit](dj-figures/circuit.png)

### DJ Results
![DJ Results](dj-figures/results.png)

---

## Final Conclusion

This project demonstrates quantum computational advantage through:

- Superposition  
- Interference  
- Phase kickback  
- Entanglement  

These algorithms form the foundation of modern quantum computing and quantum machine learning.

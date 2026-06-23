!pip install qiskit
!pip install qiskit_aer
!pip install pylatexenc
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# oracle function

def deutsch_function(case: int):
    # This function generates a quantum circuit for one of the 4 functions
    # from one bit to one bit

    if case not in [1, 2, 3, 4]:
        raise ValueError("`case` must be 1, 2, 3, or 4.")

    f = QuantumCircuit(2)
    if case in [2, 3]:
        f.cx(0, 1)
    if case in [3, 4]:
        f.x(1)
    return f


# case 1
# Run Deutsch's algorithm for Case 1 (constant function f(x) = 0)
f1 = deutsch_function(1)
print(f"Case 1: The function is {deutsch_algorithm(f1)}")

# Get the quantum circuit for Case 1 and plot histogram
qc_f1 = compile_circuit(f1)
simulator = AerSimulator()
result = simulator.run(qc_f1, shots=1024).result()
counts = result.get_counts(qc_f1)
print("Measurement results for Case 1:", counts)
display(plot_histogram(counts))


# Case 2
# Run Deutsch's algorithm for Case 2 (balanced function f(x) = x)
f2 = deutsch_function(2)
print(f"Case 2: The function is {deutsch_algorithm(f2)}")

# Get the quantum circuit for Case 2 and plot histogram
qc_f2 = compile_circuit(f2)
simulator = AerSimulator()
result = simulator.run(qc_f2, shots=1024).result()
counts = result.get_counts(qc_f2)
print("Measurement results for Case 2:", counts)
display(plot_histogram(counts))

# case 3

# Run Deutsch's algorithm for Case 3 (balanced function f(x) = NOT(x))
f3 = deutsch_function(3)
print(f"Case 3: The function is {deutsch_algorithm(f3)}")

# Get the quantum circuit for Case 3 and plot histogram
qc_f3 = compile_circuit(f3)
simulator = AerSimulator()
result = simulator.run(qc_f3, shots=1024).result()
counts = result.get_counts(qc_f3)
print("Measurement results for Case 3:", counts)
display(plot_histogram(counts))

# Case 4

# Run Deutsch's algorithm for Case 4 (constant function f(x) = 1)
f4 = deutsch_function(4)
print(f"Case 4: The function is {deutsch_algorithm(f4)}")

# Get the quantum circuit for Case 4 and plot histogram
qc_f4 = compile_circuit(f4)
simulator = AerSimulator()
result = simulator.run(qc_f4, shots=1024).result()
counts = result.get_counts(qc_f4)
print("Measurement results for Case 4:", counts)
display(plot_histogram(counts))

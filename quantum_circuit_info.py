from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram

print("Initializing Quantum Circuit...\n")

# Create a Quantum Circuit acting on a quantum register of one qubit
circuit = QuantumCircuit(1, 1)
print("Initial circuit:")
print(circuit)

print("\nAdding H gate on qubit 0 to put it in superposition...")

# Add a H gate on qubit 0, putting this qubit in superposition.
circuit.h(0)
print("\nCircuit after adding H gate:")
print(circuit)

print("\nAdding Measure gate to see the state...")

# Add a Measure gate to see the state.
circuit.measure([0], [0])
print("\nCircuit after adding Measure gate:")
print(circuit)

print("\nUsing Aer's qasm_simulator...")

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

print("\nExecuting the circuit on the qasm simulator...")

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab the results from the job
result = job.result()
print("\nExecution completed. Collecting results...")

# Get the counts (how many times we got 0 and how many times we got 1)
counts = result.get_counts(circuit)
print("\nTotal count for 0 and 1 are:", counts)

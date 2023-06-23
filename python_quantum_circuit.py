# -----------------------------------------------------------------------
# python_quantum_circuit.py
# Version: 1.0
# Author: Vell Void
# GitHub: https://github.com/VellVoid
# Twitter: https://twitter.com/VellVoid
# -----------------------------------------------------------------------

from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# Create a Quantum Circuit acting on a quantum register of one qubit
circuit = QuantumCircuit(1, 1)

# Add a H gate on qubit 0, putting this qubit in superposition.
circuit.h(0)

# Add a Measure gate to see the state.
circuit.measure([0], [0])

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab the results from the job
result = job.result()

# Get the counts (how many times we got 0 and how many times we got 1)
counts = result.get_counts(circuit)
print("\nTotal count for 0 and 1 are:",counts)

# Draw the circuit
print(circuit)

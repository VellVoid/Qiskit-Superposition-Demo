# -----------------------------------------------------------------------------
# qiskit_superposition_logging_experimental.py
#
# Description:
#   This script demonstrates the quantum superposition using Qiskit.
#
# Author: Vell Void
# Version: 1.8
#
# ────────────────────────────────────────────────────────────────────────
#
# For more information and updates, visit:
#   Twitter: https://twitter.com/VellVoid
#   Tweet: https://twitter.com/VellVoid/status/1672062894358294530
#
# License: MIT
# -----------------------------------------------------------------------------

from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_state_city
from PIL import Image, ImageDraw, ImageFont
import logging
from datetime import datetime

# Define the gate names
gate_names = ['H', 'X', 'Y', 'Z', 'S', 'T', 'RX', 'RY', 'RZ']

# Define the gate inclusion flags
gate_inclusions = [True, True, True, True, True, True, True, True, True]

# Create a Quantum Circuit acting on a quantum register of one qubit
circuit = QuantumCircuit(1, 1)

# Add gates to the circuit based on the inclusion flags
for gate_name, include_gate in zip(gate_names, gate_inclusions):
    if include_gate:
        if gate_name == 'H':
            circuit.h(0)  # Hadamard gate
        elif gate_name == 'X':
            circuit.x(0)  # Pauli-X gate
        elif gate_name == 'Y':
            circuit.y(0)  # Pauli-Y gate
        elif gate_name == 'Z':
            circuit.z(0)  # Pauli-Z gate
        elif gate_name == 'S':
            circuit.s(0)  # S gate
        elif gate_name == 'T':
            circuit.t(0)  # T gate
        elif gate_name == 'RX':
            circuit.rx(0.5, 0)  # Rotation around X-axis
        elif gate_name == 'RY':
            circuit.ry(0.5, 0)  # Rotation around Y-axis
        elif gate_name == 'RZ':
            circuit.rz(0.5, 0)  # Rotation around Z-axis

# Add a Measure gate to see the state.
circuit.measure([0], [0])

# Use Aer's statevector_simulator for circuit execution
simulator = Aer.get_backend('statevector_simulator')

# Execute the circuit on the statevector simulator
shots = 1000
logging.info("Execution Parameters:")
logging.info(f"Number of shots: {shots}")
logging.info(f"Quantum simulator: {simulator}")

start_time = datetime.now()
job = execute(circuit, simulator, shots=shots)
end_time = datetime.now()

execution_time = end_time - start_time
logging.info(f"Execution time: {execution_time}")

# Grab the results from the job
result = job.result()

# Get the counts (how many times we got 0 and how many times we got 1)
counts = result.get_counts(circuit)

# Create the filename base (without extension)
filename_base = f"{counts['0']}_{counts['1']}"

# Set up logging to a file
logging.basicConfig(filename=f"{filename_base}.log", level=logging.INFO)
logging.info(f"Total count for 0 and 1 are: {counts}")

# Draw the circuit and save it as an image
image_filename = f"{filename_base}.png"
figure = circuit.draw(output='mpl', filename=image_filename)
logging.info(f"Circuit diagram saved as {image_filename}")

# Retrieve the statevector
state = result.get_statevector(circuit)
if state is not None:
    # Plot the Bloch vector
    bloch_filename = f"{filename_base}_bloch.png"
    plot_bloch_multivector(state).savefig(bloch_filename)
    logging.info(f"Bloch vector plot saved as {bloch_filename}")

    # Plot the state city
    state_city_filename = f"{filename_base}_state_city.png"
    plot_state_city(state).savefig(state_city_filename)
    logging.info(f"State city plot saved as {state_city_filename}")
else:
    logging.warning("Statevector retrieval not supported by the backend.")

# Open the annotated image and add text overlay
image = Image.open(image_filename)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 14)

text = f"Scientific Information:\n"
text += f"Qubits: {circuit.num_qubits}\n"
text += f"Total count for 0 and 1 are: {counts}\n\n"
text += f"Execution Parameters:\nNumber of shots: {shots}\nQuantum simulator: {simulator}\n\n"
text += f"Execution time: {execution_time}\n\nResults:\nTotal count for 0 and 1 are: {counts}\n"
text += f"Date and Time of Execution: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

draw.text((10, 10), text, fill='black', font=font)

# Save the annotated image
annotated_image_filename = f"{filename_base}_annotated.png"
image.save(annotated_image_filename)
logging.info(f"Annotated image saved as {annotated_image_filename}")

# Open the annotated image
image.show()

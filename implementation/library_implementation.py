import pennylane as qml
from pennylane import numpy as np
from ozqis import quantum_relative_entropy, calculate

n_qubits = 2
dev = qml.device('default.qubit', wires=n_qubits)

def circuit(params):
    for i in range(n_qubits):
        qml.RY(params[i], wires=i)
    qml.CNOT(wires=[0,1])

@qml.qnode(dev)
def get_state(params):
    circuit(params)
    return qml.state()




init_params = np.array([0.1, 0.2], requires_grad=True)
rho_0 = np.outer(get_state(init_params), get_state(init_params).conj())


epochs = 50
qre_list = []
params = init_params.copy()

for epoch in range(epochs):
    params = params + 0.1 * (np.random.random(size=n_qubits) - 0.5)  # Küçük bir değişim
    rho_t = np.outer(get_state(params), get_state(params).conj())

    qre_value = quantum_relative_entropy(rho_t, rho_0)

    qre_list.append(qre_value)

calculate(qre_list, epochs, n_qubits)

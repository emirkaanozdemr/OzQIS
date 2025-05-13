import pennylane as qml
from pennylane import numpy as np


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

def quantum_relative_entropy(rho, sigma):
    eigvals_rho, eigvecs_rho = np.linalg.eigh(rho)
    log_rho = eigvecs_rho @ np.diag(np.log2(np.clip(eigvals_rho, 1e-10, 1.0))) @ eigvecs_rho.conj().T
    eigvals_sigma, eigvecs_sigma = np.linalg.eigh(sigma)
    log_sigma = eigvecs_sigma @ np.diag(np.log2(np.clip(eigvals_sigma, 1e-10, 1.0))) @ eigvecs_sigma.conj().T
    return np.real(np.trace(rho @ (log_rho - log_sigma)))


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


d = 2 ** n_qubits
S_max = np.log2(d)

OzQIS_QRE = 1 - (np.sum(qre_list) / (epochs * S_max))
OzQIS_QRE = np.clip(QIS_QRE, 0, 1)


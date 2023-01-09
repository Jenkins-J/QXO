from flask import Flask, render_template
from qiskit import *
from matplotlib import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, world</p>"

@app.route("/qiskit")
def my_qiskit():
    qr = QuantumRegister(4)
    cr = ClassicalRegister(4)
    circuit = QuantumCircuit(qr, cr)
    #%matplotlib inline
    circuit.h(qr[0])
    circuit.h(qr[1])
    circuit.h(qr[2]) 
    circuit.h(qr[3])
    circuit.measure(qr,cr)
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(circuit, backend=simulator, shots=1).result()
    number_dict = result.get_counts(circuit)
    number = conv_bin_to_dec(number_dict)
    #print(result.get_counts(circuit))
    return render_template("index.html", number=number)

def conv_bin_to_dec(number_dict):
    for num in number_dict:
        bin_string = str(num)
    return int(bin_string, 2)
from flask import Flask
from qiskit import *
from matplotlib import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, world</p>"

@app.route("/qiskit")
def qiskit():
    qr = QuantumRegister(2)
    cr = ClassicalRegister(2)
    circuit = QuantumCircuit(qr, cr)
    #%matplotlib inline
    circuit.draw()
    return "<p>test</p>"
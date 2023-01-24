from flask import Flask, request
from qiskit import *
from matplotlib import *
import math

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, world</p>"

@app.route("/qiskit")
def my_qiskit():
    space1 = request.args.get('space1')
    space2 = request.args.get('space2')
    space3 = request.args.get('space3')
    space4 = request.args.get('space4')
    space5 = request.args.get('space5')
    space6 = request.args.get('space6')
    space7 = request.args.get('space7')
    space8 = request.args.get('space8')
    space9 = request.args.get('space9')

    print(f'space 1: {space1}')
    print(f'space 2: {space2}')
    print(f'space 3: {space3}')
    print(f'space 4: {space4}')
    print(f'space 5: {space5}')
    print(f'space 6: {space6}')
    print(f'space 7: {space7}')
    print(f'space 8: {space8}')
    print(f'space 9: {space9}')

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
    int_dict = {"number":number}
    #print(result.get_counts(circuit))
    return int_dict

def conv_bin_to_dec(number_dict):
    for num in number_dict:
        bin_string = str(num)
    num =  int(bin_string, 2)
    num = math.floor(num * (8/15))
    return num
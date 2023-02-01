from flask import Flask, request
from qiskit import *
from matplotlib import *
import math
import ttt

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
    #if 1 computer is x if 0 computer is O
    mark = request.args.get('mark')

    print(f'space 1: {space1}')
    print(f'space 2: {space2}')
    print(f'space 3: {space3}')
    print(f'space 4: {space4}')
    print(f'space 5: {space5}')
    print(f'space 6: {space6}')
    print(f'space 7: {space7}')
    print(f'space 8: {space8}')
    print(f'space 9: {space9}')
    print(f'mark: {mark}')

    m = []
    m = ttt.moves(space1,space2,space3,space4,space5,space6,space7,space8,space9,mark)
    print(m)

    # build quantum circuit if there is only one possible move 
    if len(m) == 1: 
        if m[0] == 1:
            print("Space 1 is the winning move ")
            qr = QuantumRegister(4)
            cr = ClassicalRegister(4)
            circuit = QuantumCircuit(qr, cr)
            circuit.x(qr[0])
            circuit.measure(qr,cr)
            simulator = Aer.get_backend('qasm_simulator')
            result = execute(circuit, backend=simulator, shots=1).result()
            number_dict = result.get_counts(circuit)
            for num in number_dict:
                bin_string = str(num)
            number =  int(bin_string, 2)
            print(f'NUMBER after circuit: {number}')
        elif m[0] == 2: 
            print("Space 2 is the winning move ")
            qr = QuantumRegister(4)
            cr = ClassicalRegister(4)
            circuit = QuantumCircuit(qr, cr)
            circuit.x(qr[1])
            circuit.measure(qr,cr)
            simulator = Aer.get_backend('qasm_simulator')
            result = execute(circuit, backend=simulator, shots=1).result()
            number_dict = result.get_counts(circuit)
            for num in number_dict:
                bin_string = str(num)
            number =  int(bin_string, 2)
            print(f'NUMBER after circuit: {number}')
        elif m[0] == 3:
            print("Space 3 is the winning move ")
            qr = QuantumRegister(4)
            cr = ClassicalRegister(4)
            circuit = QuantumCircuit(qr, cr)
            circuit.x(qr[0])
            circuit.x(qr[1])
            circuit.measure(qr,cr)
            simulator = Aer.get_backend('qasm_simulator')
            result = execute(circuit, backend=simulator, shots=1).result()
            number_dict = result.get_counts(circuit)
            for num in number_dict:
                bin_string = str(num)
            number =  int(bin_string, 2)
            print(f'NUMBER after circuit: {number}')
        elif m[0] == 4:
            print("Space 4 is the winning move ")
            qr = QuantumRegister(4)
            cr = ClassicalRegister(4)
            circuit = QuantumCircuit(qr, cr)
            circuit.x(qr[2])
            circuit.measure(qr,cr)
            simulator = Aer.get_backend('qasm_simulator')
            result = execute(circuit, backend=simulator, shots=1).result()
            number_dict = result.get_counts(circuit)
            for num in number_dict:
                bin_string = str(num)
            number =  int(bin_string, 2)
            print(f'NUMBER after circuit: {number}')
        elif m[0] == 5:
            print("Space 5 is the winning move ")
            qr = QuantumRegister(4)
            cr = ClassicalRegister(4)
            circuit = QuantumCircuit(qr, cr)
            circuit.x(qr[0])
            circuit.x(qr[2])
            circuit.measure(qr,cr)
            simulator = Aer.get_backend('qasm_simulator')
            result = execute(circuit, backend=simulator, shots=1).result()
            number_dict = result.get_counts(circuit)
            for num in number_dict:
                bin_string = str(num)
            number =  int(bin_string, 2)
            print(f'NUMBER after circuit: {number}')
        elif m[0] == 6:
            print("Space 6 is the winning move ")
            qr = QuantumRegister(4)
            cr = ClassicalRegister(4)
            circuit = QuantumCircuit(qr, cr)
            circuit.x(qr[1])
            circuit.x(qr[2])
            circuit.measure(qr,cr)
            simulator = Aer.get_backend('qasm_simulator')
            result = execute(circuit, backend=simulator, shots=1).result()
            number_dict = result.get_counts(circuit)
            for num in number_dict:
                bin_string = str(num)
            number =  int(bin_string, 2)
            print(f'NUMBER after circuit: {number}')
        elif m[0] == 7:
            print("Space 7 is the winning move ")
            qr = QuantumRegister(4)
            cr = ClassicalRegister(4)
            circuit = QuantumCircuit(qr, cr)
            circuit.x(qr[0])
            circuit.x(qr[1])
            circuit.x(qr[2])
            circuit.measure(qr,cr)
            simulator = Aer.get_backend('qasm_simulator')
            result = execute(circuit, backend=simulator, shots=1).result()
            number_dict = result.get_counts(circuit)
            for num in number_dict:
                bin_string = str(num)
            number =  int(bin_string, 2)
            print(f'NUMBER after circuit: {number}')
        elif m[0] == 8:
            print("Space 8 is the winning move ")
            qr = QuantumRegister(4)
            cr = ClassicalRegister(4)
            circuit = QuantumCircuit(qr, cr)
            circuit.x(qr[3])
            circuit.measure(qr,cr)
            simulator = Aer.get_backend('qasm_simulator')
            result = execute(circuit, backend=simulator, shots=1).result()
            number_dict = result.get_counts(circuit)
            for num in number_dict:
                bin_string = str(num)
            number =  int(bin_string, 2)
            print(f'NUMBER after circuit: {number}')
        else: # if m[0] is 9
            print("Space 9 is the winning move ")
            qr = QuantumRegister(4)
            cr = ClassicalRegister(4)
            circuit = QuantumCircuit(qr, cr)
            circuit.x(qr[0])
            circuit.x(qr[3])
            circuit.measure(qr,cr)
            simulator = Aer.get_backend('qasm_simulator')
            result = execute(circuit, backend=simulator, shots=1).result()
            number_dict = result.get_counts(circuit)
            for num in number_dict:
                bin_string = str(num)
            number =  int(bin_string, 2)
            print(f'NUMBER after circuit: {number}')
        int_dict = {"number":number}
    else: # if no winning move, generate a random space to play
        print('INFO: Generating Random Number to play')
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
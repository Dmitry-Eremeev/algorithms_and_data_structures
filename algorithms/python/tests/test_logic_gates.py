from ..logic_gates import AndGate, NotGate, OrGate


def show_all_gates(gates_list):
    print("GATES:\n")
    for gate in gates_list:
        print(gate)
    print("\n")


gate_1 = AndGate(name="gate_1")
gate_2 = AndGate(name="gate_2")
gate_3 = OrGate(name="gate_3")
gate_4 = NotGate(name="gate_4")
gates = [gate_1, gate_2, gate_3, gate_4]

gate_1.pass_signal_to(connected_device=gate_3, connected_device_part="input_1")
gate_2.pass_signal_to(connected_device=gate_3, connected_device_part="input_2")
gate_3.pass_signal_to(connected_device=gate_4, connected_device_part="input")
show_all_gates(gates)

gate_1.input_1 = 0
show_all_gates(gates)

gate_1.input_2 = 1
show_all_gates(gates)

gate_2.input_1 = 0
show_all_gates(gates)

gate_2.input_2 = 1
show_all_gates(gates)

result = gate_4.output

assert result == 1, f"result: {result}"



class LogicGate:
    def __init__(self, name, pass_to_device=None, pass_to_device_part=None):
        self._name = name
        self._output = None
        self._pass_to_device = pass_to_device
        self._pass_to_device_part = pass_to_device_part

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        raise NotImplemented

    def _pass_signal(self):
        if self.pass_to_device:
            setattr(self.pass_to_device, self.pass_to_device_part, self.output)

    @property
    def pass_to_device(self):
        return self._pass_to_device

    @pass_to_device.setter
    def pass_to_device(self, device):
        self._pass_to_device = device

    @property
    def pass_to_device_part(self):
        return self._pass_to_device_part

    @pass_to_device_part.setter
    def pass_to_device_part(self, line):
        self._pass_to_device_part = line

    def pass_signal_to(self, connected_device, connected_device_part):
        self.pass_to_device = connected_device
        self.pass_to_device_part = connected_device_part
        setattr(connected_device, connected_device_part, self.output)

    def _handle_input(self, **kwargs):
        assert "input_name" in kwargs, "input_name must be provided in kwargs"
        assert "input_value" in kwargs, "input_value must be provided in kwargs"
        assert kwargs["input_value"] in [1, 0, None], f"Device {self._name}: input {kwargs['input_value']} is invalid"
        setattr(self, kwargs["input_name"], kwargs["input_value"])

    def __str__(self):
        return f"Gate {self.name}, output: {self.output}, " \
               f"pass to device: {self._pass_to_device.name if self._pass_to_device else None}, " \
               f"pass to device part: {self._pass_to_device_part}"


class BinaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input_1 = None
        self._input_2 = None

    @property
    def output(self):
        return super().output

    @output.setter
    def output(self, value):
        raise NotImplemented

    @property
    def input_1(self):
        return self._input_1

    @property
    def input_2(self):
        return self._input_2

    def _handle_input(self, **kwargs):
        super()._handle_input(**kwargs)
        self.output = (self.input_1, self.input_2)

    def __str__(self):
        return f"{super().__str__()}, input 1: {self.input_1}, input 2: {self.input_2}"

    def _check_input_values(self, input_values):
        assert len(input_values) == 2, f"Gate {self._name}: input number must be equal 2"


class UnaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input = None

    @property
    def output(self):
        return super().output

    @output.setter
    def output(self, value):
        raise NotImplemented

    @property
    def input(self):
        return self._input

    def _handle_input(self, **kwargs):
        kwargs["input_name"] = "_input"
        super()._handle_input(**kwargs)
        self.output = (self.input,)

    def __str__(self):
        return f"{super().__str__()}, input: {self.input}"


class AndGate(BinaryGate):

    @property
    def input_1(self):
        return self._input_1

    @input_1.setter
    def input_1(self, input_value):
        self._handle_input(input_name="_input_1", input_value=input_value)

    @property
    def input_2(self):
        return self._input_2

    @input_2.setter
    def input_2(self, input_value):
        self._handle_input(input_name="_input_2", input_value=input_value)

    @property
    def output(self):
        return super().output

    @output.setter
    def output(self, input_values):
        self._check_input_values(input_values=input_values)
        self._output = 1 if input_values[0] == input_values[1] == 1 else 0
        self._pass_signal()


class OrGate(BinaryGate):

    @property
    def input_1(self):
        return self._input_1

    @input_1.setter
    def input_1(self, input_value):
        self._handle_input(input_name="_input_1", input_value=input_value)

    @property
    def input_2(self):
        return self._input_2

    @input_2.setter
    def input_2(self, input_value):
        self._handle_input(input_name="_input_2", input_value=input_value)

    @property
    def output(self):
        return super().output

    @output.setter
    def output(self, input_values):
        self._check_input_values(input_values=input_values)
        self._output = 1 if input_values[0] == 1 or input_values[1] == 1 else 0
        self._pass_signal()


class NotGate(UnaryGate):

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, input_value):
        self._handle_input(input_value=input_value)

    @property
    def output(self):
        return super().output

    @output.setter
    def output(self, input_values):
        assert len(input_values) == 1, f"Gate {self._name}: input number must be equal 1"
        self._output = 1 if input_values[0] == 0 else 0
        self._pass_signal()

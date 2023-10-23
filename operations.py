import helper

import arithmetic

"""
    Add input signals (any number) and display the resulting signal.
"""


def addition_operation(signals):
    signal_len = len(signals)
    comm_n = []
    comm_val = []
    for idx in range(signal_len):
        if idx == 0:
            comm_n = signals[0][0]
            comm_val = signals[0][1]
        else:
            comm_val = arithmetic.add((comm_n, comm_val), signals[idx])
    return comm_n, comm_val


"""
    Subtract input signals and display the resulting signal
"""


def subtraction_operation(signals):
    signal_len = len(signals)
    comm_n = []
    comm_val = []
    for idx in range(signal_len):
        if idx == 0:
            comm_n = signals[0][0]
            comm_val = signals[0][1]
        else:
            comm_val = arithmetic.subtract((comm_n, comm_val), signals[idx])
    return comm_n, comm_val


"""
    Multiply a signal by a constant value to amplify or reduce the signal amplitude. 
    (If constant equals -1, then signal will be inverted)
"""


def multiplication_operation(signal, factor):
    signal_n = signal[0]
    signal_val = arithmetic.multiply(signal, factor)
    return signal_n, signal_val


"""
    Squaring a signal and displaying the resulting signal.
"""


def squaring_operation(signal):
    signal_n = signal[0]
    signal_val = arithmetic.square(signal)
    return signal_n, signal_val


"""
    Add to the signal a (+ve) or (-ve) constant.
"""


def shifting_operation(signal, factor):
    signal_n = arithmetic.shift(signal, factor)
    signal_val = signal[1]
    return signal_n, signal_val


"""
    Normalize the signal from -1 to 1 or 0 to 1 depending on user choice.
"""


def normalization_operation(signal, min, max):
    signal_n = signal[0]
    signal_val = arithmetic.normalize(signal, min, max)
    return signal_n, signal_val


"""
    Accumulation of input signal
"""


def accumulation_operation(signal):
    signal_n = signal[0]
    signal_val = arithmetic.accumulation(signal)
    return signal_n, signal_val

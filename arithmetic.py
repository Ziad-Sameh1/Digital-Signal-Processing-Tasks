import helper


def add(signal1, signal2):
    helper.validate_signals(signal1, signal2)
    f_signal = []
    length = len(signal1[1])
    for i in range(length):
        f_signal.append(signal1[1][i] + signal2[1][i])
    return f_signal


def subtract(signal1, signal2):
    helper.validate_signals(signal1, signal2)
    f_signal = []
    length = len(signal1[1])
    for i in range(length):
        f_signal.append(signal1[1][i] - signal2[1][i])
    return f_signal


def multiply(signal1, factor):
    f_signal = []
    for entry in signal1[1]:
        f_signal.append(entry * factor)
    return f_signal


def square(signal1):
    f_signal = []
    for entry in signal1[1]:
        f_signal.append(entry * entry)
    return f_signal


def normalize(signal1, min_list, max_list):
    f_signal = []
    for entry in signal1[1]:
        f_signal.append(
            ((entry - min(signal1[1])) / (max(signal1[1]) - min(signal1[1]))) * (max_list - min_list) + min_list)
    return f_signal


def shift(signal1, factor):
    f_signal = []
    for entry in signal1[0]:
        f_signal.append(entry - factor)
    return f_signal


def accumulation(signal1):
    f_signal = []
    comm = 0
    for entry in signal1[0]:
        comm += entry
        f_signal.append(comm)
    return f_signal

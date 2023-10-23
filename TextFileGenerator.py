import numpy as np
import matplotlib.pyplot as plt

file_path = '/home/ziad/PycharmProjects/taskOneDSP/signal1.txt'


def read_signal(file_path):
    with open(file_path, 'r') as file:
        xPoints = []
        yPoints = []
        idx = 0
        for line in file:
            idx = idx + 1
            if idx <= 3: continue # skip the first three params
            values = line.strip().split(' ')
            xPoints.append(float(values[0]))
            yPoints.append(float(values[1]))
    return (xPoints, yPoints)

def plot_discrete(signal):
    plt.stem(signal[0], signal[1])

def plot_continuous(signal):
    plt.plot(signal[0], signal[1], color="purple")


def plot_both_signals(signal):
    plot_continuous(signal)
    plot_discrete(signal)
    plt.xlabel('N')
    plt.ylabel('Amplitude')
    plt.show()


def plot_cont_disc():
    signal = read_signal(file_path)
    plot_both_signals(signal)

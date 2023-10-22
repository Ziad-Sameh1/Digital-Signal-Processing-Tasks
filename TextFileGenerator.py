import numpy as np
import matplotlib.pyplot as plt


file_path='C:/Users/DELL/PycharmProjects\DSP_TASK1/signal1.txt'

def read_signal(file_path):
    with open(file_path, 'r') as file:
        samples = []
        for line in file:
            values = line.strip().split(' ')
            samples.extend([float(value) for value in values])
    return samples

def plot_continuous(signal):
    plt.plot(signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Continuous Representation')
    plt.show()

def plot_discrete(signal):
    n = len(signal)
    plt.stem(range(n), signal, use_line_collection=True)
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.title('Discrete Representation')
    plt.show()

def plot_cont_disc():
    signal = read_signal(file_path)
    plot_continuous(signal)
    plot_discrete(signal)

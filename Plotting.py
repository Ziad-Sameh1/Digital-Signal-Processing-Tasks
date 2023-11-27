import math

import matplotlib.pyplot as plt

import TextFileGenerator as txt

import numpy as np


def plot_sinusoidal(amp, phase, analog, sampling):
    plot_sinusoidal_continuous(amp, phase, analog, sampling)


def plot_cosinusoidal(amp, phase, analog, sampling):
    plot_cosinusoidal_continuous(amp, phase, analog, sampling)


def plot_sinusoidal_continuous(amp, phase, analog, sampling):
    if sampling == "" or float(sampling) == 0:
        xPoints = np.linspace(0, 1, 100, endpoint=False)
    else:
        xPoints = np.linspace(0, 1, int(sampling), endpoint=False)
    yPoints = float(amp) * np.sin(2 * np.pi * float(analog) * xPoints + float(phase))
    SignalSamplesAreEqual("SinOutput.txt", [], samples=yPoints)
    # print(yPoints)
    plt.plot(xPoints, yPoints)
    plt.show()


def plot_cosinusoidal_continuous(amp, phase, analog, sampling):
    if sampling == "" or float(sampling) == 0:
        xPoints = np.linspace(0, 1, 100, endpoint=False)
    else:
        xPoints = np.linspace(0, 1, int(sampling), endpoint=False)
    yPoints = float(amp) * np.cos(2 * np.pi * float(analog) * xPoints + float(phase))
    SignalSamplesAreEqual("CosOutput.txt", [], samples=yPoints)
    # print(yPoints)
    plt.plot(xPoints, yPoints)
    plt.show()


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


def dsp_plot_continuous(signal):
    plt.plot(signal[0], signal[1], color="purple")
    plt.xlabel('N')
    plt.ylabel('Amplitude')
    plt.show()


def dsp_plot_discrete(signal, xLabel='N', yLabel='Amplitude'):
    plt.stem(signal[0], signal[1])
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

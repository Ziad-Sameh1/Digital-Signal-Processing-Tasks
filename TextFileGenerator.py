import numpy as np
import matplotlib.pyplot as plt
import re
from os.path import isfile, join

from os import listdir

file_path = '/home/ziad/PycharmProjects/taskOneDSP/signal1.txt'

def read_signal(file_path):
    with open(file_path, 'r') as file:
        xPoints = []
        yPoints = []
        idx = 0
        for line in file:
            idx = idx + 1
            if idx <= 3: continue  # skip the first three params
            values = line.strip().split(' ')
            xPoints.append(float(values[0]))
            yPoints.append(float(values[1]))
    return xPoints, yPoints


def read_signals(folder_path):
    signals = []
    files = listdir(folder_path)
    print(files)
    for file in files:
        if not isfile(join(folder_path, file)):
            continue
        l_file = file.lower()
        match = re.findall("^signal\d+", l_file)
        if len(match) != 0:
            signals.append(read_signal(join(folder_path, file)))

    return signals


def read_polar(file_path):
    with open(file_path, 'r') as file:
        xPoints = []
        yPoints = []
        idx = 0
        for line in file:
            idx = idx + 1
            if idx <= 3: continue  # skip the first three params
            values = line.strip().split(',')
            xPoints.append(float(values[0].replace('f', '')))
            yPoints.append(float(values[1].replace('f', '')))
    return xPoints, yPoints


def save_polar_signal(x1, x2, signal):
    w_file = open("generated_polar.txt", 'w')
    lines = []
    line1 = str(x1) + '\n'
    line2 = str(x2) + '\n'
    line3 = str(len(signal[0])) + '\n'
    lines.append(line1)
    lines.append(line2)
    lines.append(line3)
    for idx in range(len(signal[0])):
        x = signal[0][idx]
        y = signal[1][idx]
        if x - int(x) != 0:
            x = str(x)
            x += 'f'
        else:
            x = int(x)
        if y - int(y) != 0:
            y = str(y)
            y += 'f'
        else:
            y = int(y)
        line = str(x) + ' ' + str(y) + '\n'
        lines.append(line)

    print(lines)
    w_file.writelines(lines)
    w_file.close()

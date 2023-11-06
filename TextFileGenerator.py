import numpy as np
import matplotlib.pyplot as plt
import re
from os.path import isfile, join

from os import listdir

# file_path = '/home/ziad/PycharmProjects/taskOneDSP/signal1.txt'


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
    for file in files:
        if not isfile(join(folder_path, file)):
            continue
        l_file = file.lower()
        match = re.findall("^signal\d+", l_file)
        if len(match) != 0:
            signals.append(read_signal(join(folder_path, file)))
    return signals

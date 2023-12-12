import TextFileGenerator as tfg
import Shift_Fold_Signal
import comparesignal2
import FrequencyDomain
import ConvTest
import DerivativeSignal


def smoothing(f, num_pnts):
    y = []
    amps = f[1]
    for i in range(len(amps) - (num_pnts - 1)):
        sum = 0
        for j in range(i, i + num_pnts):
            sum += amps[j]
        y.append(float(sum / num_pnts))

    print(y)
    # comparesignal2.SignalSamplesAreEqual(
    #     '/home/ziad/DSP/Digital-Signal-Processing-Tasks/input/OutMovAvgTest1.txt', y)
    return f[0], y


# def sharpening(f):
#     first_der = []
#     sec_der = []
#     ##calculate first derivative##
#     for i in range(f[1]):
#         if (i == 0):
#             first_der.append(f[1][i])
#         else:
#             first_derivative = f[1][i] - f[1][i - 1]
#             first_der.append(first_derivative)
#             ##calculate second derivative##
#             for j in range(f[1]):
#                 if (j == 0):
#                     second_derivative = f[1][j + 1] + 2 * (f[1][j])
#                     sec_der.append(second_derivative)
#                 else:
#                     second_derivative = f[1][j + 1] + 2 * (f[1][j]) + f[1][j - 1]
#                     sec_der.append(second_derivative)
#
#     return first_der, sec_der


def sharpening_first_derv(signal):
    y = []
    for i in range(len(signal) - 1):
        y.append(signal[i + 1] - signal[i])
    return y


def sharpening(signal):
    s = signal[1]
    first_derv = sharpening_first_derv(s)
    second_derv = sharpening_first_derv(first_derv)
    DerivativeSignal.DerivativeSignal(first_derv, second_derv)
    return signal[0], second_derv


def shift_signal(f, k):
    y = []
    time = f[0]
    for x in time:
        y.append(x + k)
    return y, f[1]


def fold_signal(f):
    amps = f[1]
    amps = amps[::-1]
    comparesignal2.SignalSamplesAreEqual(
        '/home/ziad/DSP/Digital-Signal-Processing-Tasks/shifting-folding/Output_fold.txt', amps)
    return f[0], amps


def shift_folded(signal, k):
    folded_signal = fold_signal(signal)
    shifted = shift_signal(folded_signal, k)
    print(shifted[0])
    print(shifted[1])
    Shift_Fold_Signal.Shift_Fold_Signal(
        '/home/ziad/DSP/Digital-Signal-Processing-Tasks/shifting-folding/Output_ShiftFoldedby-500.txt', shifted[0],
        shifted[1])
    return shifted


def rmv_dc(signal):
    y = []

    freq_domain = FrequencyDomain.v2_dft(signal[1])

    freq_domain[0] = 0

    removed_dc = FrequencyDomain.v2_inverse_dft(freq_domain)

    for s in removed_dc:
        y.append(s.real)

    print(y)

    comparesignal2.SignalSamplesAreEqual(
        '/home/ziad/DSP/Digital-Signal-Processing-Tasks/output/DC_component_output.txt', y)

    return signal[0], y

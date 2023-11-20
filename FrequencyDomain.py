import cmath
import math
import numpy as np
import signalcompare
import TextFileGenerator as parser


def dft(signal, freq, amp):
    input = signal[0]
    amps = signal[1]
    freqs = _get_frequencies(input, freq)
    freq_domain = get_freq_domain(amps)
    amplitudes = _get_amp(input, freq_domain)
    phase = _get_phase(input, freq_domain)
    # _check(amps, amplitudes, )
    if amp == 0:
        return freqs, phase
    elif amp == 1:
        return freqs, amplitudes


def idft(signal, idx=-1, new_amplitude=-1, new_phase=-1):
    real = []
    imag = []
    if idx != -1:
        signal[0][idx] = new_amplitude
        signal[1][idx] = new_phase
    amp = signal[0]
    phase = signal[1]
    for i in range(len(amp)):
        real.append(amp[i] * np.cos(phase[i]))
        imag.append(amp[i] * np.sin(phase[i]))

    res = np.zeros(len(real))
    for n in range(len(real)):
        for k in range(len(real)):
            angle = 2 * np.pi * k * n / len(real)
            res[n] += real[k] * np.cos(angle) - imag[k] * np.sin(angle)

    return res / len(real)


def get_freq_domain(input):
    res = []
    for k in range(len(input)):
        x_k = 0
        for n in range(len(input)):
            x_k += input[n] * cmath.exp(-1j * (2 * np.pi * k * n / len(input)))
        res.append(x_k)
    return res


def _get_frequencies(input, fs):
    print(input)
    res = []
    fund_f = (2 * 22 / 7) / (len(input) * 1 / fs)
    res.append(round(fund_f, 4))
    f = fund_f
    for x in range(len(input) - 1):
        f = f + fund_f
        res.append(round(f, 4))
    return res


def _get_amp(input, freq_domain):
    return [np.round(np.sqrt((np.real(abs(freq_domain[k])) ** 2) + (np.imag(abs(freq_domain[k])) ** 2)), 14) for k in
            range(len(input))]


def _get_phase(input, freq_domain):
    return [np.round(np.arctan2(np.imag(freq_domain[k]), np.real(freq_domain[k])), 14) for k in
            range(len(input))]


# def _check(input_amp, output_amp, input_phase, output_phase):
#     if signalcompare.SignalComapreAmplitude(input_amp, output_amp) and signalcompare.SignalComaprePhaseShift(input_phase, output_phase):
#         print('Success')
#     else:
#         print('Error')
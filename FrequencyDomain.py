import cmath
import math
import numpy as np
import signalcompare
import TextFileGenerator as parser
import comparesignal2


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


def v2_dft(signal):
    N = len(signal)
    dft_result = []
    for k in range(N):
        X_k = sum(signal[n] * cmath.exp(-2j * cmath.pi * k * n / N) for n in range(N))
        dft_result.append(X_k)
    return dft_result

def v2_inverse_dft(dft_result):
    N = len(dft_result)
    signal = []
    for n in range(N):
        x_n = sum(X_k * cmath.exp(2j * cmath.pi * k * n / N) for k, X_k in enumerate(dft_result))
        signal.append(x_n / N)
    return signal




def calc_dct_coeff(k, signal):
    y_k = 0
    x_n = signal[1]
    N = len(signal[1])
    for n in range(N):
        y_k += x_n[n] * math.cos(np.pi * (2 * n - 1) * (2 * k - 1) / (4 * N))
    if k == 0:
        return y_k * math.sqrt(1.0 / N) * math.sqrt(2)
    else:
        return y_k * math.sqrt(2.0 / N)


def save_ms(res, m):
    with open('saved_coeffs.txt', 'w') as file:
        file.write('0\n')
        file.write('1\n')
        t = str(m) + '\n'
        file.write(t)
        for i in range(m):
            file.write('0 ' + str(res[i]) + '\n')


def dct(signal, m):
    N = len(signal[1])
    dct_result = [calc_dct_coeff(k, signal) for k in range(N)]
    if m:
        m = int(m)
        if 0 < m <= len(dct_result):
            save_ms(dct_result, m)
        else:
            save_ms(dct_result, len(dct_result))
    else:
        save_ms(dct_result, len(dct_result))
    x = [0] * len(dct_result)
    comparesignal2.SignalSamplesAreEqual('/home/ziad/DSP/Digital-Signal-Processing-Tasks/output/DCT_output.txt', dct_result)
    return x, dct_result


def calc_sub(amp, avg):
    return amp - avg


def rmv_dct(signal):
    N = len(signal[1])
    x_n = signal[1]
    avg = np.mean(x_n)
    rmv_dct_result = [calc_sub(x_n[k], avg) for k in range(N)]
    comparesignal2.SignalSamplesAreEqual('/home/ziad/DSP/Digital-Signal-Processing-Tasks/output/DC_component_output.txt',
                                         rmv_dct_result)
    return signal[0], rmv_dct_result


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

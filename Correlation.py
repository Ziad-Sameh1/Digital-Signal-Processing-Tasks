import comparesignal2


def  __calc_num_value(signal1, numerator):
    size = len(signal1)
    summation_res = 0
    for n in range(size):
        summation_res += signal1[n] * numerator[n]
    return 1 / size * summation_res


def __get_numerators(signal1, signal2):
    size = len(signal1)
    res = [signal2]
    sig = signal2
    for _ in range(size):
        new_num = __rotate(sig, 1)
        sig = new_num
        res.append(new_num)
    return res


def __rotate(l, n):
    return l[n:] + l[:n]


def __calc_denominator(signal1, signal2):
    size = len(signal1)
    sum1 = sum2 = 0
    for n in range(size):
        sum1 += signal1[n] ** 2
        sum2 += signal2[n] ** 2
    print("sum1: ", sum1)
    print("sum2: ", sum2)
    return 1 / size * (sum1 * sum2) ** 0.5


def cross_correlation(sig1, sig2):
    res = []
    print(sig1)
    print(sig2)

    sig1_amp = sig1[1]
    sig2_amp = sig2[1]

    size = len(sig1_amp)

    n_numerator = __get_numerators(sig1_amp, sig2_amp)
    denominator = __calc_denominator(sig1_amp, sig2_amp)

    print(n_numerator)
    print(denominator)

    for i in range(size):
        result_n = __calc_num_value(sig1_amp, n_numerator[i]) / denominator
        res.append(result_n)

    comparesignal2.SignalSamplesAreEqual('/home/ziad/DSP/Digital-Signal-Processing-Tasks/Correlation/CorrOutput.txt',
                                         res)

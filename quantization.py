import math
def quantize_signal_levels(signal, levels_num):
    # y's
    amp = signal[1]

    # calculate min
    min_amp = min(amp)

    # calculate max
    max_amp = max(amp)

    # calculate resolution
    resolution = (max_amp - min_amp) / levels_num

    # quantized signal
    start = min_amp

    mid_points = []

    intervals = []

    curr_level = 0

    while curr_level < levels_num:
        start_range = start
        end_range = round(start + resolution, 4)
        start = end_range
        curr_level = curr_level + 1
        mid_range = round((end_range + start_range) / 2, 4)
        mid_points.append(mid_range)
        intervals.append((start_range, end_range))

    quantized_signal = []

    interval_index = []

    encoded_signal = []

    quantized_error = []
    for sample in amp:
        for idx, interval in enumerate(intervals):
            if interval[0] <= sample <= interval[1]:
                quantized_signal.append(mid_points[idx])
                interval_index.append(idx + 1)
                quantized_error.append(round(mid_points[idx] - sample, 4))
                encoded_signal.append(decimal_to_binary(idx, int(math.log2(levels_num))))
                break

    for i in range(len(encoded_signal)):
        print(str(interval_index[i]) + ' ' + str(encoded_signal[i]) + ' ' + ' ' + str(quantized_signal[i]) + ' ' + str(
            quantized_error[i]))

    QuanTest2.QuantizationTest2('/home/ziad/DSP/Digital-Signal-Processing-Tasks/output/Quan2_Out.txt', interval_index, encoded_signal, quantized_signal, quantized_error)

    return signal[0], quantized_signal


def quantize_signal_bits(signal, bits_num):
    levels_num = pow(2, bits_num)

    # y's
    amp = signal[1]

    # calculate min
    min_amp = min(amp)

    # calculate max
    max_amp = max(amp)

    # calculate resolution
    resolution = (max_amp - min_amp) / levels_num

    # quantized signal
    start = min_amp

    mid_points = []

    intervals = []

    curr_level = 0
## calculate intervals and midpoints
    while curr_level < levels_num:
        start_range = start
        end_range = round(start + resolution, 4)
        start = end_range
        curr_level = curr_level + 1
        mid_range = round((end_range + start_range) / 2, 4)
        mid_points.append(mid_range)
        intervals.append((start_range, end_range))

    print(intervals)

    quantized_signal = []
##signal encoding
    encoded_signal = []
    for sample in amp:
        for idx, interval in enumerate(intervals):
            if interval[0] <= sample <= interval[1]:
                quantized_signal.append(mid_points[idx])
                encoded_signal.append(decimal_to_binary(idx, int(math.log2(levels_num))))
                break

    for i in range(len(encoded_signal)):
        print(encoded_signal[i] + ' ' + str(quantized_signal[i]))
    QuanTest1.QuantizationTest1('/home/ziad/DSP/Digital-Signal-Processing-Tasks/output/Quan1_Out.txt', encoded_signal, quantized_signal)
    return signal[0], quantized_signal


def decimal_to_binary(n, num_bits):
    if n < 0:
        raise ValueError("Input number must be non-negative.")
    if num_bits <= 0:
        raise ValueError("Number of bits must be a positive integer.")

    binary_num = bin(n)[2:]  # Convert decimal to binary (excluding '0b' prefix)
    binary_len = len(binary_num)

    if binary_len > num_bits:
        raise ValueError("Input number cannot be represented with the given number of bits.")

    padding = '0' * (num_bits - binary_len)  # Add leading zeros if necessary
    binary_result = padding + binary_num
    return binary_result
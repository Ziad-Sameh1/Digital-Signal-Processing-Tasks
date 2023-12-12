import ConvTest


def __get_start_index(sig1_x, sig2_x):
    min1 = min(sig1_x)
    min2 = min(sig2_x)

    return min1 + min2


def __get_end_index(sig1_x, sig2_x):
    max1 = max(sig1_x)
    max2 = max(sig2_x)

    return max1 + max2


def __calc_conv(sig1_map, sig2_map, start_index, end_index, max_sig1, max_sig2):
    conv_res = []
    for n in range(start_index, end_index + 1):
        y_n = 0
        for k in range(start_index, end_index + 1):
            if k < start_index or (n - k) < start_index:
                break
            if k > max_sig1 or (n - k) > max_sig2:
                continue
            y_n += sig1_map[k] * sig2_map[n - k]
        conv_res.append(y_n)
    return conv_res


def two_signal_convolution(sig1, sig2):
    """
       Function two_signal_convolution calculates convolution for
       two signals

       params:
        - sig1: required parameter represents the first signal
        - sig2: required parameter represents the second signal
    """

    print('Signal 1', sig1)
    print('Signal 2', sig2)

    sig1_x = sig1[0]
    sig1_y = sig1[1]

    sig2_x = sig2[0]
    sig2_y = sig2[1]

    # Convert float indices into int
    sig1_x = [int(x) for x in sig1_x]
    sig2_x = [int(x) for x in sig2_x]

    start_index = __get_start_index(sig1_x, sig2_x)
    end_index = __get_end_index(sig1_x, sig2_x)

    max_sig1 = max(sig1_x)
    max_sig2 = max(sig2_x)

    print('Start Idx:', start_index)
    print('End Idx: ', end_index)

    sig1_map = {}
    sig2_map = {}

    idx1 = 0
    idx2 = 0

    for i in range(start_index, end_index + 1):
        if sig1_x[0] <= i <= sig1_x[-1]:
            sig1_map[i] = sig1_y[idx1]
            idx1 += 1
        else:
            sig1_map[i] = 0

        if sig2_x[0] <= i <= sig2_x[-1]:
            sig2_map[i] = sig2_y[idx2]
            idx2 += 1
        else:
            sig2_map[i] = 0

    print('Signal 1 Map: ', sig1_map)
    print('Signal 2 Map:', sig2_map)

    # sig1_y = list(sig1_map.values())
    #
    # sig2_x = list(sig2_map.keys())
    # sig2_y = list(sig2_map.values())
    #
    # print('sig1_x: ', sig1_x)
    # print('sig1_y: ', sig1_y)
    #
    # print('sig2_x: ', sig2_x)
    # print('sig2_y: ', sig2_y)

    indices = list(sig1_map.keys())

    conv_res = __calc_conv(sig1_map, sig2_map, start_index, end_index, max_sig1, max_sig2)

    ConvTest.ConvTest(indices, conv_res)

    print(conv_res)

    return indices, conv_res

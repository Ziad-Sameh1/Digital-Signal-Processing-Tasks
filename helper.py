def validate_signals(signal1, signal2):
    if len(signal1[0]) != len(signal2[0]):
        raise Exception("Exception: Signals don't have the same discrete values (n)")
    for i in range(len(signal1[0])):
        if signal1[0][i] != signal2[0][i]:
            raise Exception("Exception: Signals don't have the same discrete values (n)")
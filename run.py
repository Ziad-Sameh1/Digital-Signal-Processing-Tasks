import TextFileGenerator as txt
import operations as ops


signal = txt.read_signals("/home/ziad/DSP/Digital-Signal-Processing-Tasks/input/")

# print(signals[0][1])
# print(signals[1][1])
# print(signals[2][1])

x = ops.accumulation_operation(signal[0])

print(x[1])
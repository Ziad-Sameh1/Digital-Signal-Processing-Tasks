import TextFileGenerator as tfg

filepath ='Signal1.txt'
f = tfg.read_signal(filepath)
def smoothing(f,num_pnts):
    y=[]

    for i in range(len(f[1])):
        if i < num_pnts:
            sum = 0
            for j in range(i+1):
                sum += f[1][j]
                y.append(sum/float(i+1))
            else:
                sum = 0
                for j in range(i - num_pnts + 1, i + 1):
                    sum += f[1][j]
                    y.append(sum/num_pnts)
    return y

def sharpening(f):
    first_der = []
    sec_der = []
    ##calculate first derivative##
    for i in range(f[1]):
        if (i==0):
            first_der.append(f[1][i])
        else:
            first_derivative = f[1][i] - f[1][i - 1]
            first_der.append(first_derivative)
     ##calculate second derivative##
            for j in range(f[1]):
               if(j==0):
                   second_derivative = f[1][j + 1] + 2 * (f[1][j])
                   sec_der.append(second_derivative)
               else:
                   second_derivative = f[1][j + 1] + 2 * (f[1][j]) + f[1][j - 1]
                   sec_der.append(second_derivative)

    return first_der , sec_der


def shift_signal(f,k):
    if k >= 0:
        delayed_signal = [0] * k + f[:-k]
        return delayed_signal
    else:
        advanced_signal = f[-k:] + [0] * abs(k)
        return advanced_signal

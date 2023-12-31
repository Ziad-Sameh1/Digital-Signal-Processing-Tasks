import tkinter as tk

import FrequencyDomain
import Plotting as txt
import TextFileGenerator as parser
import Plotting as form
from tkinter import ttk
import operations as op
import quantization as quant
from tkinter.filedialog import askopenfilename


def sinusoidal():
    form.plot_sinusoidal(Amplitude_value_input.get(), theta_value_input.get(), Afreq_value_input.get(),
                         sfreq_value_input.get())


def cosinusoidal():
    form.plot_cosinusoidal(Amplitude_value_input.get(), theta_value_input.get(), Afreq_value_input.get(),
                           sfreq_value_input.get())


# create color
background_colour = '#000000'
f1 = '#FFEBCD'
f2 = '#ffffff'

# window
window = tk.Tk()
window.title("")
window.geometry('500x600')
window.configure(bg=background_colour)

# frames
frame_body = tk.Frame(window, width=700, height=590, bg=f2)
frame_body.grid(row=1, column=0)

title_region = tk.Label(frame_body, text="Choose Task", height=1, font=('Ivy 18 bold'), bg=f2)
title_region.place(x=155, y=10)


def task1_form():
    # frames
    frame1_body = tk.Frame(window, width=700, height=590, bg=f2)
    frame1_body.grid(row=1, column=0)

    # frame body
    title_region = tk.Label(frame1_body, text="Signal Generator", height=1, font=('Ivy 18 bold'), bg=f2)
    title_region.place(x=145, y=10)
    ## Amplitude
    Amplitude_value = tk.Label(frame1_body, text="Amplitude", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    Amplitude_value.place(x=10, y=110)
    Amplitude_value_input = tk.Entry(frame1_body, width=30)
    Amplitude_value_input.pack()
    Amplitude_value_input.place(x=250, y=115)

    ## Phase shift(theta)
    theta_value = tk.Label(frame1_body, text="Phase Shift", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    theta_value.place(x=10, y=150)
    theta_value_input = tk.Entry(frame1_body, width=30)
    theta_value_input.pack()
    theta_value_input.place(x=250, y=155)

    ##Analog frequency
    Afreq_value = tk.Label(frame1_body, text="Analog Frequency", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    Afreq_value.place(x=10, y=190)
    Afreq_value_input = tk.Entry(frame1_body, width=30)
    Afreq_value_input.pack()
    Afreq_value_input.place(x=250, y=195)

    ##sampling frequency
    sfreq_value = tk.Label(frame1_body, text="Sampling Frequency", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    sfreq_value.place(x=10, y=230)
    sfreq_value_input = tk.Entry(frame1_body, width=30)
    sfreq_value_input.pack()
    sfreq_value_input.place(x=250, y=235)

    ##text file signal button
    submit_button = tk.Button(frame1_body, text="Generate Text file Signal", bd=2, font="arial 10", fg="black",
                              bg="silver",
                              height=1, command=txt.plot_cont_disc)
    submit_button.place(x=170, y=360)

    ##sine signal generator button
    sine_button = tk.Button(frame1_body, text="Sine Signal", bd=2, font="arial 10", fg="black", bg="silver", height=1,
                            command=sinusoidal)
    sine_button.place(x=150, y=300)

    ##cosine signal generator button
    cosine_button = tk.Button(frame1_body, text="Cosine Signal", bd=2, font="arial 10", fg="black", bg="silver",
                              height=1, command=cosinusoidal)
    cosine_button.place(x=250, y=300)


def task2_form():
    def on_shift_button():
        signal = parser.read_signal("/home/ziad/DSP/Digital-Signal-Processing-Tasks/input/inputShifting.txt")
        s = op.shifting_operation(signal, int(shift_value_input.get()))
        form.dsp_plot_continuous(s)

    def on_norm_button():
        signal = parser.read_signal("/home/ziad/DSP/Digital-Signal-Processing-Tasks/input/Signal1.txt")

        if n.get() == '0 to 1':
            s = op.normalization_operation(signal, 0, 1)
        else:
            s = op.normalization_operation(signal, -1, 1)
        form.dsp_plot_continuous(s)

    def on_mult_button():
        signal = parser.read_signal("/home/ziad/DSP/Digital-Signal-Processing-Tasks/input/Signal1.txt")
        s = op.multiplication_operation(signal, int(mult_value_input.get()))
        form.dsp_plot_continuous(s)

    # frames
    frame2_body = tk.Frame(window, width=800, height=590, bg=f2)
    frame2_body.grid(row=1, column=0)

    # frame body
    title_region = tk.Label(frame2_body, text="Arithmetic Operations", height=1, font=('Ivy 18 bold'), bg=f2)
    title_region.place(x=110, y=10)
    Add_button = tk.Button(frame2_body, text="   Addition   ", bd=2, font="arial 10", fg="black", bg="green", height=1,
                           command=on_add_button)
    Add_button.place(x=125, y=80)
    sub_button = tk.Button(frame2_body, text="Subtraction", bd=2, font="arial 10", fg="black", bg="silver", height=1,
                           command=on_sub_button)
    sub_button.place(x=240, y=80)
    acc_button = tk.Button(frame2_body, text="Accumulation", bd=2, font="arial 10", fg="black", bg="yellow", height=1,
                           command=on_acc_button)
    acc_button.place(x=125, y=135)
    sq_button = tk.Button(frame2_body, text="  Squaring  ", bd=2, font="arial 10", fg="black", bg="pink", height=1,
                          command=on_square_button)
    sq_button.place(x=240, y=135)
    ##shift##
    shift_value = tk.Label(frame2_body, text="Shift Value", height=1, font=('Ivy 15 bold'), fg="black", bg=f2)
    shift_value.place(x=10, y=250)
    shift_value_input = tk.Entry(frame2_body, width=30)
    shift_value_input.pack()
    shift_value_input.place(x=155, y=255)
    shift_button = tk.Button(frame2_body, text="shift", bd=2, font="arial 10", fg="black", bg="white",
                             height=1, command=on_shift_button)

    shift_button.place(x=440, y=250)
    ##Normalize##
    norm_value = tk.Label(frame2_body, text="Normalization", height=1, font=('Ivy 15 bold'), fg="black", bg=f2)
    norm_value.place(x=5, y=290)
    # Combobox creation
    n = tk.StringVar()
    normalization_value = ttk.Combobox(frame2_body, width=27, textvariable=n)

    # Adding combobox drop down list
    normalization_value['values'] = ('0 to 1', '-1 to 1'
                                     )
    normalization_value.place(x=175, y=295)
    normalization_value.current()
    norm_button = tk.Button(frame2_body, text="Normalize", bd=2, font="arial 10", fg="black", bg="white",
                            height=1, command=on_norm_button)
    norm_button.place(x=440, y=290)

    ##mult##
    mult_value = tk.Label(frame2_body, text="Multiplication", height=1, font=('Ivy 15 bold'), fg="black", bg=f2)
    mult_value.place(x=10, y=340)
    mult_value_input = tk.Entry(frame2_body, width=30)
    mult_value_input.pack()
    mult_value_input.place(x=185, y=345)
    mult_button = tk.Button(frame2_body, text="mult", bd=2, font="arial 10", fg="black", bg="white",
                            height=1, command=on_mult_button)
    mult_button.place(x=440, y=340)

def task3_form():

    def on_plot_button_click():
        if n.get() == 'Number of Bits':
            signal = parser.read_signal("/home/ziad/DSP/Digital-Signal-Processing-Tasks/input/Quan1_input.txt")
            s = quant.quantize_signal_bits(signal, int(num_value_input.get()))
        else:
            signal = parser.read_signal("/home/ziad/DSP/Digital-Signal-Processing-Tasks/input/Quan2_input.txt")
            s = quant.quantize_signal_levels(signal, int(num_value_input.get()))
        form.dsp_plot_continuous(s)

    # frames
    frame3_body = tk.Frame(window, width=800, height=590, bg=f2)
    frame3_body.grid(row=1, column=0)

    # frame body
    title_region = tk.Label(frame3_body, text="Quantization", height=1, font=('Ivy 18 bold'), bg=f2)
    title_region.place(x=180, y=10)

    ##quantalize##
    quant_value = tk.Label(frame3_body, text="Quantization Param", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    quant_value.place(x=5, y=140)

    # Combobox creation
    n = tk.StringVar()
    quantization_value = ttk.Combobox(frame3_body, width=27, textvariable=n)

    # Adding combobox drop down list
    quantization_value['values'] = ('Number of Levels', 'Number of Bits')
    quantization_value.place(x=250, y=142)
    quantization_value.current()

    ##num##
    num_value = tk.Label(frame3_body, text="Enter Number", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    num_value.place(x=10, y=200)
    num_value_input = tk.Entry(frame3_body, width=30)
    num_value_input.pack()
    num_value_input.place(x=185, y=200)


    ##plot_quant##
    plot_quant_button = tk.Button(frame3_body, text="Plot", bd=2, font="arial 10", fg="black", bg="silver",
                            height=1, command=on_plot_button_click)
    plot_quant_button.place(x=240, y=250)

def task4_form():
    file_path = ""
    polar_file_path = ""

    def load_file():
        nonlocal file_path
        file_path = askopenfilename()

    def load_polar():
        nonlocal polar_file_path
        polar_file_path = askopenfilename()

    def dft():
        signal = parser.read_signal(file_path)
        do_dft(signal)

    def dct():
        signal = parser.read_signal(file_path)
        do_dct(signal)

    def rmv_dct():
        signal = parser.read_signal(file_path)
        do_rmv_dct(signal)

    def idft():
        signal = parser.read_polar(polar_file_path)
        do_idft(signal)

    def do_dft(signal):
        signal_amp = FrequencyDomain.dft(signal, int(freq_value_input.get()), 1)
        form.dsp_plot_discrete(signal_amp, 'Frequency', 'Amplitude')
        signal_phase = FrequencyDomain.dft(signal, int(freq_value_input.get()), 0)
        form.dsp_plot_discrete(signal_phase, 'Frequency', 'Phase')
        signal = (signal_amp[1], signal_phase[1])
        parser.save_polar_signal(0, 1, signal)

    def do_idft(signal):
        if index_value_input.get() != '' and int(index_value_input.get()) >= 0:
            amp = FrequencyDomain.idft(signal, int(index_value_input.get()), int(amp_value_input.get()),
                                       float(phase_value_input.get()))
        else:
            amp = FrequencyDomain.idft(signal)
        signal = (range(len(amp)), amp)
        form.dsp_plot_discrete(signal)

    def do_dct(signal):
        signal = FrequencyDomain.dct(signal, m_value_input.get())
        print(signal)
        form.dsp_plot_discrete(signal)

    def do_rmv_dct(signal):
        signal = FrequencyDomain.rmv_dct(signal)
        print(signal)
        form.dsp_plot_discrete(signal)

    # frames
    frame4_body = tk.Frame(window, width=800, height=590, bg=f2)
    frame4_body.grid(row=1, column=0)

    # frame body
    title_region = tk.Label(frame4_body, text="Frequency Domain", height=1, font=('Ivy 18 bold'), bg=f2)
    title_region.place(x=180, y=10)

    # load file button
    load_button = tk.Button(frame4_body, text="Load File", bd=2, font="arial 10", fg="black", bg="beige", height=1,
                            command=load_file)
    load_button.place(x=200, y=80)

    # load file button
    load_polar_btn = tk.Button(frame4_body, text="Load Polar File", bd=2, font="arial 10", fg="black", bg="beige",
                               height=1,
                               command=load_polar)
    load_polar_btn.place(x=300, y=80)
    
    # num
    m_value = tk.Label(frame4_body, text="Enter M", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    m_value.place(x=10, y=150)
    m_value_input = tk.Entry(frame4_body, width=30)
    m_value_input.pack()
    m_value_input.place(x=260, y=150)

    # num
    freq_value = tk.Label(frame4_body, text="Enter Frequency(HZ)", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    freq_value.place(x=10, y=230)
    freq_value_input = tk.Entry(frame4_body, width=30)
    freq_value_input.pack()
    freq_value_input.place(x=260, y=230)

    # dft button
    dft_button = tk.Button(frame4_body, text="DFT", bd=2, font="arial 10", fg="black", bg="beige", height=1,
                           command=dft)
    dft_button.place(x=150, y=270)

    # idft button
    idft_button = tk.Button(frame4_body, text="IDFT", bd=2, font="arial 10", fg="black", bg="beige", height=1,
                            command=idft)
    idft_button.place(x=220, y=270)
    
    # dct button
    dct_button = tk.Button(frame4_body, text="DCT", bd=2, font="arial 10", fg="black", bg="beige", height=1,
                            command=dct)
    dct_button.place(x=290, y=270)

    # remove dct button
    rmv_dct_button = tk.Button(frame4_body, text="Remove DCT", bd=2, font="arial 10", fg="black", bg="beige", height=1,
                            command=rmv_dct)
    rmv_dct_button.place(x=360, y=270)

    ##index##
    index_value = tk.Label(frame4_body, text="Enter Index", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    index_value.place(x=10, y=350)
    index_value_input = tk.Entry(frame4_body, width=30)
    index_value_input.pack()
    index_value_input.place(x=220, y=350)

    ##amp##
    amp_value = tk.Label(frame4_body, text="Enter Amplitude", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    amp_value.place(x=10, y=400)
    amp_value_input = tk.Entry(frame4_body, width=30)
    amp_value_input.pack()
    amp_value_input.place(x=220, y=400)

    ##phase##
    phase_value = tk.Label(frame4_body, text="Enter Phase", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
    phase_value.place(x=10, y=450)
    phase_value_input = tk.Entry(frame4_body, width=30)
    phase_value_input.pack()
    phase_value_input.place(x=220, y=450)


task1_button = tk.Button(frame_body, text="Task1", bd=2, font="arial 10", fg="black", bg="beige", height=1,
                         command=task1_form)
task1_button.place(x=210, y=80)
task2_button = tk.Button(frame_body, text="Task2", bd=2, font="arial 10", fg="black", bg="beige", height=1,
                         command=task2_form)
task2_button.place(x=210, y=120)

task3_button = tk.Button(frame_body, text="Task3", bd=2, font="arial 10", fg="black", bg="beige", height=1,
                         command=task3_form)
task3_button.place(x=210, y=160)

task4_button = tk.Button(frame_body, text="Task4", bd=2, font="arial 10", fg="black", bg="beige", height=1,
                         command=task4_form)
task4_button.place(x=210, y=200)

window.mainloop()

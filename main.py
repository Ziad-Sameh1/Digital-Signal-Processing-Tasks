import tkinter as tk
import TextFileGenerator as txt
import FormGenerator as form
from tkinter import ttk

############################### task1 functions############################################################################
def sinusoidal():
    form.plot_sinusoidal(form.Amplitude_value_input.get(), form.theta_value_input.get(), form.Afreq_value_input.get(),
                         form.sfreq_value_input.get())

def cosinusoidal():
    form.plot_cosinusoidal(form.Amplitude_value_input.get(), form.theta_value_input.get(), form.Afreq_value_input.get(),
                         form.sfreq_value_input.get())


# create color
background_colour = '#000000'
f1 = '#FFEBCD'
f2 = '#ffffff'

# window
window = tk.Tk()
window.title("")
window.geometry('500x450')
window.configure(bg=background_colour)

# frames
frame_body = tk.Frame(window, width=700, height=590, bg=f2)
frame_body.grid(row=1, column=0)

# frame body
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
    # frames
    frame2_body = tk.Frame(window, width=700, height=590, bg=f2)
    frame2_body.grid(row=1, column=0)

    # frame body
    title_region = tk.Label(frame2_body, text="Arithmetic Operations", height=1, font=('Ivy 18 bold'), bg=f2)
    title_region.place(x=110, y=10)
    Add_button = tk.Button(frame2_body,text="   Addition   ", bd=2, font="arial 10", fg="black", bg="green", height=1)
    Add_button.place(x=140, y=80)
    sub_button = tk.Button(frame2_body,text="Subtraction", bd=2, font="arial 10", fg="black", bg="silver", height=1)
    sub_button.place(x=240, y=80)
    mul_button = tk.Button(frame2_body,text="Multiplication", bd=2, font="arial 10", fg="black", bg="yellow", height=1)
    mul_button.place(x=140, y=135)
    sq_button = tk.Button(frame2_body,text="  Squaring  ", bd=2, font="arial 10", fg="black", bg="pink", height=1)
    sq_button.place(x=240,y=135)
    accumulation_button = tk.Button(frame2_body,text="Accumulation", bd=2, font="arial 10", fg="black", bg="maroon", height=1)
    accumulation_button.place(x=180,y=185)
    ##shift##
    shift_value = tk.Label(frame2_body, text="Shift Value", height=1, font=('Ivy 15 bold'), fg="black", bg=f2)
    shift_value.place(x=10, y=250)
    shift_value_input = tk.Entry(frame2_body, width=30)
    shift_value_input.pack()
    shift_value_input.place(x=155, y=255)
    shift_button = tk.Button(frame2_body, text="shift", bd=2, font="arial 10", fg="black", bg="white",
                                    height=1)
    shift_button.place(x=365, y=250)
    ##Normalize##
    norm_value = tk.Label(frame2_body, text="Normalization", height=1, font=('Ivy 15 bold'), fg="black", bg=f2)
    norm_value.place(x=5, y=290)
    # Combobox creation
    n = tk.StringVar()
    normalization_value = ttk.Combobox(frame2_body, width=27, textvariable=n)

    # Adding combobox drop down list
    normalization_value['values'] = (' -1 to 1',
                              ' 1 to -1')
    normalization_value.place(x=155, y=295)
    normalization_value.current()
    norm_button = tk.Button(frame2_body, text="Normalize", bd=2, font="arial 10", fg="black", bg="white",
                                    height=1)
    norm_button.place(x=365, y=290)


task1_button = tk.Button(frame_body,text="Task1", bd=2, font="arial 10", fg="black", bg="beige", height=1, command=task1_form)
task1_button.place(x=210, y=80)
task2_button = tk.Button(frame_body,text="Task2", bd=2, font="arial 10", fg="black", bg="beige", height=1, command=task2_form)
task2_button.place(x=210, y=120)
window.mainloop()



import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.ttk as t
import TextFileGenerator as txt
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
title_region = tk.Label(frame_body, text="Signal Generator", height=1, font=('Ivy 18 bold'), bg=f2)
title_region.place(x=145, y=10)


## Amplitude
Amplitude_value = tk.Label(frame_body, text="Amplitude", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
Amplitude_value.place(x=10, y=110)
Amplitude_value_input = tk.Entry(frame_body,width=30)
Amplitude_value_input.pack()
Amplitude_value_input.place(x=210, y=115)
## Phase shift(theta)
theta_value = tk.Label(frame_body, text="Phase Shift", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
theta_value.place(x=10, y=150)
theta_value_input = tk.Entry(frame_body,width=30)
theta_value_input.pack()
theta_value_input.place(x=210, y=155)
##Analog frequency
Afreq_value = tk.Label(frame_body, text="Analog Frequency", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
Afreq_value.place(x=10, y=190)
Afreq_value_input = tk.Entry(frame_body,width=30)
Afreq_value_input.pack()
Afreq_value_input.place(x=210, y=195)

##sampling frequency
Afreq_value = tk.Label(frame_body, text="Sampling Frequency", height=1, font=('Ivy 15 bold'), fg="maroon", bg=f2)
Afreq_value.place(x=10, y=230)
Afreq_value_input = tk.Entry(frame_body,width=30)
Afreq_value_input.pack()
Afreq_value_input.place(x=210, y=235)

##text file signal button
submit_button = tk.Button(frame_body, text="Generate Text file Signal", bd=2, font="arial 10", fg="black", bg="silver", height=1, command=txt.plot_cont_disc)
submit_button.place(x=170, y=360)

##sine signal generator button
sine_button = tk.Button(frame_body, text="Sine Signal", bd=2, font="arial 10", fg="black", bg="silver", height=1)
sine_button.place(x=150, y=300)

##cosine signal generator button
cosine_button = tk.Button(frame_body, text="Cosine Signal", bd=2, font="arial 10", fg="black", bg="silver", height=1)
cosine_button.place(x=250, y=300)

window.mainloop()

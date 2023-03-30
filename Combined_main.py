from tkinter import *
import os
FONT_NAME = "Courier"

def call_GUI1():
    os.system('python ./TextToEyeBlink/main.py')
    return

def call_GUI2():
    os.system('python ./EyeBlink/eye_blink_Morse.py --shape-predictor ./EyeBlink/shape_predictor_68_face_landmarks.dat')
    return

if __name__ == "__main__":
    window = Tk()
    window.title("Bridge of Morse Code")
    window.config(padx=275, pady=100)    
    
    heading = Label(text="Bridge of Morse Code", font=(FONT_NAME, 50, "bold"))
    heading.grid(row=0, column=1)

    extra1 = Label(text="", font=(FONT_NAME, 32, "normal"))
    extra1.grid(row=2, column=1)

    label_gui_1 = Label(text="1. Text To Eye Blink: ", font=(FONT_NAME, 32, "normal"))
    label_gui_1.grid(row=3, column=1)
    button_gui_1 = Button(text="Enter", background='grey',  highlightthickness=0, height=3, width=15,
                      font=(FONT_NAME, 12, "bold"), command=call_GUI1)
    button_gui_1.grid(row=4, column=1)

    extra2 = Label(text="", font=(FONT_NAME, 32, "normal"))
    extra2.grid(row=5, column=1)

    label_gui_2 = Label(text="2. Eye Blink To Text: ", font=(FONT_NAME, 32, "normal"))
    label_gui_2.grid(row=6, column=1)
    button_gui_2 = Button(text="Enter", background='grey',  highlightthickness=0, height=3, width=15,
                        font=(FONT_NAME, 12, "bold"), command=call_GUI2)
    button_gui_2.grid(row=7, column=1)
    window.bind("<Escape>", lambda event:window.destroy())
    window.state('zoomed')
    window.mainloop()
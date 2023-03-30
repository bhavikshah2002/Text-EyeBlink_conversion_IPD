from tkinter import *
import morsecodetotext2
FONT_NAME = "Courier"

c = morsecodetotext2.texttomorsecode()
is_true=True
timer=None
ans=['/']
whole_word=' '
show_word=''
cur_i=0
cur_j=0
def morse_to_blink(i):
    global isLongBlink,timer
    # print(f"BlinkHere {i}")
    if i=="-":
        isLongBlink=2000
    elif i==".":
        isLongBlink=1000
    else:
        isLongBlink=3000
    window.after_cancel(timer)
    timer = window.after(20, Blink1)

def all_Code(i):
    global ans,timer,show_word,whole_word
    # print(f"allIndex {i}")
    if(i<len(ans)):
        window.after_cancel(timer)
        timer = window.after(20, singleCode,i,0)
    else:
        ans=['/']
        show_word=''
        whole_word=' '

    

def singleCode(i,j):
    global ans,timer,cur_i,cur_j,show_word,show_label
    cur_i=i
    cur_j=j
    if(j<len(ans[i])):
        # print(f"single{ans[i]} || {ans[i][j]}")
        window.after_cancel(timer)
        timer = window.after(50, morse_to_blink,ans[i][j])
    else:
        show_word+=whole_word[len(show_word)]
        show_label.config(text=f"Letter :{show_word}")
        window.after_cancel(timer)
        timer = window.after(1000, all_Code,i+1)

def on_enter_button_click():
    global ans,whole_word,show_word
    txt = text_str.get(1.0, "end-1c")
    text_str.delete(1.0, "end")
    txt = txt.lower()
    show_word=''
    whole_word=txt
    ans = c.text_to_morse(txt)
    if ans == ['']:
        show_word=''
        whole_word=''
        show_label.config(text=f"Data Not In Required Format!")



def on_start_button_click():
    global timer
    timer = window.after(20, all_Code,0)
        

window = Tk()
window.title("Text-To-Eye-Blink")
window.config(padx=100, pady=50)

canvas = Canvas(width=500, height=400, highlightthickness=0, background="grey")
canvas.grid(row=1, column=1)

# Time Of Blink
isLongBlink=2000


# Creating Eye
def createLeftEye(y1,y2):
    return canvas.create_oval(50, y1, 210, y2,outline = "black", fill = "white",width = 5)
    

def createRightEye(y1,y2):
    return canvas.create_oval(250, y1, 410, y2,outline = "black", fill = "white",width = 5)

# Creating Eye Positions
t11=createLeftEye(150,220)
t21=createRightEye(150,220)

t12=createLeftEye(160,210)
t22=createRightEye(160,210)

t13=createLeftEye(170,200)
t23=createRightEye(170,200)

t14=createLeftEye(180,190)
t24=createRightEye(180,190)

t15=createLeftEye(195,195)
t25=createRightEye(195,195)


heading = Label(text="Text to eye blink", font=(FONT_NAME, 50, "bold"))
heading.grid(row=0, column=5)

entry_label = Label(text="Enter a text: ", font=(FONT_NAME, 32, "normal"))
entry_label.place(x=650,y=115)

# text_str = Entry(width=50)
text_str = Text(window, height=10, width=60, font=(FONT_NAME, 12, "normal"))
text_str.grid(row=1, column=5, columnspan=2)
text_str.focus_set()

show_label = Label(text=f"Letter :{show_word}", font=(FONT_NAME, 24, "normal"))
show_label.place(x=550,y=400)

start_button = Button(text="Start", background='grey',  highlightthickness=0, height=3, width=15,
                      font=(FONT_NAME, 12, "bold"), command=on_start_button_click)
start_button.place(x=170,y=500)

enter_button = Button(text="Enter", background='grey',  highlightthickness=0, height=3, width=15,
                      font=(FONT_NAME, 12, "bold"), command=on_enter_button_click)
enter_button.grid(row=2, column=5, columnspan=2)



# Hiding And Showing Eye Positions
def hide_Eye(t1,t2):
    canvas.itemconfig(t1,state="hidden")
    canvas.itemconfig(t2,state="hidden")

def show_Eye(t1,t2):
    canvas.itemconfig(t1,state="normal")
    canvas.itemconfig(t2,state="normal")

hide_Eye(t12,t22)
hide_Eye(t13,t23)
hide_Eye(t14,t24)
hide_Eye(t15,t25)

eyes = [[t11,t21],[t12,t22],[t13,t23],[t14,t24],[t15,t25]]


# Logic Of Blink
def Blink_It(i):
    hide_Eye(eyes[i][0],eyes[i][1])
    show_Eye(eyes[i+1][0],eyes[i+1][1])

def Open_It(i):
    hide_Eye(eyes[i+1][0],eyes[i+1][1])
    show_Eye(eyes[i][0],eyes[i][1])

def Blink1():
    global timer
    window.after_cancel(timer)
    window.after(50, Blink_It,0)
    timer= window.after(50, Blink2) 
def Blink2():
    global timer
    window.after_cancel(timer)
    window.after(50, Blink_It,1)
    timer= window.after(50, Blink3) 
def Blink3():
    global timer
    window.after_cancel(timer)
    window.after(50, Blink_It,2)
    timer= window.after(50, Blink4) 
def Blink4():
    global timer, isLongBlink
    blinkTime=isLongBlink
    window.after_cancel(timer)
    window.after(50, Blink_It,3)
    timer= window.after(blinkTime, Open4) 
    

def Open4():
    global timer
    window.after_cancel(timer)
    window.after(50, Open_It,3)
    timer= window.after(50, Open3)
def Open3():
    global timer
    window.after_cancel(timer)
    window.after(50, Open_It,2)
    timer= window.after(50, Open2)
def Open2():
    global timer
    window.after_cancel(timer)
    window.after(50, Open_It,1)
    timer= window.after(50, Open1)
def Open1():
    global timer,is_true,cur_i,cur_j
    window.after_cancel(timer)
    window.after(50, Open_It,0)
    is_true=True
    timer= window.after(1000, singleCode,cur_i,cur_j+1)


window.mainloop()
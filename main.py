import tkinter
import math
wd = tkinter.Tk()
wd.configure(background="#271d1a")
wd.title("Calculator")
def click(number):
    e.insert(tkinter.END, number)
def c():
    e.delete(0, tkinter.END)
    cal_e.delete(0, tkinter.END)
def ce():
    e.delete(0, tkinter.END)
def backspace():
    current_text = e.get()
    if len(current_text) > 0:
        e.delete(len(current_text) - 1, tkinter.END)
def add_plu():
    global num1
    global cal
    num1 = e.get()
    c()
    cal = "+"
    cal_e.insert(tkinter.END, num1 + "+")
def add_min():
    global num1
    global cal
    num1 = e.get()
    c()
    cal = "-"
    cal_e.insert(tkinter.END, num1 + "-")
def add_div():
        global num1
        global cal
        num1 = e.get()
        c()
        cal = "/"
        cal_e.insert(tkinter.END, num1 + "÷")
def add_mul():
    global num1
    global cal
    num1 = e.get()
    c()
    cal = "*"
    cal_e.insert(tkinter.END, num1 + "×")

def prc():
    baseprc = float(e.get())
    base1prc = float((baseprc / 100))
    e.delete(0, tkinter.END)
    e.insert(0, base1prc)
def add_mem():
    global mem
    if len(mem) == 0:
        mem = e.get()
    else:
        e.insert(0, mem)
def opr_com():
        e.insert(tkinter.END, ".")
def numDivX():
    base = e.get()
    e.delete(0, tkinter.END)
    newbase = 1 / float(base)
    e.insert(0, newbase)
def expo():
    expo = float(e.get()) ** float(2)
    e.delete(0, tkinter.END)
    e.insert(0, expo)
def sqrt():
    sqrrt = math.sqrt(float(e.get()))
    e.delete(0, tkinter.END)
    e.insert(0, sqrrt)
def minplu():
    old_val = float(e.get())
    e.delete(0, tkinter.END)
    e.insert(0, old_val * -1)
def calc():
    global num1
    global cal
    num = e.get()
    num_ce = e.get()
    leng = len(num)
    cal_e.insert(tkinter.END, num_ce+"=")
    if leng == 0:
        return
    else:
        if cal == "+":
            result = float(num1) + float(e.get())
        if cal == "-":
            result = float(num1) - float(e.get())
        if cal == "/":
            input_val = e.get()
            if input_val == "0":
                e.delete(0, tkinter.END)
                e.insert(0, "Cannot divide by 0")
            else:
                result = float(num1) / float(input_val)
                e.delete(0, tkinter.END)
                e.insert(0, result)
        if cal == "*":
            result = float(num1) * float(e.get())
        e.delete(0, tkinter.END)
        e.insert(0, result)
def MS():
    global memory_MS
    global MC_request
    memory_MS = float(e.get())
def print_M():
    global memory_MS
    print(memory_MS)
def MC():
    global memory_MS
    memory_MS = 0
def MR():
    if memory_MS is not None:
        e.delete(0, tkinter.END)
        e.insert(0, memory_MS)
def M_plu():
    global memory_MS
    add_plu()
    e.insert(0, memory_MS)
def M_min():
    global memory_MS
    add_min()
    e.insert(0, memory_MS)
cal_e = tkinter.Entry(width=25, borderwidth= 0, font="Arial 15", background= "#271d1a", foreground="#ffffff")
e = tkinter.Entry(width=17, borderwidth= 0, font="Arial 16", background= "#2d1a1b", foreground="#ffffff")
bt_mem_clear = tkinter.Button(text="MC", width=4, height=1, command=MC, background="#271d1a", foreground="#ffffff")
bt_mem_recall = tkinter.Button(text="MR", width=4, height=1, command=MR, background="#271d1a", foreground="#ffffff")
bt_mem_plus = tkinter.Button(text="M+", width=4, height=1, command=M_plu, background="#271d1a", foreground="#ffffff")
bt_mem_min = tkinter.Button(text="M-", width=4, height=1, command=M_min, background="#271d1a", foreground="#ffffff")
bt_mem_store = tkinter.Button(text="MS", width=4, height=1, command=MS, background="#271d1a", foreground="#ffffff")
bt_mem_history = tkinter.Button(text="M↓", width=4, height=1,command=print_M, background="#271d1a", foreground="#ffffff")
bt0 = tkinter.Button(text="0", width=10, height=2, command=lambda: click(0), background= "#383032", foreground="#ffffff")
bt1 = tkinter.Button(text="1", width=10, height=2, command=lambda: click(1), background= "#383032", foreground="#ffffff")
bt2 = tkinter.Button(text="2", width=10, height=2, command=lambda: click(2), background= "#383032", foreground="#ffffff")
bt3 = tkinter.Button(text="3", width=10, height=2, command=lambda: click(3), background= "#383032", foreground="#ffffff")
bt4 = tkinter.Button(text="4", width=10, height=2, command=lambda: click(4), background= "#383032", foreground="#ffffff")
bt5 = tkinter.Button(text="5", width=10, height=2, command=lambda: click(5), background= "#383032", foreground="#ffffff")
bt6 = tkinter.Button(text="6", width=10, height=2, command=lambda: click(6), background= "#383032", foreground="#ffffff")
bt7 = tkinter.Button(text="7", width=10, height=2, command=lambda: click(7), background= "#383032", foreground="#ffffff")
bt8 = tkinter.Button(text="8", width=10, height=2, command=lambda: click(8), background= "#383032", foreground="#ffffff")
bt9 = tkinter.Button(text="9", width=10, height=2, command=lambda: click(9), background= "#383032", foreground="#ffffff")
bt_div = tkinter.Button(text="÷", width=10, height=2, command=add_div, background= "#383031", foreground="#ffffff")
bt_mul = tkinter.Button(text="×", width=10, height=2, command=add_mul, background= "#383031", foreground="#ffffff")
bt_min = tkinter.Button(text="-", width=10, height=2, command=add_min, background= "#383031", foreground="#ffffff")
bt_plu = tkinter.Button(text="+", width=10, height=2, command=add_plu, background= "#383031", foreground="#ffffff")
bt_eq = tkinter.Button(text="=", width=10, height=2, command=calc, background= "#dd765e", foreground="#ffffff")
bt_dec = tkinter.Button(text=",", width=10, height=2, command=opr_com, background= "#383032", foreground="#ffffff")
bt_prc = tkinter.Button(text="%", width=10, height=2, command=prc, background= "#383031", foreground="#ffffff")
bt_ce = tkinter.Button(text="CE", width=10, height=2, command=ce, background= "#383031", foreground="#ffffff")
bt_c = tkinter.Button(text="C", width=10, height=2, command=c, background= "#383031", foreground="#ffffff")
bt_bs = tkinter.Button(text="⌫", width=10, height=2, command=backspace, background= "#383031", foreground="#ffffff")
bt_1divX = tkinter.Button(text="1/𝑥", width=10, height=2, command=numDivX, background= "#383031", foreground="#ffffff")
bt_square = tkinter.Button(text="𝑥²", width=10, height=2, command=expo, background= "#383031", foreground="#ffffff")
bt_sqrt = tkinter.Button(text="²√𝑥", width=10, height=2, command=sqrt, background= "#383031", foreground="#ffffff")
bt_plus_minus = tkinter.Button(text="+/-", width=10, height=2,command = minplu, background= "#383032", foreground="#ffffff")
bt_options = tkinter.Button(text="☰", width=5, height=1, background="#271d1a", foreground="#ffffff")
Label = tkinter.Label(text="   Standart", height=2, background="#271d1a", foreground="#ffffff", font="Arial 8")
Label.config(font=("Helvetica", 12, "bold"))
cal_e.grid(row=1, column=0, columnspan=5, padx=0, pady=5)
e.grid(row=2, column=0, columnspan=5, padx=0, pady=15)
bt_prc.grid(row=4, column=0, padx=3, pady=3)
bt_ce.grid(row=4, column=1, padx=3, pady=3)
bt_c.grid(row=4, column=2, padx=3, pady=3)
bt_bs.grid(row=4, column=3, padx=3, pady=3)
bt_1divX.grid(row=5, column=0, padx=3, pady=3)
bt_square.grid(row=5, column=1, padx=3, pady=3)
bt_sqrt.grid(row=5, column=2, padx=3, pady=3)
bt_div.grid(row=5, column=3, padx=3, pady=3)
bt7.grid(row=6, column=0, padx=3, pady=3)
bt8.grid(row=6, column=1, padx=3, pady=3)
bt9.grid(row=6, column=2, padx=3, pady=3)
bt_mul.grid(row=6, column=3, padx=3, pady=3)
bt4.grid(row=7, column=0, padx=3, pady=3)
bt5.grid(row=7, column=1, padx=3, pady=3)
bt6.grid(row=7, column=2, padx=3, pady=3)
bt_min.grid(row=7, column=3, padx=3, pady=3)
bt1.grid(row=8, column=0, padx=3, pady=3)
bt2.grid(row=8, column=1, padx=3, pady=3)
bt3.grid(row=8, column=2, padx=3, pady=3)
bt_plu.grid(row=8, column=3, padx=3, pady=3)
bt_plus_minus.grid(row=9, column=0, padx=3, pady=3)
bt0.grid(row=9, column=1, padx=3, pady=3)
bt_dec.grid(row=9, column=2, padx=3, pady=3)
bt_eq.grid(row=9, column=3, padx=3, pady=3)
Label.grid(column=1, row=0)
bt_options.grid(column=0, row=0)
bt_mem_clear.grid(column=0, row=3, padx=3, pady=3, sticky='w')
bt_mem_recall.grid(column=0, row=3, padx=3, pady=3, sticky='e')
bt_mem_plus.grid(column=1, row=3, padx=3, pady=3, sticky='e')
bt_mem_min.grid(column=2, row=3, padx=3, pady=3, sticky='w')
bt_mem_store.grid(column=3, row=3, padx=3, pady=3, sticky='w')
bt_mem_history.grid(column=3, row=3, padx=3, pady=3, sticky='e')
wd.mainloop()
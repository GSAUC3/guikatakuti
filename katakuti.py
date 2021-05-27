import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import font

win = Tk()
win.resizable(height=False,width=False)
win.title('KataKuti')

def disable():
    for i in buttons:
        i.config(state=DISABLED)
    


def check():
    global jiteche
    jiteche = False
    # ----horizontal check---- 
    for i in range(3):
        if buttons[0+i*3]["text"]== 'X' and buttons[1+i*3]["text"]=='X' and buttons[2+i*3]["text"]=='X':
            buttons[0+i*3].config(bg="yellow")
            buttons[1+i*3].config(bg="yellow")
            buttons[2+i*3].config(bg="yellow")
            jiteche = True
 
            messagebox.showinfo("KataKuti", " X babaji you Won!!")
            disable()

    # -----VERTICAL check----- 
    for i in range(3):
        if buttons[0+i]["text"]== 'X' and buttons[3+i]["text"]=='X' and buttons[6+i]["text"]=='X':
            buttons[0+i].config(bg="yellow")
            buttons[3+i].config(bg="yellow")
            buttons[6+i].config(bg="yellow")
            jiteche = True
            messagebox.showinfo("KataKuti", " X babaji you Won!!")
            disable()

    # -----diagonal check----- 
    if buttons[0]["text"]=='X' and buttons[4]["text"]=='X' and buttons[8]["text"]=='X':
        buttons[0].config(bg="yellow")
        buttons[4].config(bg="yellow")
        buttons[8].config(bg="yellow")
        jiteche = True
        messagebox.showinfo("KataKuti", " X babaji you Won!!")
        disable()

    if buttons[2]["text"]=='X' and buttons[4]["text"]=='X' and buttons[6]["text"]=='X': 
        buttons[2].config(bg="yellow")
        buttons[4].config(bg="yellow")
        buttons[6].config(bg="yellow")
        jiteche = True
        messagebox.showinfo("KataKuti", " X babaji you Won!!")
        disable()
        
        # ------------checking for o-------------- 
     # ----horizontal check---- 
    for i in range(3):
        if buttons[0+i*3]["text"]== 'O' and buttons[1+i*3]["text"]=='O' and buttons[2+i*3]["text"]=='O':
            buttons[0+i*3].config(bg="skyblue")
            buttons[1+i*3].config(bg="skyblue")
            buttons[2+i*3].config(bg="skyblue")
            jiteche = True
            messagebox.showinfo("KataKuti", " O babaji you Won!!")
            disable()

    # -----VERTICAL check----- 
    for i in range(3):
        if buttons[0+i]["text"]== 'O' and buttons[3+i]["text"]=='O' and buttons[6+i]["text"]=='O':
            buttons[0+i].config(bg="skyblue")
            buttons[3+i].config(bg="skyblue")
            buttons[6+i].config(bg="skyblue")
            jiteche = True
            messagebox.showinfo("KataKuti", " O babaji you Won!!")
            disable()

    # -----diagonal check----- 
    if buttons[0]["text"]=='O' and buttons[4]["text"]=='O' and buttons[8]["text"]=='O':
        buttons[0].config(bg="skyblue")
        buttons[4].config(bg="skyblue")
        buttons[8].config(bg="skyblue")
        jiteche = True
        messagebox.showinfo("KataKuti", " O babaji you Won!!")
        disable()

    if buttons[2]["text"]=='O' and buttons[4]["text"]=='O' and buttons[6]["text"]=='O': 
        buttons[2].config(bg="skyblue")
        buttons[4].config(bg="skyblue")
        buttons[6].config(bg="skyblue")
        jiteche = True
        messagebox.showinfo("KataKuti", " O babaji you Won!!")
        disable()
    
    if count == 9 and jiteche==False:
        for i in buttons:
            i.config(bg="red")
        messagebox.showinfo("KataKuti", "Toder Kopal Pora!")
        disable()


def bclick(b):
    global tipeche,count

    if b["text"]== " " and tipeche==True:
        b["text"] = 'X'
        tipeche =False 
        count+=1
        check()
    elif b["text"] ==" " and tipeche==False:
        b["text"] = "O"
        tipeche =True
        count+=1
        check()
    else:
        messagebox.showerror("KataKuti","Chompaa! kana naki??")

def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,tipeche,count
    
    tipeche = True 
    count =0 
    b1 = Button(win, text=" ",font=("Arial",10), height= 3,width= 6, command= lambda: bclick(b1))
    b2 = Button(win, text=" ",font=("Arial",10), height= 3,width= 6, command= lambda: bclick(b2))
    b3 = Button(win, text=" ",font=("Arial",10), height= 3,width= 6, command= lambda: bclick(b3))
    b4 = Button(win, text=" ",font=("Arial",10), height= 3,width= 6, command= lambda: bclick(b4))
    b5 = Button(win, text=" ",font=("Arial",10), height= 3,width= 6, command= lambda: bclick(b5))
    b6 = Button(win, text=" ",font=("Arial",10), height= 3,width= 6, command= lambda: bclick(b6))
    b7 = Button(win, text=" ",font=("Arial",10), height= 3,width= 6, command= lambda: bclick(b7))
    b8 = Button(win, text=" ",font=("Arial",10), height= 3,width= 6, command= lambda: bclick(b8))
    b9 = Button(win, text=" ",font=("Arial",10), height= 3,width= 6, command= lambda: bclick(b9))
    

    global buttons
    buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    

    
    x=0
    for i in range(3):
        for j in range(3):
            buttons[x].grid(row=i,column=j)
            x+=1

reset()
rset = Button(win,text='RESET',command=reset)
rset.grid(row=4,column=1)

win.mainloop()
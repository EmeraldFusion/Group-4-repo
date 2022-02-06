from tkinter import *

gooe = Tk()

lbl=Label(gooe, text="Chiro v3 (CHOOSE MODE)", fg='black', font=("Times New Roman", 20))
lbl.pack(side=TOP)
lb2=Label(gooe, text="Close modes below title after mode chosen", fg='black', font=("Times New Roman", 20))
lb2.pack(side=BOTTOM)

def HideB(button):
    button.grid_forget()
    
def Auto():
    #Create the window when Auto is pressed
    AutWin = Toplevel(gooe)
    AutWin.title("Auto Mode")
    AutWin.geometry("800x600")
    
    #Create a button on the main window to close the mode
    AutB = Button(gooe, text="Close Auto", command=lambda: AutWin.destroy).pack()

    #simple labels for the new window
    lbA=Label(AutWin, text="Chiro v3 (AUTOPILOT MODE)", font=("Times New Roman", 20))
    lbA.pack(side=TOP)
    lbA2=Label(AutWin, text="Chiro v3 is in autopilot mode, sit back and let him run", font=("Times New Roman", 20))
    lbA2.place(x=100, y=300)
    lbA3=Label(AutWin, text="Close autopilot in the main to stop and choose mode", bg='yellow', font=("Times New Roman", 20))
    lbA3.pack(side=BOTTOM)

def Manual():
    #Create the window when manual is pressed
    ManWin = Toplevel(gooe)
    ManWin.title("Manual Mode")
    ManWin.geometry("800x600")
    
    #Create a button on the main window to close the mode
    ManB = Button(gooe, text="Close Manual", command=lambda: ManWin.destroy).pack()
    
    #simple label for the new window
    lbM=Label(ManWin, text="Chiro v3 (MANUAL MODE)", fg='black', font=("Times New Roman", 20))
    lbM.pack(side=TOP)
    lbM2=Label(ManWin, text="Close Manual in the main to stop and choose mode", bg='yellow', font=("Times New Roman", 20))
    lbM2.pack(side=BOTTOM)
    
    #movement controls for chiro v3
    btnmS=Button(ManWin, text="STOP", width=20, height=10, bg='yellow')
    btnmS.place(x=325,y=250)
    btnm1=Button(ManWin, text="Forward", width=20, height=10, bg='green')
    btnm1.place(x=325,y=100)
    btnm2=Button(ManWin, text="Left",width=20, height=10, bg='green')
    btnm2.place(x=175,y=250)
    btnm3=Button(ManWin, text="Back", width=20, height=10, bg='green')
    btnm3.place(x=325,y=400)
    btnm4=Button(ManWin, text="Right", width=20, height=10, bg='green')
    btnm4.place(x=475,y=250)


#created buttons on the main window for the 2 modes to be chosen
Bootun = Button(gooe, text="AUTO", width=10, height=30, bg='red', font=("Helvetica", 20), command=Auto)
Bootun.pack(side=LEFT)

Bootun2 = Button(gooe, text="MANUAL", width=10, height=30, bg='green', font=("Helvetica", 20), command=Manual)
Bootun2.pack(side=RIGHT)

'''
#These are if anyone needed extra options to make things more flashy
input=Entry(gooe, text="input here", bd=5)
input.place(x=80, y=150)
button_1 = TkinterCustomButton(text="My Button", corner_radius=10, command=button_function)
button_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
command=lambda: callback_and_hide(Button2)
button(gooe, text="quit", command-gooe.destroy).pack

lbl.configure(text="Chiro v3 (MANUAL ON)", font=("Times New Roman", 20))
btnm1=Button(gooe, text="Forward")
btnm1.place(anchor=CENTER)
btnm2=Button(gooe, text="Left")
btnm2.pack(side=BOTTOM)
btnm3=Button(gooe, text="Back")
btnm3.place(anchor=NW)
btnm4=Button(gooe, text="Right")
btnm4.place(anchor=SE)
'''

#Create window geometry and title, the activate
gooe.title("Chiro v3 Controls")
gooe.geometry("800x600")
gooe.mainloop()

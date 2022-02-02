from tkinter import *

# Makes the window, titles it Chiro, and sets the perimeter
window = Tk()
window.title("Chiro")
window.geometry('350x200')

# makes a label called Chiro with font and size, and sets its position (needs work)
lbl = Label(window, text="Chiro", font=("Arial Bold", 40))
lbl.grid(column=3000, row=100)

# changes the text and adds 4 buttons when the manual button is clicked (needs work)
def clicked():
    lbl.configure(text="Chiro Manual Piloting Mode", font=("Arial", 15))
    btnm1=Button(window, text="Forward")
    btnm1.grid(column=1, row=1)
    btnm2=Button(window, text="Left")
    btnm2.grid(column=1,row=2)
    btnm3=Button(window, text="Back")
    btnm3.grid(column=1, row=3)
    btnm4=Button(window, text="Right")
    btnm4.grid(column=1, row=4)

# changes the text when the auto button is clicked
def clicked2():
    lbl.configure(text="Chiro Autopilot Mode", font=("Arial", 15))

# the manual button (needs work)
btn = Button(window, text="Manual", command=clicked)
btn.grid(column=3000, row=1)

# the auto button (needs work)
btn2 = Button(window, text="Auto", command=clicked2)
btn2.grid(column=1500, row=1)

# has the window stay until destroyed
window.mainloop()

from tkinter import *
window = Tk()


btn=Button(window, text="Continue", fg='black', bg='cyan')
btn.place(x=275, y=100)
lbl=Label(window, text="Global Pollution", fg='cyan', font=("Helvetica", 18))
lbl.place(x=220, y=50)

window.title('Quiz on Global pollution')
window.geometry("650x400+10+20")
window.mainloop()
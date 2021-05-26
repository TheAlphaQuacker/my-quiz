from tkinter import *

class main_screen:
    def __init__ (self, master):
        self.master = master
        master.title("Quiz on Global Pollution")

        background_color = "black"

        self.quiz_frame = Frame(master, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame, text = "Global Pollution", font=("Tw Cen MT", "20"),bg = background_color, fg = 'cyan', padx = 20, pady = 20)
        self.heading_label.grid(row = 1, padx = 10)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)

        self.start_button = Button(self.quiz_frame, text="Start", font=("Helvetica", "13", "bold"), bg=background_color)

root = Tk()
mainscreen = main_screen(root)
root.mainloop()
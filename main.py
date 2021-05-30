from tkinter import *
import random
global question_answer
names_list = []
asked = []
score = 0

question_answers = {}

class MainScreen:
    def __init__ (self, master):
        self.master = master
        master.title("Quiz on Global Pollution")

        background_color = "black"

        self.quiz_frame = Frame(master, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame, text = "Global Pollution", font=("Tw Cen MT", "20"),bg = background_color, fg = 'cyan', padx = 20, pady = 20)
        self.heading_label.grid(row = 1, padx = 20, pady = 20)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)

        #start button
        self.start_button = Button(self.quiz_frame, text="Start", font=("Helvetica", "13", "bold"),fg='cyan', bg=background_color, command=self.name_collection)
        self.start_button.grid(row=3, padx=20, pady=20)
        
        #Leaderboard
        self.Leaderboard_Button = Button(self.quiz_frame, text="LeaderBoard", font=("Helvetica", "13", "bold"),fg='cyan', bg=background_color, command=self.name_collection)
        self.Leaderboard_Button.grid(row=4, padx=20, pady=20) 

    def name_collection(self):
        name = self.entry_box.get()
        names_list.append (name)
        self.quiz_frame.destroy()
        Quiz(root)

class Quiz:
    def __init__ (self,master):
        self.master = master
        master.title("Quiz on Global Pollution")

        background_color = "black"

        self.quiz_frame = Frame(master, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()

    
root = Tk()
root.title("Quiz on Global Pollution")
mainscreen = MainScreen(root)
root.mainloop()

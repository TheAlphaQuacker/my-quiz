from tkinter import *
import random

global question_answer
names_list = []
asked = []
score = 0

question_answer = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
}


def randomiser():
    global qnum  #the question number is the key in the dictionary question_answers, we have 10 keys (10 questions)
    qnum = random.randint(1, 10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


class MainScreen:
    def __init__(self, master):
        self.master = master
        master.title("Quiz on Global Pollution")

        background_color = "black"

        self.quiz_frame = Frame(master,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame,
                                   text="Global Pollution",
                                   font=("Pacifico", "20"),
                                   bg=background_color,
                                   fg='cyan',
                                   padx=20,
                                   pady=20)
        self.heading_label.grid(row=1, padx=20, pady=20)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)

        #start button
        self.start_button = Button(self.quiz_frame,
                                   text="Start",
                                   font=("Pacifico", "13", "bold"),
                                   fg='black',
                                   bg="cyan",
                                   command=self.name_collection)
        self.start_button.grid(row=3, padx=20, pady=20)

        #Leaderboard
        self.Leaderboard_Button = Button(self.quiz_frame,
                                         text="LeaderBoard",
                                         font=("Pacifico", "13", "bold"),
                                         fg='black',
                                         bg="cyan")
        self.Leaderboard_Button.grid(row=4, padx=20, pady=20)

        #quit button
        self.Quit_Button = Button(self.quiz_frame,
                                  text="Quit",
                                  font=("Pacifico", "13", "bold"),
                                  fg='black',
                                  bg="cyan")
        self.Quit_Button.grid(row=5, padx=20, pady=20)

    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        self.quiz_frame.destroy()
        Quiz(root)


class Quiz:
    def __init__(self, master):
        self.master = master
        master.title("Quiz on Global Pollution")

        background_color = "black"

        self.quiz_frame = Frame(master,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()

        self.question_label = Label(self.quiz_frame,
                                    text=question_answer[qnum][0],
                                    font=("Pacifico", "16"),
                                    fg='black',
                                    bg="cyan")
        self.question_label.grid(row=1, padx=20, pady=20)

        self.var1 = IntVar()

        self.rb1 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][1],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=1,
                               padx=10
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background = "cyan"
                               fg="black")
        self.rb1.grid(row=2,sticky=W)

        self.rb2 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][2],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=2,
                               padx=10
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background = "cyan"
                               fg="black")
        self.rb2.grid(roow=3, sticky=W)

        self.rb3 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][3],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=2,
                               padx=10
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background = "cyan"
                               fg="black")
        self.rb3.grid(roow=4, sticky=W)

        self.rb4 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][4],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=2,
                               padx=10
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background = "cyan"
                               fg="black")
        self.rb4.grid(roow=5, sticky=W)

        self.rb5 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][5],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=2,
                               padx=10
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background = "cyan"
                               fg="black")
        self.rb5.grid(roow=6, sticky=W)

root = Tk()
root.title("Quiz on Global Pollution")
mainscreen = MainScreen(root)
root.mainloop()

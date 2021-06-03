from tkinter import *
import random

global question_answer
names_list = []
asked = []
score = 0

question_answer = {
    1: [
        "What is Pollution?",
        'The release of anything that is harmful to the environment',
        'playing too much games', 'eating too much sweets',
        'throwing garbage on the ground', 'killing animals',
        'The release of anything that is harmful to the environment', 1
    ],
    2: [
        "How does pollution affect the environment?",
        'long term exposure to air pollution can lead to chronic diseases',
        'it kill plants and animal life',
        'it causes the soil to turn infertile',
        'pollution can cause harmful weather like smog', 'all of them',
        'all of them', 5
    ],
    3: [
        "Which country creates the most pollution?", 'Brazil', 'China',
        'United States of America', 'Germany', 'Russia', 'China', 2
    ],
    4: [
        "Which country creates the least pollution?", 'New Zealand', 'Finland',
        'France', 'Sweden', 'Australia', 'Sweden', 4
    ],
    5: [
        "What are greenhouse gases?", 'gases that make the earth colder',
        'gases that are poisnous',
        'gases that create a greenhouse effect by trapping the heat inside the earths atmosphere',
        'gases inside a greenhouse', 'gases that make your house green',
        'gases that create a greenhouse effect by trapping the heat inside the earths atmosphere',
        3
    ],
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
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="cyan",
                               fg="black")
        self.rb1.grid(row=2, sticky=W)

        self.rb2 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][2],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=2,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="cyan",
                               fg="black")
        self.rb2.grid(row=3, sticky=W)

        self.rb3 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][3],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=3,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="cyan",
                               fg="black")
        self.rb3.grid(row=4, sticky=W)

        self.rb4 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][4],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=4,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="cyan",
                               fg="black")
        self.rb4.grid(row=5, sticky=W)

        self.rb5 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][5],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=5,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="cyan",
                               fg="black")
        self.rb5.grid(row=6, sticky=W)

        self.quiz_instance = Button(self.quiz_frame,
                                    text="Confirm",
                                    font=("Helvetica", "13", "bold"),
                                    bg="cyan",
                                    command=self.test_progress)

        self.quiz_instance.grid(row=7, padx=5, pady=5)

        self.score_label=Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT","16"), bg=background_color)
        self.score_label.grid(row=8, padx=10, pady=1)

    def question_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=question_answer[qnum][0])
        self.rb1.config(text=question_answer[qnum][1])
        self.rb2.config(text=question_answer[qnum][2])
        self.rb3.config(text=question_answer[qnum][3])
        self.rb4.config(text=question_answer[qnum][4])
        self.rb5.config(text=question_answer[qnum][5])

    def test_progress(self):
        global score
        scr_label=self.score_label
        choice=self.var1.get()
        if len(asked)>9:
            if choice ==question_answer[qnum][6]:
                score+=1
                scr_label.config(text=score)
                self.quiz_instance.config(text="Confirm")

            else:
                score+=0
                scr_label.config(text="The correct answer was: " + question_answer[qnum][5] )
                self.quiz_instance.config(text="Confirm")

        else:
            if choice ==0:
                self.quiz_instance.config(text="Try Again, You didn't select an option then submit again")
                choice=self.var1.get()
            else:
                if choice == question_answer[qnum][6]:
                    score+=1
                    scr_label.config(text=score)
                    self.quiz_instance.config(text="Confirm")
                else:
                    print(choice)
                    score+=0
                    scr_label.configure(text="The correct answer was: "+question_answer[qnum][5])
                    self.quiz_instance.config(text="Confirm")
                    self.question_setup()


class End:
    def __init__(self):
        background="black"

        self.end_box=Toplevel(root)
        self.end_box.title

randomiser()
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz on Global Pollution")
    quiz_instance = MainScreen(root)
    root.mainloop()

root = Tk()
root.title("Quiz on Global Pollution")
mainscreen = MainScreen(root)
root.mainloop()

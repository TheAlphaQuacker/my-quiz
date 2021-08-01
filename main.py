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
        'United States of America', 
        'Germany', 
        'Russia', 
        'China', 
        2
    ],
    4: [
        "Which country creates the least pollution?", 
        'New Zealand', 
        'Finland',
        'France', 
        'Sweden', 
        'Australia', 
        'Sweden', 
        4
    ],
    5: [
        "What are greenhouse gases?", 'gases that make the earth colder',
        'gases that are poisnous',
        'gases that create a greenhouse effect by trapping the heat inside the earths atmosphere',
        'gases inside a greenhouse', 
        'gases that make your house green',
        'gases that create a greenhouse effect by trapping the heat inside the earths atmosphere',
        3
    ],
    6: [
        "Which one of these industry creates the most pollution globally?",
        'transport industry', 
        'construction industry', 
        'tech industry',
        'fuel industry', 
        'agriculture', 
        'fuel industry', 4
    ],
    7: [
        "How many people die everyday due to unclean drinking water caused by pollution",
        '5,000 people', 
        '20,000 people', 
        '100,000 people', 
        '1,000,000 people',
        '2,500 people', 
        '5,000 people', 
        1],
    8:[
        "What type of energy source causes the most pollution?", 
        'hydro power', 
        'Oil', 
        'solar', 
        'wind', 
        'natural gas', 
        'oil', 
        2],
    9:[
        "What causes the most pollution in the seas?", 
        'Plastic', 
        'Oil spills', 
        'Ship wrecks', 
        'dead sea animals', 
        'water', 
        'Plastic', 
        1],
    10:[
        "What kind of pollution does nuclear reactors create", 
        'air pollution', 
        'noise pollution', 
        'radioactive pollution', 
        'water pollution', 
        'space pollution', 
        'radioactive pollution', 
        3]
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
        #main screen window 
        self.quiz_frame = Frame(master,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()
        #name of quiz
        self.heading_label = Label(self.quiz_frame,
                                   text="Global Pollution",
                                   font=("Pacifico", "20"),
                                   bg=background_color,
                                   fg='cyan',
                                   padx=20,
                                   pady=20)
        self.heading_label.grid(row=1, padx=20, pady=20)
        #adds the place to enter name
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
        #quit button
        self.Quit_Button = Button(self.quiz_frame,
                                  text="Quit",
                                  font=("Pacifico", "13", "bold"),
                                  fg='black',
                                  bg="cyan",
                                  command=self.end_screen)
        self.Quit_Button.grid(row=5, padx=20, pady=20)


    def end_screen(self):
        root.withdraw()
        open_endscreen = End(root)

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
        #creates Quiz window
        self.quiz_frame = Frame(master,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()
        #adds the question
        self.question_label = Label(self.quiz_frame,
                                    text=question_answer[qnum][0],
                                    font=("Pacifico", "16"),
                                    fg='black',
                                    bg="cyan")
        self.question_label.grid(row=1, padx=20, pady=20)
        #add variable 1
        self.var1 = IntVar()
        #radiobutton
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
        #adds radiobuttun 2
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
        #adds radio button 3
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
        #adds radiobutton 4
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
        #adds radiobutton 5
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
        #adds confirm button
        self.confirm_button = Button(self.quiz_frame,
                                     text="Confirm",
                                     font=("Helvetica", "13", "bold"),
                                     bg="cyan",
                                     command=self.test_progress)

        self.confirm_button.grid(row=7, padx=5, pady=5)
        #Adds end quiz button
        self.end_quiz = Button(self.quiz_frame,
                               text="End Quiz",
                               font=("Helvetica", "13", "bold"),
                               bg="cyan",
                               command=self.end_screen)
        self.end_quiz.grid(row=9, padx=10, pady=10)
        #adds score label which tells you correct answer
        self.score_label = Label(self.quiz_frame,
                                 text="SCORE",
                                 font=("Tw Cen MT", "16"),
                                 bg=background_color,
                                 fg="cyan")
        self.score_label.grid(row=8, padx=10, pady=1)
    #sets up the radio buttons
    def question_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=question_answer[qnum][0])
        self.rb1.config(text=question_answer[qnum][1])
        self.rb2.config(text=question_answer[qnum][2])
        self.rb3.config(text=question_answer[qnum][3])
        self.rb4.config(text=question_answer[qnum][4])
        self.rb5.config(text=question_answer[qnum][5])
    #sets up score label
    def test_progress(self):
        global score
        scr_label = self.score_label
        choice = self.var1.get()
        if len(asked) > 9:
            if choice == question_answer[qnum][6]:
                score += 1
                scr_label.config(text=score)
                self.confirm_button.config(text="Confirm")

            else:
                score += 0
                scr_label.config(text="The correct answer was: " +
                                 question_answer[qnum][6])
                self.confirm_button.config(text="Confirm")

        else:
            if choice == 0:
                self.confirm_button.config(
                    text=
                    "Try Again, You didn't select an option then submit again")
                choice = self.var1.get()
            else:
                if choice == question_answer[qnum][6]:
                    score += 1
                    scr_label.config(text=score)
                    self.confirm_button.config(text="Confirm")
                else:
                    print(choice)
                    score += 0
                    scr_label.configure(text="The correct answer was: " +
                                        question_answer[qnum][6])
                    self.confirm_button.config(text="Confirm")
                    self.question_setup()
    #adds end method
    def end_screen(self):
        root.withdraw()
        open_endscreen = End(root)



class End:
    def __init__(self,master):
        background = "black"


        self.end_box = Toplevel(root)
        self.end_box.title("End Box")

        self.end_frame = Frame(self.end_box,
                               width=1000,
                               height=1000,
                               bg=background,
                               )
        self.end_frame.grid()

        self.end_heading = Label(self.end_frame,
                            text='Well Done',
                            font=('Tw Cent Mt', 22, 'bold'),
                            bg=background,
                            pady=15)
        self.end_heading.grid(row=0)

        self.exit_button = Button(self.end_frame,
                             text='Exit',
                             width=10,
                             bg='cyan',
                             font=('Tw Cent Mt', 12, 'bold'),
                             command=self.close_end)
        self.exit_button.grid(row=4, pady=20)

    def close_end(self):
        self.end_box.destroy()
        root.withdraw()


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

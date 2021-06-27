from tkinter import *
from tkinter import messagebox
import json


class Quiz:
    # constructors
    def __init__(self):

        self.question_num = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0
        self.check_result()
        self.timer()
        self.attempted = [False] * len(question)

    # function shows the result
    def display_result(self):

        score = f"Score: {self.correct}"
        messagebox.showinfo("Result", f"{score}")

    # check if the answer selected is correct
    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

    # This method is used to check the answer of the current question
    def check_btn(self):
        if self.attempted[self.question_num]:
            check.config(text="Already attempted", fg="red")
        else:
            self.attempted[self.question_num] = True
            if self.check_ans(self.question_num):
                self.correct += 1
                check.config(text="You are correct", fg="green")
            else:
                check.config(text="Incorrect", fg="red")


        if self.question_num == self.data_size - 1:

            self.display_result()
            gui.destroy()

    # Skip to the next question without check it
    def skip_btn(self):
        check.config(text=" ", fg="green")
        self.question_num += 1

        if self.question_num == self.data_size:

            self.question_num = 0
            self.display_question()
            self.display_options()
        else:
            self.display_question()
            self.display_options()

    # Go back to the previous question
    def prev_btn(self):
        check.config(text=" ", fg="green")

        self.question_num -= 1
        if self.question_num == self.data_size:

            self.question_num = 0
            self.display_question()
            self.display_options()
        else:
            self.display_question()
            self.display_options()

    # make buttons to display
    def buttons(self):

        check_button = Button(gui, text="Check", command=self.check_btn,
                             width=10, bg="blue", fg="white", font=("Comic Sans MS", 16, "bold"))
        next_button = Button(gui, text="next", command=self.skip_btn,
                             width=10, bg="blue", fg="white", font=("Comic Sans MS", 16, "bold"))
        prev_button = Button(gui, text="prev", command=self.prev_btn,
                             width=10, bg="blue", fg="white", font=("Comic Sans MS", 16, "bold"))

        check_button.place(x=350, y=380)
        next_button.place(x=650, y=380)
        prev_button.place(x=50, y=380)

    # shows which option is selected
    # and select other options others are selected
    def display_options(self):

        val = 0
        self.opt_selected.set(0)
        for option in options[self.question_num]:
            self.opts[val]['text'] = option
            val += 1

    # function for display question
    def display_question(self):

        q_no = Label(gui, text=question[self.question_num], width=60,
                     font=('comic sans', 16, 'bold'), anchor='w')
        q_no.place(x=70, y=100)

    # Display title
    def display_title(self):

        title = Label(gui, text="CANADA GEOGRAPHY QUIZ",
                      width=50, bg="red", fg="white", font=("Comic Sans MS", 20, "bold"))
        title.place(x=-80, y=0)

    # Display the option in a radio button format
    def radio_buttons(self):

        q_list = []
        y_pos = 150

        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("Comic Sans MS", 14))

            q_list.append(radio_btn)

            radio_btn.place(x=100, y=y_pos)

            y_pos += 40

        return q_list

    # display check
    def check_result(self):
        global check
        check = Label(gui, text=" ",
                      width=50, fg="red", font=("Comic Sans MS", 16, "bold"))
        check.place(x=-300, y=310)

    # a 3 min count down timer
    def timer(self, countdown=180):
        print(countdown)
        a = Label(gui, text="1", width=50, fg="red", font=("Comic Sans MS", 16, "bold"))
        a.place(x=320, y=50)
        if countdown > 0:
            a.config(text=countdown)
            countdown -= 1
            a.after(1000, lambda: self.timer(countdown))
        elif countdown == 0:
            self.display_result()
            gui.destroy()


# Create a GUI Window
gui = Tk()


# set the size of the GUI Window
gui.geometry("900x450")

# set the title of the Window
gui.title("CANADA GEOGRAPHY QUIZ")

# get the data from the json file
with open('data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])

quiz = Quiz()

gui.mainloop()

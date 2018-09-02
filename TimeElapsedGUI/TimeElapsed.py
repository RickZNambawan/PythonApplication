# Time Elapsed Application
# Let you convert hour or minute into seconds

from tkinter import *
import tkinter.messagebox


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.hour = IntVar()
        self.minute = IntVar()
        self.second = IntVar()
        self.createWidgets()

    def createWidgets(self):
        self.programTitle = Label(self, font=("times new roman", 20, "bold"), text="Program: Time Elapsed", fg="hot pink", bd=2, anchor="n")
        self.programTitle.grid(row=0, columnspan=5)

        Label(self, text="Enter Hours:").grid()
        self.hours = Entry(self, textvariable=self.hour)
        self.hours.grid(row=1, column=2)

        Label(self, text="Enter Minutes:").grid()
        self.minutes = Entry(self, textvariable=self.minute)
        self.minutes.grid(row=2, column=2)

        Label(self, text="Enter Seconds:").grid()
        self.seconds = Entry(self, textvariable=self.second)
        self.seconds.grid(row=3, column=2)

        self.totalButton = Button(self, text="Total", pady=5, width=20, bd=3, command=self.computed)
        self.totalButton.grid(row=4, column=2)

        self.resetButton = Button(self, text="Reset", pady=5, width=20, bd=3, command=self.clearButton)
        self.resetButton.grid(row=5, column=2)

        self.exitButton = Button(self, text="Exit", pady=5, width=20, bd=3, command=self.exit)
        self.exitButton.grid(row=6, column=2)

        self.resultBox = Text(self, width=40, height=5)
        self.resultBox.grid(row=7, column=1, columnspan=3)

    def computed(self):
        try:
            if self.hour.get() < 0 or self.hour.get() > 24:
                message = "Invalid Hour."
                print("Invalid Hour.")
            elif self.minute.get() < 0 or self.minute.get() > 60:
                message = "Invalid Minute."
                print("Invalid Minute.")
            elif self.second.get() < 0 or self.second.get() > 60:
                message = "Invalid Second."
                print("Invalid Second.")
            else:
                timeElapsed = (self.hour.get() * 3600) + (self.minute.get() * 60) + self.second.get()
                message = "Enter Hour: {}\n".format(self.hour.get())
                message += "Enter Minute: {}\n".format(self.minute.get())
                message += "Enter Second: {}\n".format(self.second.get())
                message += "Time Elapsed In Seconds is: {:,}".format(timeElapsed)
                print("\nEnter Hour: {}".format(self.hour.get()))
                print("Enter Minute: {}".format(self.minute.get()))
                print("Enter Second: {}".format(self.second.get()))
                print("Time Elapsed In Seconds is: {:,}\n".format(timeElapsed))
                self.hour.set(0)
                self.minute.set(0)
                self.second.set(0)
        except:
            message = "Invalid Input!"
            print("Invalid Input!")
        self.resultBox.delete(0.0, END)
        self.resultBox.insert(0.0, message)

    def clearButton(self):
        self.hour.set(0)
        self.minute.set(0)
        self.second.set(0)
        self.resultBox.delete(0.0, END)

    @staticmethod
    def exit():
        exitMessage = tkinter.messagebox.askquestion("Close Program", "Do you want to quit?")
        if exitMessage == "yes":
            quit()


root = Tk()
root.title("Time Elapsed")
root.geometry("470x320+700+350")

mainFrame = Application(root)
mainFrame.grid()
root.mainloop()

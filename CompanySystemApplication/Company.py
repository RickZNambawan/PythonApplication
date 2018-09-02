# Company System Application
# Lets you add and remove employees
# You can also see the list of your employees

from tkinter import *


class Main(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.employeeList = []
        self.positionList = []
        self.salaryList = []
        self.employeeDict = {}
        self.name = StringVar()
        self.position = StringVar()
        self.pay = IntVar()
        self.creatWidgets()

    def creatWidgets(self):
        Label(self, text="Enter Employee Name: ").grid(row=0, column=0)
        self.employeeName = Entry(self, textvariable=self.name)
        self.employeeName.grid(row=0, column=1)

        Label(self, text="Enter What Position: ").grid(row=1, column=0)
        self.employeePosition = Entry(self, textvariable=self.position)
        self.employeePosition.grid(row=1, column=1)

        Label(self, text="Enter the Salary: ").grid(row=2, column=0)
        self.employeeSalary = Entry(self, textvariable=self.pay)
        self.employeeSalary.grid(row=2, column=1)

        self.addButton = Button(self, text="Add Employee", command=self.addEmployee).grid(row=3, column=0)
        self.removeButton = Button(self, text="Remove Employee", command=self.removeEmployee).grid(row=3, column=1)
        self.showEmpListButton = Button(self, text="Show Employees", command=self.showList).grid(row=3, column=2)

        self.resultBox = Text(self, width=42, height=10)
        self.resultBox.grid(row=4, column=0, columnspan=4)

    def addEmployee(self):
        if self.name.get() == "" and self.position.get() == "" and self.pay.get() == 0:
            message = "There's no input!"
        elif self.name.get() and self.position.get() == "" and self.pay.get() == 0:
            message = "Please enter his/her position to your company and the salary!"
        elif self.name.get() == "" and self.position.get() and self.pay.get() == 0:
            message = "Please type in the name and the salary!"
        elif self.name.get() == "" and self.position.get() == "" and self.pay.get():
            message = "Please type in the name and the position to your company!"
        elif self.name.get() and self.position.get() == "" and self.pay.get():
            message = "Please type in his/her position to your company!"
        elif self.name.get() == "" and self.position.get() and self.pay.get():
            message = "Please type in his/her name!"
        elif self.name.get() and self.position.get() and self.pay.get() == 0:
            message = "Please enter his/her salary!"
        elif self.name.get().title() in self.employeeList:
            message = "{} has already on the list!".format(self.name.get().title())
        else:
            self.employeeList.append(self.name.get().title())
            self.positionList.append(self.position.get().title())
            self.salaryList.append(self.pay.get())
            message = "{}, you've been successfully added as an Employee of the Company!".format(self.name.get().title())
            message += "\nPosition: {}".format(self.position.get().title())
            message += "\nSalary: {:,}".format(self.pay.get())
            print("{} was successfully added as an Employee of the Company!".format(self.name.get().title()))
            print("Position: {}".format(self.position.get().title()))
            print("Salary: {:,}\n".format(self.pay.get()))
            self.name.set("")
            self.position.set("")
            self.pay.set(0)

        self.resultBox.delete(0.0, END)
        self.resultBox.insert(0.0, message)

    def removeEmployee(self):
        if self.name.get() == "":
            message = "There's no input. \nPlease type in the name."
        elif self.name.get().title() not in self.employeeList:
            message = "There's no {} on the list of Employee! Sorry.".format(self.name.get())
        else:
            self.employeeList.remove(self.name.get().title())
            message = "You've successfully deleted {} as your employee!".format(self.name.get().title())
            print("You've successfully deleted {} as your employee!".format(self.name.get().title()))

        self.name.set("")
        self.position.set("")
        self.pay.set(0)
        self.resultBox.delete(0.0, END)
        self.resultBox.insert(0.0, message)

    def showList(self):
        if not self.employeeList:
            message = "There's no employee on the list yet. \nPlease add employee!"
            self.resultBox.delete(0.0, END)
            self.resultBox.insert(END, message)
        else:
            print("\nList of Employees: ")
            title = "List Of Employees:\n"
            self.resultBox.delete(0.0, END)
            self.resultBox.insert(END, title)

            count = 0
            for employee, position, salary in zip(self.employeeList, self.positionList, self.salaryList):
                count += 1
                self.employeeDict[employee, position] = salary
                message = "{}. Name: {}\nPosition: {}\nSalary: {:,}\n".format(count, employee, position, salary)
                print("{}. Name: {}\nPosition: {}\nSalary: {:,}".format(count, employee, position, salary))
                self.resultBox.insert(END, message)


root = Tk()
root.title("Company System Application")
root.geometry("400x320+700+350")
mainFrame = Main(root)
mainFrame.grid()
root.mainloop()

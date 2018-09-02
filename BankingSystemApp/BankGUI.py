# Bank System with Graphical User-Interface without Database
# Let's you add, delete, withdraw money, deposit money and see your balance.
# You can also see the lists of your customers.

from tkinter import *
import tkinter.messagebox


class Bank(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.name = StringVar()
        self.money = IntVar()
        self.customerList = []
        self.moneyList = []
        self.myDict = {}
        self.createWidgets()

    def createWidgets(self):
        Label(self, text="Enter Name: ").grid(row=0, column=0, padx=5, pady=7)
        self.enterName = Entry(self, textvariable=self.name, width=30)
        self.enterName.grid(row=0, column=1)

        Label(self, text="Enter Money:").grid(row=1, column=0, padx=5, pady=7)
        self.enterMoney = Entry(self, textvariable=self.money, width=30)
        self.enterMoney.grid(row=1, column=1)

        self.addButton = Button(self, text="Add", width=15, command=self.addCustomer).grid(row=2, column=0, columnspan=2)
        self.deleteButton = Button(self, text="Delete", width=15, command=self.deleteCustomer).grid(row=2, column=1, columnspan=2, padx=5, pady=2)

        self.balanceButton = Button(self, text="Balance", width=15, command=self.viewBalance).grid(row=3, column=0, padx=5, pady=7)
        self.withdrawButton = Button(self, text="Withdraw", width=15, command=self.withdrawMoney).grid(row=3, column=1, padx=5, pady=7)
        self.depositButton = Button(self, text="Deposit", width=15, command=self.depositMoney).grid(row=3, column=2, padx=5, pady=7)

        self.resultBox = Text(self, width=40, height="8")
        self.resultBox.grid(row=4, column=0, columnspan=3)
        self.customersButton = Button(self, text="View Customer List", width=15, command=self.viewCustomerList).grid(row=5, column=0, columnspan=3, padx=5, pady=7)

    def addCustomer(self):
        if self.name.get() in self.customerList:
            message = "{} is already on the list!".format(self.name.get())
            self.name.set("")
            self.money.set(0)
        elif self.name.get() == "" and self.money.get() == 0:
            message = "There's no input!"
        elif self.name.get() and self.money.get() == 0:
            message = "Zero is not allowed!"
        elif self.name.get() == "" and self.money.get():
            message = "Please type in your name!"
        else:
            addMessage = tkinter.messagebox.askquestion("Add Customer", "Do you want to add {}?".format(self.name.get()))
            if addMessage == "yes":
                self.customerList.append(self.name.get())
                self.moneyList.append(self.money.get())
                for name, money in zip(self.customerList, self.moneyList):
                    self.myDict[name] = money
                message = "{}, You've been successfully added in our Bank!\n".format(self.name.get())
                message += "You've added amount of {:,} as your starting money!".format(self.money.get())
                self.name.set("")
                self.money.set(0)
            else:
                message = "{} is NOT successfully added as your customer!".format(self.name.get())
        self.resultBox.delete(0.0, END)
        self.resultBox.insert(0.0, message)

    def deleteCustomer(self):
        if self.name.get() == "":
            message = "There's no input!"
        elif self.name.get() not in self.customerList:
            message = "There's no {} on the list!".format(self.name.get())
        else:
            addMessage = tkinter.messagebox.askquestion("Delete Customer", "Do you want to Delete {}?".format(self.name.get()))
            if addMessage == "yes":
                self.customerList.remove(self.name.get())
                message = "You've been successfully removed {} as your customer!".format(self.name.get())
            else:
                message = "{} is NOT successfully removed as your customer!".format(self.name.get())
        self.name.set("")
        self.resultBox.delete(0.0, END)
        self.resultBox.insert(0.0, message)

    def viewBalance(self):
        if self.name.get() == "":
            message = "Please type your name!"
        elif self.name.get() not in self.customerList:
            message = "There's no {} in the list.".format(self.name.get())
            self.name.set("")
        else:
            message = "Customer {}:\nYour remaining balance is: {:,}".format(self.name.get(), self.myDict[self.name.get()])
            self.name.set("")
            self.money.set(0)
        self.resultBox.delete(0.0, END)
        self.resultBox.insert(0.0, message)

    def withdrawMoney(self):
        if self.name.get() == "":
            message = "Please type your name!"
        elif self.name.get() not in self.customerList:
            message = "There's no {} in the list.".format(self.name.get())
            self.name.set("")
        elif self.name.get() and self.money.get() == 0:
            message = "Zero is not allowed!"
        elif self.money.get() > self.myDict[self.name.get()]:
            message = "Invalid Input! Your money is higher than your balance!"
        else:
            newMoney = self.myDict[self.name.get()]
            newMoney -= self.money.get()
            self.myDict[self.name.get()] = newMoney
            message = "{}, You've been withdraw amount of {:,}\n".format(self.name.get(), self.money.get())
            message += "Your currently balance is: {:,}".format(newMoney)
            self.name.set("")
            self.money.set(0)
        self.resultBox.delete(0.0, END)
        self.resultBox.insert(0.0, message)

    def depositMoney(self):
        if self.name.get() == "":
            message = "Please type your name!"
        elif self.name.get() not in self.customerList:
            message = "There's no {} in the list.".format(self.name.get())
            self.name.set("")
        elif self.name.get() and self.money.get() == 0:
            message = "Zero is not allowed!"
        else:
            newMoney = self.myDict[self.name.get()]
            newMoney += self.money.get()
            self.myDict[self.name.get()] = newMoney
            message = "{}, You've been deposit amount of {:,}\n".format(self.name.get(), self.money.get())
            message += "Your currently balance is: {:,}".format(newMoney)
            self.name.set("")
            self.money.set(0)
        self.resultBox.delete(0.0, END)
        self.resultBox.insert(0.0, message)

    def viewCustomerList(self):
        if not self.customerList:
            message = "There's no employee on the list yet.\nPlease add employee!"
            self.resultBox.delete(0.0, END)
            self.resultBox.insert(END, message)
        else:
            print("\nList of Customers: ")
            title = "List Of Customers:\n"
            self.resultBox.delete(0.0, END)
            self.resultBox.insert(END, title)
            count = 0
            message = ""
            for name in self.customerList:
                count += 1
                message += "{}. Name: {}\nBalance: {:,}\n".format(count, name, self.myDict[name])
                print("{}. Name: {}\nBalance: {:,}".format(count, name, self.myDict[name]))
            self.resultBox.insert(END, message)


root = Tk()
root.title("Frederick's Banking System")
root.geometry("440x315+700+350")
main = Bank(root)
main.grid()
root.mainloop()


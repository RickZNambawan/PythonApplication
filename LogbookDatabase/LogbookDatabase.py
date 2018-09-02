# Logbook Application Database
# Lets you add information and store it on your Database

from tkinter import *
import sqlite3

conn = sqlite3.connect("Logbook.db")
c = conn.cursor()

# c.execute("""DROP TABLE IF EXISTS Logbook""")
# c.execute("""CREATE TABLE Logbook(name TEXT, age INTEGER, address TEXT, status TEXT)""")


class LogBook(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name, self.age, self.address = StringVar(), IntVar(), StringVar()
        self.createWidgets()
        self.showList()

    def createWidgets(self):
        Label(self, text="Name: ").grid(row=1, column=0)
        self.nameEntry = Entry(self, width=50, textvar=self.name)
        self.nameEntry.grid(row=1, column=1)

        Label(self, text="Age: ").grid(row=2, column=0)
        self.ageEntry = Entry(self, width=50, textvar=self.age)
        self.ageEntry.grid(row=2, column=1)

        self.addButton = Button(self, text="Add Customer", width=26, height=2, border=5, bg="light blue", command=self.addCustomer)
        self.addButton.grid(row=2, column=3)

        self.deleteButton = Button(self, text="Delete Customer", width=26, height=2, border=5, bg="light blue", command=self.deleteCustomer)
        self.deleteButton.grid(row=2, column=4)

        Label(self, text="Address: ").grid(row=3, column=0)
        self.addressEntry = Entry(self, width=50, textvar=self.address)
        self.addressEntry.grid(row=3, column=1)

        Label(self, text="\t\tName").grid(row=4, column=0, pady=10)
        Label(self, text="Age").grid(row=4, column=1)
        Label(self, text="Address").grid(row=4, column=3)
        Label(self, text="Status").grid(row=4, column=8)

        self.resultBox = Text(self, width=235, height=53)
        self.resultBox.grid(row=5, column=0, columnspan=10, padx=20, pady=5)

    def addCustomer(self):
        c.execute("""INSERT INTO Logbook (name, age, address) VALUES (?, ?, ?)""", (self.name.get(), self.age.get(), self.address.get()))
        conn.commit()

        while True:
            self.count += 1
            text = "{}. {} \t\t\t\t\t\t       ".format(self.count, self.name.get())
            text += "{} \t\t\t\t\t\t\t\t   {}\n".format(self.age.get(), self.address.get())
            self.resultBox.insert(END, text)
            self.name.set(""), self.age.set(0), self.address.set("")
            break

    def deleteCustomer(self):
        c.execute("DELETE FROM Logbook WHERE name=?", (self.name.get(),))
        conn.commit()
        self.resultBox.delete(0.0, END)
        self.name.set("")
        self.showList()

    def showList(self):
        table = c.execute("""SELECT name, age, address FROM Logbook""")

        self.count = 0
        for name, age, address in table:
            self.count += 1
            text = "{}. {} \t\t\t\t\t\t       ".format(self.count, name)
            text += "{} \t\t\t\t\t\t\t\t   {}\n".format(age, address)
            self.resultBox.insert(END, text)


root = Tk()
root.title("Database")
root.geometry("1910x1000+0+0")
main = LogBook(root)
main.grid()
root.mainloop()

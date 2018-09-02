# Library Application System (Scratch)
# Not yet done
# Add button, Refreshlist, List of books Button and Exit button are done

from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("library.db")
c = conn.cursor()

##c.execute("DROP TABLE IF EXISTS LIBRARY")
##c.execute("CREATE TABLE LIBRARY (name TEXT, author TEXT, iso INTEGER, genre TEXT, position TEXT)")


class MainApplication(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("900x940+535+60")
        self.title("Library Application")
        self.container = Frame(self)
        self.container.grid()

class AddingBooks(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.name = StringVar()
        self.author = StringVar()
        self.iso = IntVar()
        self.genre = StringVar()
        self.position = StringVar()
        self.createWidgets()
        self.showDatabase()

    def createWidgets(self):
        Label(self, text="Name of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=1, column=1)
        self.nameEntry = Entry(self, width=60, textvar=self.name)
        self.nameEntry.grid(row=1, column=2)

        Label(self, text="Author of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=2, column=1)
        self.authorEntry = Entry(self, width=60, textvar=self.author)
        self.authorEntry.grid(row=2, column=2)

        Label(self, text="ISO Number:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=3, column=1)
        self.isoNumber = Entry(self, width=60, textvar=self.iso)
        self.isoNumber.grid(row=3, column=2)

        Label(self, text="Genre of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=4, column=1)
        self.genreEntry = Entry(self, width=60, textvar=self.genre)
        self.genreEntry.grid(row=4, column=2)

        Label(self, text="Position of the Book:", padx=70, width=12, height=3, font=("bold", 15)).grid(row=5, column=1)
        self.positionEntry = Entry(self, width=60, textvar=self.position)
        self.positionEntry.grid(row=5, column=2)

        self.addButton = Button(self, text="Add Book", width=20, height=3, padx=50, command=self.addBooks).grid(row=6, column=1)
        self.removeButton = Button(self, text="Remove Book", width=20, height=3, padx=50).grid(row=6, column=2)
        self.updateButton = Button(self, text="Update Book", width=20, height=3, padx=50).grid(row=6, column=3)
        self.refreshButton = Button(self, text="Refresh List", width=20, height=3, padx=50, command=self.showDatabase).grid(row=7, column=1)
        self.showButton = Button(self, text="Show List of Books", width=20, height=3, padx=50, command=self.showBooksWindow).grid(row=7, column=2)
        self.exitButton = Button(self, text="EXIT", width=20, height=3, padx=50, command=self.exitProgram).grid(row=7, column=3)

        self.textBox = Text(self, width=100, height=23, padx=15)
        self.textBox.grid(row=8, column=1, columnspan=4)

    def addBooks(self):
        f = c.execute("SELECT name FROM LIBRARY")
        if self.name.get() in f:
            print("It's in the database!")
        else:
            print("gago")
            c.execute("INSERT INTO LIBRARY (name, author, iso, genre, position) VALUES (?, ?, ?, ?, ?)",
                      (self.name.get(), self.author.get(), self.iso.get(), self.genre.get(), self.position.get()))
            conn.commit()

    def showDatabase(self):
        self.textBox.delete(0.0, END)
        self.counter = 0
        c.execute("SELECT name, author, iso, genre, position FROM LIBRARY")
        title = "List of Available Books: \n\n"
        self.textBox.insert(END, title)
        for name, author, iso, genre, position in c:
            self.counter += 1
            text = "{}.) Name of the Book: {} \nAuthor of the Book: {} \nISO Number: {} " \
                   "\nGenre of the Book: {} \nPosition of the Book: {}\n\n".format(self.counter, name, author, iso, genre, position)
            self.textBox.insert(END, text)

    def showBooksWindow(self):
        db = ShowingListOfBooks()
        db.geometry("515x940+5+60")
        db.mainloop()

    def exitProgram(self):
        exitMessage = tkinter.messagebox.askquestion("Close the Program", "Do you want to Exit the Program?")
        if exitMessage == "yes":
            exit()

class ShowingListOfBooks(Tk):
    def __init__(self, *args, **kwargs, ):
        Tk.__init__(self, *args, **kwargs)
        Label(self, text="LIST OF AVAILABLE BOOKS", font=("bold", 15)).pack(pady=40)
        self.textBox = Text(self, width=54, height=40, padx=2)
        self.textBox.pack(padx=10, pady=40)
        self.refreshButton = Button(self, text="Refresh List", command=lambda: AddingBooks.showDatabase(self)).pack()
        AddingBooks.showDatabase(self)


root = MainApplication()
mainApp = AddingBooks(root)
mainApp.grid()
root.mainloop()

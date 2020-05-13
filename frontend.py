from tkinter import *
from backend import Database

database = Database("books.db")

class Window:

    def __init__(self, window):
        self.window = window
        self.window.wm_title("BookStore 2.0")

        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        """
        ^^^ LABELS ^^^
        """

        self.title_text=StringVar()
        self.e1=Entry(window, width=17, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text=StringVar()
        self.e2=Entry(window, width=17, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text= StringVar()
        self.e3=Entry(window, width=17, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(window, width=17, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        """
        ^^^ ENTRY ^^^
        """
        self.list1 = Listbox(window, height=10, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.sb1=Scrollbar(window)
        self.sb1.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        """
        ^^^ LISTBOX & SCROLL ^^^
        """


        b1 = Button(window, text="View all", width=13, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Search entry", width=13, command=self.search_command) 
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add entry", width=13, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update", width=13, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete", width=13, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=13, command=self.window.destroy)
        b6.grid(row=7, column=3)

        """
        ^^^ BUTTONS ^^^
        """

    def get_selected_row(self, event):
        try:
            index = self.list1.curselection()[0]
            self.selected_row = self.list1.get(index)
        except IndexError:
            pass
        else:
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_row[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_row[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_row[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_row[4])



    def view_command(self):
        self.list1.delete(0, END)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)

        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)


    def update_command(self):
        database.update(self.selected_row[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())

        self.list1.delete(0, END)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)

        for row in database.view():
            self.list1.insert(END, row)

    def delete_command(self):
        database.delete(self.selected_row[0])
        
        self.list1.delete(0, END)
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)

        for row in database.view():
            self.list1.insert(END, row)


window = Tk()
Window(window)
window.mainloop()
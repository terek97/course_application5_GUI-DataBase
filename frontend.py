from tkinter import *
import backend


def get_selected_row(event):
    global selected_row 
    try:
        index = list1.curselection()[0]
        selected_row = list1.get(index)
    except IndexError:
        pass
    else:
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
        e4.delete(0, END)
        e4.insert(END, selected_row[4])



def view_command():
    list1.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def update_command():
    backend.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def delete_command():
    backend.delete(selected_row[0])


window = Tk()
window.wm_title("BookStore 1.0")

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

title_text=StringVar()
e1=Entry(window, width=17, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2=Entry(window, width=17, textvariable=author_text)
e2.grid(row=0, column=3)

year_text= StringVar()
e3=Entry(window, width=17, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4=Entry(window, width=17, textvariable=isbn_text)
e4.grid(row=1, column=3)

"""
^^^ ENTRY ^^^
"""
list1 = Listbox(window, height=10, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

"""
^^^ LISTBOX & SCROLL ^^^
"""


b1 = Button(window, text="View all", width=13, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=13, command=search_command) 
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=13, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=13, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=13, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=13, command=window.destroy)
b6.grid(row=7, column=3)

"""
^^^ BUTTONS ^^^
"""

window.mainloop()
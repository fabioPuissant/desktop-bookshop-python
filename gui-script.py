from tkinter import *
import backend

window = Tk()

def view_command():
    for book in backend.view():
        list1.insert(END, book) # END means that every ne entry is placed at the END of the list!


# The labels
label_1 = Label(window, text="Title")
label_1.grid(row=0, column=0)

label_2 = Label(window, text="Author")
label_2.grid(row=0, column=2)

label_3 = Label(window, text="Year")
label_3.grid(row=1, column=0)

label_4 = Label(window, text="ISBN")
label_4.grid(row=1, column=2)

title_text = StringVar()
entry_title = Entry(window, textvariable=title_text)
entry_title.grid(row=0, column=1)

author_text = StringVar()
entry_author = Entry(window, textvariable=author_text)
entry_author.grid(row=0, column=3)

year_text = StringVar()
entry_year = Entry(window, textvariable=year_text)
entry_year.grid(row=1, column=1)

isbn_text = StringVar()
entry_isbn = Entry(window, textvariable=isbn_text)
entry_isbn.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

scrollbar= Scrollbar(window)
scrollbar.grid(row=2, column=2)

list1.configure(yscrollcommand= scrollbar.set)
scrollbar.config(command=list1.yview)

button_view_all = Button(window, text="View all", width=12, command=view_command)
button_view_all.grid(row= 2, column=3)

button_search_entry = Button(window, text="Search entry", width=12)
button_search_entry.grid(row=3, column=3)

button_add_entry = Button(window, text="Add entry", width=12)
button_add_entry.grid(row= 4, column=3)

button_Update = Button(window, text="Update", width=12)
button_Update.grid(row= 5, column=3)

button_delete = Button(window, text="Delete", width=12)
button_delete.grid(row= 6, column=3)

button_close = Button(window, text="Close", width=12)
button_close.grid(row= 7, column=3)

window.mainloop()

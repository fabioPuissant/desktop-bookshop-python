from tkinter import *
from tkinter import Listbox
from bookshop.backend import DataBase


db_name = "books.db"
database = DataBase(db_name)
window = Tk()
window.title("Python's Book-Shop ")


def view_command():
    # Ensure that the listbox is empty before adding the fresh values of the database!
    list1.delete(0, END)

    # Now we populate the display list with the freshly fetched items of the database!
    for book in database.get_all():
        list1.insert(END, book)  # END means that every ne entry is placed at the END of the list!


def search_command():
    # Ensure that the listbox is empty before adding the fresh values of the database!
    list1.delete(0, END)
    for found in database.search(title_text.get(),
                                author_text.get(),
                                year_text.get(),
                                isbn_text.get()
                                ):
        list1.insert(END, found)


def add_book_command():
    database.insert(title_text.get(),
                   author_text.get(),
                   year_text.get(),
                   isbn_text.get())
    list1.delete(0, END)
    view_command()
    clear_entries()


def delete_book_command():
    if selected_list_item is not None:
        database.delete(selected_list_item[0])
        clear_entries()
        view_command()


def update_book_command():
    if selected_list_item is not None:
        database.update(
            selected_list_item[0],
            entry_title.get(),
            entry_author.get(),
            entry_year.get(),
            entry_isbn.get(),
        )
        clear_entries()
        view_command()


def clear_entries():
    entry_title.delete(0, END)
    entry_author.delete(0, END)
    entry_year.delete(0, END)
    entry_isbn.delete(0, END)
    selected_list_item = None


def get_selected_row(event):
    global selected_list_item
    if list1.curselection():
        index = int(list1.curselection()[0])
        selected_list_item = list1.get(index)

        # Display which one is selected!
        entry_title.delete(0,END)
        entry_title.insert(END, selected_list_item[1])

        entry_author.delete(0, END)
        entry_author.insert(END, selected_list_item[2])

        entry_year.delete(0, END)
        entry_year.insert(END, selected_list_item[3])

        entry_isbn.delete(0, END)
        entry_isbn.insert(END, selected_list_item[4])


def close_window_command():
    window.destroy()


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

list1: Listbox = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
list1.bind('<<ListboxSelect>>', get_selected_row)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2)

list1.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=list1.yview)

button_view_all = Button(window, text="View all", width=12, command=view_command)
button_view_all.grid(row=2, column=3)

button_search_entry = Button(window, text="Search entry", width=12, command=search_command)
button_search_entry.grid(row=3, column=3)

button_add_entry = Button(window, text="Add entry", width=12, command=add_book_command)
button_add_entry.grid(row=4, column=3)

button_Update = Button(window, text="Update", width=12, command = update_book_command)
button_Update.grid(row=5, column=3)

button_delete = Button(window, text="Delete", width=12, command= delete_book_command)
button_delete.grid(row=6, column=3)

button_close = Button(window, text="Close", width=12, command = close_window_command)
button_close.grid(row=7, column=3)

window.mainloop()

from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_text = task_listbox.get(selected_task)
        if task_text in tasks:
            tasks.remove(task_text)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (task_text,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        tasks.clear()
        the_cursor.execute('delete from tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    guiWindow.destroy()

def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List - Farhana")
    guiWindow.geometry("665x400+550+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#FFFF00") 
    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    functions_frame = Frame(guiWindow, bg="#FFFF00")  
    functions_frame.pack(side="top", expand=True, fill="both")

    task_label = Label(functions_frame, text="Enter the Tasks:",
                       font=("arial", "14", "bold"),
                       background="#FFFF00",  
                       foreground="#FF6103")
    task_label.place(x=20, y=30)

    task_field = Entry(functions_frame,
                       font=("Arial", "14"),
                       width=42,
                       foreground="black",
                       background="white")
    task_field.place(x=180, y=30)

    add_button = Button(functions_frame, text="Add", width=15,
                        bg='#FF0000', font=("arial", "14", "bold"), 
                        command=add_task)
    
    del_button = Button(functions_frame, text="Remove", width=15,
                        bg='#FF0000', font=("arial", "14", "bold"),  
                        command=delete_task)
    
    del_all_button = Button(functions_frame, text="Delete All", width=15,
                            bg='#FF0000', font=("arial", "14", "bold"), 
                            command=delete_all_tasks)
    
    exit_button = Button(functions_frame, text="Exit / Close", width=52,
                         bg='#FF0000', font=("arial", "14", "bold"), 
                         command=close)
    
    add_button.place(x=18, y=80)
    del_button.place(x=240, y=80)
    del_all_button.place(x=460, y=80)
    exit_button.place(x=17, y=330)

    task_listbox = Listbox(functions_frame, width=70, height=9,
                           font="bold", selectmode='SINGLE',
                           background="white", foreground="black",
                           selectbackground="#FF8C00", selectforeground="black")
    task_listbox.place(x=17, y=140)

    retrieve_database()
    list_update()
    guiWindow.mainloop()

    the_connection.commit()
    the_cursor.close()

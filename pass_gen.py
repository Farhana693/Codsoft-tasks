import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def accept_password():
    result_label.config(text=f"Password accepted: {password_var.get()}")

def reject_password():
    result_label.config(text="Password rejected. Please generate a new one.")

def delete_password():
    password_var.set("")
    result_label.config(text="Password deleted.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x300")
root.configure(bg="brown")

large_font = ("Arial", 16)

name_label = tk.Label(root, text="Enter your name:", bg="brown", fg="white", font=large_font, anchor="w")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root, font=large_font)
name_entry.grid(row=0, column=1, padx=10, pady=5)

length_label = tk.Label(root, text="Enter password length:", bg="brown", fg="white", font=large_font, anchor="w")
length_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
length_entry = tk.Entry(root, font=large_font)
length_entry.grid(row=1, column=1, padx=10, pady=5)

password_var = tk.StringVar()

generate_button = tk.Button(root, text="Generate", command=generate_password, font=large_font)
generate_button.grid(row=2, column=1, padx=10, pady=20, sticky="w")

accept_button = tk.Button(root, text="Accept", command=accept_password, font=large_font)
accept_button.grid(row=2, column=2, padx=10, pady=20)

reject_button = tk.Button(root, text="Reject", command=reject_password, font=large_font)
reject_button.grid(row=3, column=1, padx=10, pady=20, sticky="w")

delete_button = tk.Button(root, text="Delete", command=delete_password, font=large_font)
delete_button.grid(row=3, column=2, padx=10, pady=20)

password_label = tk.Label(root, textvariable=password_var, bg="brown", fg="white", font=large_font)
password_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

result_label = tk.Label(root, text="", bg="brown", fg="white", font=large_font)
result_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()


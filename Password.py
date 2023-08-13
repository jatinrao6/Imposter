import tkinter as tk
import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_and_display_password():
    try:
        name = entry_name.get()
        password_length = int(entry_length.get())
        if password_length <= 0:
            raise ValueError("Password length must be a positive integer.")

        generated_password = generate_password(password_length)
        password_display_label.config(text=f"Hello {name}, your generated password is:")
        generated_password_label.config(text=generated_password)
    except ValueError as e:
        password_display_label.config(text=str(e))
        generated_password_label.config(text="")


def accept_password():
    accepted_password = generated_password_label.cget("text")
    print(f"Accepted Password: {accepted_password}")


def reset_password():
    entry_name.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    password_display_label.config(text="")
    generated_password_label.config(text="")


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and pack the widgets
label_name = tk.Label(root, text="Enter your name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_length = tk.Label(root, text="Enter the desired password length:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

generate_button = tk.Button(root, text="Generate Password",  command=generate_and_display_password, )
generate_button.pack()

password_display_label = tk.Label(root, text="")
password_display_label.pack()

generated_password_label = tk.Label(root, text="", font=("Courier", 12))
generated_password_label.pack()

accept_button = tk.Button(root, text="Accept Password", command=accept_password)
accept_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_password)
reset_button.pack()

# Start the GUI main loop
root.mainloop()

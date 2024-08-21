import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # For copying to clipboard

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x350")
        self.root.configure(bg='#f0f0f0')
        
        self.label_title = tk.Label(root, text="Random Password Generator", font=("Helvetica", 18), bg='#f0f0f0', fg='#333')
        self.label_title.pack(pady=10)
        
        self.label_length = tk.Label(root, text="Enter password length:", font=("Helvetica", 12), bg='#f0f0f0', fg='#333')
        self.label_length.pack()
        
        self.entry_length = tk.Entry(root, width=30, font=("Helvetica", 12))
        self.entry_length.pack(pady=5)
        self.entry_length.focus_set()  # Automatically focus on entry field
        self.entry_length.bind("<Return>", lambda event: self.generate_password())  # Bind Enter key to generate_password
        
        self.generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12), bg='#4caf50', fg='white', command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        self.password_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg='#f0f0f0', fg='#333')
        self.password_label.pack(pady=10)
        
        self.copy_button = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 12), bg='#007bff', fg='white', command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)
        
    def generate_password(self):
        length_str = self.entry_length.get()
        
        try:
            length = int(length_str)
            if length <= 0:
                messagebox.showerror("Error", "Length should be greater than zero.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        
        self.password_label.config(text=f"Generated Password:\n{password}")
        self.generated_password = password  # Store generated password for copying
    
    def copy_to_clipboard(self):
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.generated_password)
            self.root.update()  # to trigger clipboard update
            messagebox.showinfo("Success", "Password copied to clipboard!")
        except AttributeError:
            messagebox.showerror("Error", "No password generated yet. Generate a password first.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

main()

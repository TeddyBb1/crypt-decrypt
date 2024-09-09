import tkinter as tk
from tkinter import ttk, messagebox

# Function to encrypt text using Caesar cipher
def caesar_encrypt(text, key):
    result = ""
    try:
        key = int(key)
        for char in text:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                result += chr((ord(char) - shift + key) % 26 + shift)
            else:
                result += char
        return result
    except ValueError:
        messagebox.showerror("Key Error", "For Caesar Cipher, the key must be an integer.")
        return ""

# Function to decrypt text using Caesar cipher
def caesar_decrypt(text, key):
    return caesar_encrypt(text, -int(key))

# Function to encrypt text using Vigenère cipher
def vigenere_encrypt(text, key):
    key = [ord(char.lower()) - 97 for char in key]
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key[i % len(key)]) % 26 + shift)
        else:
            result += char
    return result

# Function to decrypt text using Vigenère cipher
def vigenere_decrypt(text, key):
    key = [-(ord(char.lower()) - 97) for char in key]
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key[i % len(key)]) % 26 + shift)
        else:
            result += char
    return result

# Function to handle encryption
def encrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    key = key_input.get().strip()

    if not text or not key:
        messagebox.showwarning("Input Error", "Please enter both text and key.")
        return

    method = encryption_method.get()
    try:
        if method == "Caesar Cipher":
            encrypted = caesar_encrypt(text, key)
        elif method == "Vigenère Cipher":
            encrypted = vigenere_encrypt(text, key)
        else:
            messagebox.showwarning("Method Error", "Select a valid encryption method.")
            return
        encrypted_text.set(encrypted)
    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))

# Function to handle decryption
def decrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    key = key_input.get().strip()

    if not text or not key:
        messagebox.showwarning("Input Error", "Please enter both text and key.")
        return

    method = encryption_method.get()
    try:
        if method == "Caesar Cipher":
            decrypted = caesar_decrypt(text, key)
        elif method == "Vigenère Cipher":
            decrypted = vigenere_decrypt(text, key)
        else:
            messagebox.showwarning("Method Error", "Select a valid decryption method.")
            return
        encrypted_text.set(decrypted)
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))

# Set up the main window
root = tk.Tk()
root.title("Text Encryptor/Decryptor")
root.geometry("600x400")
root.resizable(False, False)

# Add a style
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Title label
title_label = ttk.Label(root, text="Text Encryptor/Decryptor", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Text input section
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

input_label = ttk.Label(input_frame, text="Enter Text:", font=("Helvetica", 12))
input_label.grid(row=0, column=0, sticky="w")

input_text = tk.Text(input_frame, height=6, width=50)
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Key input section
key_label = ttk.Label(input_frame, text="Enter Key:", font=("Helvetica", 12))
key_label.grid(row=2, column=0, sticky="w", pady=5)

key_input = ttk.Entry(input_frame, width=30)
key_input.grid(row=2, column=1, pady=5)

# Dropdown for encryption methods
method_label = ttk.Label(input_frame, text="Select Method:", font=("Helvetica", 12))
method_label.grid(row=3, column=0, sticky="w", pady=5)

encryption_method = ttk.Combobox(input_frame, values=["Caesar Cipher", "Vigenère Cipher"], state="readonly")
encryption_method.set("Caesar Cipher")
encryption_method.grid(row=3, column=1, pady=5)

# Output section
output_label = ttk.Label(input_frame, text="Output:", font=("Helvetica", 12))
output_label.grid(row=4, column=0, sticky="w", pady=5)

encrypted_text = tk.StringVar()
output_entry = ttk.Entry(input_frame, textvariable=encrypted_text, width=50)
output_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Buttons for Encrypt and Decrypt
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

encrypt_button = ttk.Button(button_frame, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = ttk.Button(button_frame, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=0, column=1, padx=10)

# Run the main loop
root.mainloop()

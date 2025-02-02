import tkinter as tk
from speech import speak, listen


def search():
    query = search_entry.get()
    result_label.config(text=f"Search for: {query}")
    speak(f"You searched for: {query}")


def start_gui():
    global root, search_entry, result_label

    root = tk.Tk()
    root.title("Math Tutor")
    root.geometry("800x500")
    root.config(bg='gray')

    label = tk.Label(root, text="Math Tutor", font=("Arial", 26), bg='gray')
    label.pack(pady=20)

    result_label = tk.Label(root, text="Enter Your Math Question", font=("Arial", 14), bg='gray')
    result_label.pack(pady=20)

    search_entry = tk.Entry(root, font=("Arial", 14), width=50)
    search_entry.pack(pady=10)

    search_button = tk.Button(root, text="Search", command=search, font=("Arial", 14))
    search_button.pack(pady=10)

    speech_button = tk.Button(root, text="Speech", command=lambda: listen(search_entry, result_label),
                              font=("Arial", 14))
    speech_button.pack(pady=10)

    root.mainloop()

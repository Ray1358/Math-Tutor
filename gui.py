import tkinter as tk
from tkinter import ttk
from speech import speak
from ai_explainer import explain_math

# Available topics from the syllabus
SYLLABUS_TOPICS = [
    "Real Numbers", "Order of Operations", "Absolute Value", "Exponents", "Linear Equations",
    "Graphing Lines", "Inequalities", "Scientific Notation", "Polynomials", "Factoring",
    "Coordinate System", "Slopes", "Intercepts", "Simplifying Expressions"
]

def search():
    query = topic_var.get().strip()
    if not query or query == "Select a topic":
        result_label.config(text="Please select a valid math topic")
        speak("Please select a valid math topic")
        return

    explanation = explain_math(query)  # Get AI-powered explanation
    result_textbox.config(state=tk.NORMAL)  # Enable editing
    result_textbox.delete("1.0", tk.END)  # Clear previous text
    result_textbox.insert(tk.END, explanation)  # Display explanation
    result_textbox.config(state=tk.DISABLED)  # Disable editing

def start_gui():
    global root, topic_var, result_label, result_textbox

    root = tk.Tk()
    root.title("Math Tutor AI")
    root.geometry("850x600")
    root.configure(bg='#2C2F33')  # Dark theme

    # Modern Styling
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 16), padding=5, background="#7289DA", foreground="black")  # Button text black
    style.configure("TLabel", font=("Arial", 16), background='#2C2F33', foreground="black")

    label = ttk.Label(root, text="Math Tutor AI", font=("Arial", 26, "bold"), background='#23272A', foreground='black')
    label.pack(pady=20)

    # Instruction label ABOVE the dropdown menu
    instruction_label = ttk.Label(root, text="Choose a topic to learn about:", font=("Arial", 14), background='#2C2F33', foreground="black")
    instruction_label.pack(pady=(10, 0))

    frame = ttk.Frame(root, padding=20)
    frame.pack(pady=10)

    # Dropdown menu for selecting a topic
    topic_var = tk.StringVar(root)
    topic_var.set("Select a topic")

    topic_dropdown = ttk.Combobox(frame, textvariable=topic_var, values=SYLLABUS_TOPICS, font=("Arial", 14), state="readonly")
    topic_dropdown.grid(row=0, column=0, padx=10)

    search_button = ttk.Button(frame, text="Explain", command=search, style="TButton")
    search_button.grid(row=0, column=1, padx=10)

    # Textbox to display AI explanations
    result_textbox = tk.Text(root, font=("Arial", 14), height=10, width=80, wrap="word", state=tk.DISABLED, bg='#F0F0F0')
    result_textbox.pack(pady=10)

    root.mainloop()
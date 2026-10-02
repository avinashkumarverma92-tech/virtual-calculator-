#this is our santific calculater
import tkinter as tk
import math


# ---------------- FUNCTIONS ---------------- #

def button_click(value):
    current = display_var.get()

    if value == "=":
        try:
            expression = current.replace("×", "*").replace("÷", "/")

            # Safe mathematical environment
            result = eval(expression, {
                "__builtins__": None,
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "sqrt": math.sqrt,
                "log": math.log10,
                "ln": math.log,
                "pi": math.pi,
                "e": math.e
            })

            display_var.set(str(round(result, 10)))

        except Exception:
            display_var.set("Error")

    elif value == "C":
        display_var.set("")

    elif value == "⌫":
        display_var.set(current[:-1])

    elif value == "x²":
        display_var.set(f"({current})**2")

    elif value == "√":
        display_var.set(current + "sqrt(")

    elif value == "sin":
        display_var.set(current + "sin(")

    elif value == "cos":
        display_var.set(current + "cos(")

    elif value == "tan":
        display_var.set(current + "tan(")

    elif value == "log":
        display_var.set(current + "log(")

    elif value == "ln":
        display_var.set(current + "ln(")

    elif value == "π":
        display_var.set(current + "pi")

    else:
        display_var.set(current + value)


# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("500x650")
root.resizable(False, False)


# ---------------- DISPLAY ---------------- #

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 24),
    justify="right",
    bd=10
)

display.grid(
    row=0,
    column=0,
    columnspan=5,
    padx=10,
    pady=20,
    sticky="nsew",
    ipady=15
)


# ---------------- BUTTONS ---------------- #

buttons = [
    ["sin", "cos", "tan", "√", "C"],
    ["log", "ln", "π", "(", ")"],
    ["7", "8", "9", "÷", "⌫"],
    ["4", "5", "6", "×", "x²"],
    ["1", "2", "3", "-", "+"],
    ["0", ".", "%", "**", "="]
]


# ---------------- CREATE BUTTONS ---------------- #

for i, row in enumerate(buttons):

    for j, value in enumerate(row):

        button = tk.Button(
            root,
            text=value,
            font=("Arial", 16),
            height=2,
            width=6,
            command=lambda x=value: button_click(x)
        )

        button.grid(
            row=i + 1,
            column=j,
            padx=5,
            pady=5,
            sticky="nsew"
        )


# Make grid responsive
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

for j in range(5):
    root.grid_columnconfigure(j, weight=1)


# ---------------- RUN ---------------- #

root.mainloop()
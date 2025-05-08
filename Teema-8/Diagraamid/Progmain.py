from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

canvas = None


# window - root / akna kuvatamine
# ---------------------------------------------------
window = Tk()

# ---------------------------------------------------
# config
# --------------------------------------------------

window.title("Kvadraatilise võrrandi lahendus")
window.configure(bg="#2c3e50")
window.resizable(width=False, height=False)
window.iconbitmap("icon1234.ico")
window.attributes("-fullscreen", True)

# --------------------------------------------------
# elemendid
# --------------------------------------------------

pealkiri = Label(window, text="Kvadraatilise võrrandi lahendus", bg="#2c3e50", font=("Arial", 22), fg="white")

inputA = Entry(window, bg="#ecf0f1", font=("Arial", 18), fg="black")
inputB = Entry(window, bg="#ecf0f1", font=("Arial", 18), fg="black")
inputC = Entry(window, bg="#ecf0f1", font=("Arial", 18), fg="black")

inputA.insert(0, "")
inputB.insert(0, "")
inputC.insert(0, "")

TEXT1 = Label(window, text="X² +", bg="#2c3e50", font=("Arial", 12), fg="WHITE")
TEXT2 = Label(window, text="X +", bg="#2c3e50", font=("Arial", 12), fg="WHITE")
TEXT3 = Label(window, text="= 0", bg="#2c3e50", font=("Arial", 12), fg="WHITE")

answer = "Lahendus kuvatakse siin."
solve = Label(window, text=answer, bg="#2c3e50", font=("Arial", 16), fg="white")

# --------------------------------------------------
# def
# --------------------------------------------------

def on_focus_in(event, entry):
    entry.config(bg="#bdc3c7")

def on_focus_out(event, entry):
    entry.config(bg="#ecf0f1")

def validate_input():
    try:
        a = float(inputA.get())
        b = float(inputB.get())
        c = float(inputC.get())
        return True
    except ValueError:
        return False

def solve_quadratic():
    if not validate_input():
        if not inputA.get():
            inputA.config(bg="red")
        if not inputB.get():
            inputB.config(bg="red")
        if not inputC.get():
            inputC.config(bg="red")
        
        solve.config(text="Palun sisetage korrekte andmed.")
        return

    inputA.config(bg="#ecf0f1")
    inputB.config(bg="#ecf0f1")
    inputC.config(bg="#ecf0f1")

    try:
        a = float(inputA.get())
        b = float(inputB.get())
        c = float(inputC.get())

        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            x1 = (-b + np.sqrt(discriminant)) / (2*a)
            x2 = (-b - np.sqrt(discriminant)) / (2*a)
            result = (
                f"D = {discriminant:.2f}\n"
                f"Juured: x1 = {x1:.2f}, x2 = {x2:.2f}"
            )
        else:
            result = f"D = {discriminant:.2f}\nPole juured."
    except ValueError:
        result = "Vale andmed."

    solve.config(text=result)



def plot_graph():
    global canvas

    if not validate_input():
        if not inputA.get():
            inputA.config(bg="red")
        if not inputB.get():
            inputB.config(bg="red")
        if not inputC.get():
            inputC.config(bg="red")

        solve.config(text="Пожалуйста, введите корректные значения.")
        return

    inputA.config(bg="#ecf0f1")
    inputB.config(bg="#ecf0f1")
    inputC.config(bg="#ecf0f1")

    try:
        a = float(inputA.get())
        b = float(inputB.get())
        c = float(inputC.get())

        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c

        # Создание графика
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(x, y, label=f"y = {a}x² + {b}x + {c}")
        ax.set_title("График квадратной функции")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)

        # Вершина параболы
        x_vertex = -b / (2 * a)
        y_vertex = a * x_vertex**2 + b * x_vertex + c
        ax.scatter(x_vertex, y_vertex, color='red')
        ax.text(x_vertex, y_vertex, f"({x_vertex:.2f}, {y_vertex:.2f})",
                fontsize=10, va='bottom', ha='right')

        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.legend()

        # Если график уже есть — удаляем
        if canvas:
            canvas.get_tk_widget().destroy()

        # Вставка графика в окно
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().place(x=400, y=80)

    except ValueError:
        solve.config(text="Неверный ввод для графика")

# --------------------------------------------------
# nuppud
# --------------------------------------------------

solve_button = Button(window, text="Решить", command=solve_quadratic, bg="#27ae60", fg="white", font=("Arial", 14), relief=FLAT)
plot_button = Button(window, text="График", command=plot_graph, bg="#2980b9", fg="white", font=("Arial", 14), relief=FLAT)
exit_button = Button(window, text="Выход", command=exit, bg="RED", fg="white", font=("Arial", 14), relief=FLAT)

# --------------------------------------------------
# упаковка элементов
# --------------------------------------------------

pealkiri.place(x=50, y=20)
inputA.place(x=50, y=80, width=40)
inputB.place(x=150, y=80, width=40)
inputC.place(x=250, y=80, width=40)

TEXT1.place(x=100, y=86, width=40)
TEXT2.place(x=200, y=86, width=40)
TEXT3.place(x=300, y=86, width=40)

solve_button.place(x=50, y=150, width=200, height=40)
plot_button.place(x=50, y=200, width=200, height=40)
solve.place(x=50, y=300, height=40)
exit_button.place(x=50, y=1000, height=40)

# ---------------------------------------------------
window.mainloopg()

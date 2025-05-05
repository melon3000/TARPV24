from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

# root - окно
# ---------------------------------------------------
window = Tk()  # создание окна

# ---------------------------------------------------
# Настройка внутри окна
# --------------------------------------------------

window.title("Решение квадратного уравнения")  # заголовок
window.configure(bg="#2c3e50")  # цвет заднего фона
window.resizable(width=False, height=False)  # 1/0 изменения размера окна
window.iconbitmap("Teema-8//icon1234.ico")  # иконка
window.attributes("-fullscreen", True)

# --------------------------------------------------
# элементы
# --------------------------------------------------

pealkiri = Label(window, text="Решение квадратного уравнения", bg="#2c3e50", font=("Arial", 22), fg="white")  # заголовок

# Поле ввода
inputA = Entry(window, bg="#ecf0f1", font=("Arial", 18), fg="black")
inputB = Entry(window, bg="#ecf0f1", font=("Arial", 18), fg="black")
inputC = Entry(window, bg="#ecf0f1", font=("Arial", 18), fg="black")

inputA.insert(0, "")
inputB.insert(0, "")
inputC.insert(0, "")

#X**2+, X+, + =0
TEXT1 = Label(window, text="X^2 +", bg="#2c3e50", font=("Arial", 12), fg="WHITE")  # добавление заголовка
TEXT2 = Label(window, text="X +", bg="#2c3e50", font=("Arial", 12), fg="WHITE")  # добавление заголовка
TEXT3 = Label(window, text="= 0", bg="#2c3e50", font=("Arial", 12), fg="WHITE")  # добавление заголовка

answer = "Решение будет отображено сдесь."
solve = Label(window, text=answer, bg="#2c3e50", font=("Arial", 16), fg="white")  # результат

# --------------------------------------------------
# Функции / обработчики
# --------------------------------------------------

def on_focus_in(event, entry):
    """При фокусе на поле ввода меняем его цвет на чуть темнее."""
    entry.config(bg="#bdc3c7")

def on_focus_out(event, entry):
    """При потере фокуса восстанавливаем стандартный цвет."""
    entry.config(bg="#ecf0f1")

def validate_input():
    """Проверка на пустые поля и неправильный ввод."""
    try:
        a = float(inputA.get())
        b = float(inputB.get())
        c = float(inputC.get())
        return True
    except ValueError:
        return False

def solve_quadratic():
    if not validate_input():
        # Подсвечиваем неверные поля красным
        if not inputA.get():
            inputA.config(bg="red")
        if not inputB.get():
            inputB.config(bg="red")
        if not inputC.get():
            inputC.config(bg="red")
        
        solve.config(text="Пожалуйста, введите корректные значения.")
        return

    # Очищаем подсветку после правильного ввода
    inputA.config(bg="#ecf0f1")
    inputB.config(bg="#ecf0f1")
    inputC.config(bg="#ecf0f1")

    try:
        a = float(inputA.get())
        b = float(inputB.get())
        c = float(inputC.get())

        # Решение квадратного уравнения
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            x1 = (-b + np.sqrt(discriminant)) / (2*a)
            x2 = (-b - np.sqrt(discriminant)) / (2*a)
            result = f"Корни: x1 = {x1:.2f}, x2 = {x2:.2f}"
        else:
            result = "Нет реальных корней"
    except ValueError:
        result = "Неверный ввод."

    solve.config(text=result)


def plot_graph():
    if not validate_input():
        # Подсвечиваем неверные поля красным
        if not inputA.get():
            inputA.config(bg="red")
        if not inputB.get():
            inputB.config(bg="red")
        if not inputC.get():
            inputC.config(bg="red")
        
        solve.config(text="Пожалуйста, введите корректные значения.")
        return

    # Очищаем подсветку после правильного ввода
    inputA.config(bg="#ecf0f1")
    inputB.config(bg="#ecf0f1")
    inputC.config(bg="#ecf0f1")

    try:
        # Получение значений коэффициентов a, b, c
        a = float(inputA.get())
        b = float(inputB.get())
        c = float(inputC.get())

        # График функции y = ax^2 + bx + c
        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c

        # Находим координаты вершины параболы
        x_vertex = -b / (2 * a)
        y_vertex = a * x_vertex**2 + b * x_vertex + c

        # Построение графика
        plt.plot(x, y, label=f"y = {a}x² + {b}x + {c}")
        plt.title("График квадратной функции")
        plt.xlabel("x")
        plt.ylabel("y")

        # Отображение вершины
        plt.scatter(x_vertex, y_vertex, color='red')  # точка вершины
        plt.text(x_vertex, y_vertex, f"({x_vertex:.2f}, {y_vertex:.2f})", fontsize=12, verticalalignment='bottom', horizontalalignment='right')

        # Добавление осей
        plt.axhline(0, color='black', linewidth=1)  # ось X
        plt.axvline(0, color='black', linewidth=1)  # ось Y

        # Сетка
        plt.grid(True)

        # Легенда
        plt.legend()

        # Показ графика
        plt.show()

    except ValueError:
        solve.config(text="Неверный ввод для графика")

# Кнопки
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
# MAIN LOOP
# Привязываем события focus в/выход
inputA.bind("<FocusIn>", lambda event: on_focus_in(event, inputA))
inputA.bind("<FocusOut>", lambda event: on_focus_out(event, inputA))

inputB.bind("<FocusIn>", lambda event: on_focus_in(event, inputB))
inputB.bind("<FocusOut>", lambda event: on_focus_out(event, inputB))

inputC.bind("<FocusIn>", lambda event: on_focus_in(event, inputC))
inputC.bind("<FocusOut>", lambda event: on_focus_out(event, inputC))

# MAIN LOOP
window.mainloop()

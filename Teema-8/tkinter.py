from tkinter import *

k=0

def tuhista(event):
    sisestus.delete(0, END)


def clicked():
    global k
    k+=1
    pealkiri.config(text=f"Sa vajutasid siia {k} korda")
    nupp.config(text="Vajuta siia veelkord!", bg="orange", fg="blue", width=100, height=100)

def clickedPK(event):
    global k
    k-=1
    pealkiri.config(text=f"Sa vajutasid siia {k} korda")
    nupp.config(text="Vajuta siia veelkord!", bg="blue", fg="orange", width=100, height=100)

#root - окно
#---------------------------------------------------
window = Tk() # создание окна

#---------------------------------------------------
#Настройка внутри окна
window.title("Title") # заголовок
window.geometry("512x512") # размер
window.configure(bg="#222233") # цвет заднего фона
window.resizable(width=False, height=False,) # 1/0 изменения размера окна
window.iconbitmap("Teema-8//icon123.ico") # иконка

#--------------------------------------------------
#elements

pealkiri=Label(window, text="Welcome", bg="#222233", font=("Arial", 32), fg="white") # добавление заголовка
nupp=Button(window, text="Press me", bg="#222222", font=("Arial", 12), fg="white", relief=RAISED, command=clicked) # добавление кнопки
nupp.bind("<Button-3>",clickedPK)

sisestus = Entry(window, bg="white", font=("arial", 20), fg="black")
sisestus.insert(1, "Sisesta midagi.") #END
sisestus.bind("<FocusIn>", tuhista)

pealkiri.pack(pady=20)
sisestus.pack(pady=20)
nupp.pack()
#---------------------------------------------------
#MAIN LOOP
window.mainloop()

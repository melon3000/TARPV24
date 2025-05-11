from tkinter import filedialog, messagebox, ttk
from tkinter import *
import smtplib, ssl
from email.message import EmailMessage
import os

#-----------------------------------------------------------------------------------------------------

aken = Tk()                      
aken.title("E-kirja saatmine")       
aken.geometry("530x460")        
aken.configure(bg="white")      
aken.resizable(width=False, height=False) 

#------------------------------------------------------------------------------------------------------

def theme():
    current_bg = aken["bg"]

    if current_bg == "white":
        # Тёмная тема
        aken.configure(bg="black")
        label_bg = "black"
        label_fg = "white"
        entry_bg = "#3A3A3A"
        entry_fg = "white"
        button_bg = "#444"
        button_fg = "white"
        lisa_bg = "#111111"
    else:
        # Светлая тема
        aken.configure(bg="white")
        label_bg = "green"
        label_fg = "white"
        entry_bg = "#E1EFDF"
        entry_fg = "black"
        button_bg = "green"
        button_fg = "black"
        lisa_bg = "white"

    # Обновляем элементы вручную
    email_label.configure(bg=label_bg, fg=label_fg)
    teema_label.configure(bg=label_bg, fg=label_fg)
    lisa_label.configure(bg=label_bg, fg=label_fg)
    kiri_label.configure(bg=label_bg, fg=label_fg)

    email.configure(bg=entry_bg, fg=entry_fg)
    teema.configure(bg=entry_bg, fg=entry_fg)
    kiri.configure(bg=entry_bg, fg=entry_fg)
    lisa.configure(bg=lisa_bg, fg=entry_fg)

    nupp.configure(bg=button_bg, fg=button_fg)
    nupp_2.configure(bg=button_bg, fg=button_fg)
    nupp_3.configure(bg=button_bg, fg=button_fg)

def tyhjenda():
    email.delete(0, 'end')
    teema.delete(0, 'end')
    kiri.delete('1.0', 'end')
    lisa.config(text="") 
    lisa.config(image="")

    

def vali_pilt():
    global file
    file = filedialog.askopenfilename()
    file_name = os.path.basename(file)  # Extract only the file name
    lisa.configure(text=file_name)  # Display only the file name
    return file

def saada():
    kellele = email.get()
    text = kiri.get("1.0", END)
    error = False  # Флаг для отслеживания ошибок

    try:
        if email.get().strip() == "":
            email.configure(bg="red")
            error = True
        else:
            email.configure(bg="#E1EFDF")

        if teema.get().strip() == "":
            teema.configure(bg="red")
            error = True
        else:
            teema.configure(bg="#E1EFDF")

        kiri_text = text.strip()
        if kiri_text == "":
            kiri.configure(bg="red")
            error = True
        else:
            kiri.configure(bg="#E1EFDF")

        if error:
            return
    except Exception as e:
        print(f"Viga: {e}")
        return

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "nikitosik.pidoras@gmail.com"
    em_passh = os.getenv("em_passh") # cmd -> setx em_passh = "xxxx xxxx xxxx xxxx"
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(text)
    msg["Subject"] = "E-kiri saatmine"
    msg["From"] = f"{sender_email}"
    msg["To"] = kellele
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(sender_email, em_passh)
            server.send_message(msg)
        messagebox.showinfo(message="E-kiri saadetud")
        email.configure(bg="#E1EFDF")
        teema.configure(bg="#E1EFDF")
        kiri.configure(bg="#E1EFDF")
        email.delete(0, END)
        teema.delete(0, END)
        kiri.delete("1.0", END)

    except Exception as e:
        messagebox.showinfo(message=f"Viga: {e}")

#------------------------------------------------------------------------------------------------------

email_label = Label(aken, text="EMAIL:", bg="green", font=("Times New Roman", 25), fg="white", width=12)   
teema_label = Label(aken, text="TEEMA:", bg="green", font=("Times New Roman", 25), fg="white", width=12)
lisa_label = Label(aken, text="LISA:", bg="green", font=("Times New Roman", 25), fg="white", width=12)
kiri_label = Label(aken, text="KIRI:", bg="green", font=("Times New Roman", 25), fg="white", width=12)

email=Entry(aken, bg="#E1EFDF", font=("Arial", 14), fg="black", width=30)  
teema=Entry(aken, bg="#E1EFDF", font=("Arial", 14), fg="black", width=30)  
lisa=Label(aken, bg="white", font=("Arial", 14), fg="black", width=30)  
kiri=Text(aken, bg="#E1EFDF", font=("Arial", 14), fg="black", width=30)  

nupp = Button(aken, text="LISA PILT", bg="green", font=("Arial", 25), fg="black", relief=RAISED, command=vali_pilt)
nupp_2 = Button(aken, text="SAADA", bg="green", font=("Arial", 25), fg="black", relief=RAISED, command=saada)
nupp_3 = Button(aken, text="TEEMA", bg="green", font=("Arial", 25), fg="black", relief=RAISED, command=theme)
nupp_4 = Button(aken, text="🗑", bg="red", font=("Arial", 25), fg="white", relief=RAISED, command=tyhjenda)

#-----------------------------------------------------------------------------------------------------

email_label.place(x=0, y=0, width=200)
teema_label.place(x=0, y=43, width=200)
lisa_label.place(x=0, y=86, width=200)
kiri_label.place(x=0, y=230, width=200)

email.place(x=200, y=0, height=46)
teema.place(x=200, y=45, height=46)
lisa.place(x=200, y=89, height=46)
kiri.place(x=200, y=128, height=250)

nupp.place(x=350, y=390)
nupp_2.place(x=200, y=390)
nupp_3.place(x=50, y=390)
nupp_4.place(x=0, y=390)

#-----------------------------------------------------------------------------------------------------

progress = ttk.Progressbar(aken, mode='indeterminate', length=200)
progress.place(x=160, y=360)


#-----------------------------------------------------------------------------------------------------
aken.mainloop()


"""
🖼 Дополнительные возможности

1 Предварительный просмотр письма - добавьте возможность предварительного просмотра письма перед отправкой.

2 Автоматическое сохранение шаблонов, чтобы не потерять письмо при закрытии программы.

///3 Отправка нескольким адресатам (адреса электронной почты, разделенные запятыми). 

4 Добавление нескольких вложений, а не только одного файла.

5 Сохранение отправленных писем в журнале или базе данных.

🎨 Улучшение пользовательского интерфейса.

1 Использование 1 ttk для улучшения оформления (более стильные кнопки и поля ввода).

2 Строка загрузки при отправке, чтобы пользователь мог видеть ход процесса.

///3 Выбор темы (темный/светлый режим) - добавление переключателя.

///4 Кнопка «Очистить форму», чтобы можно было быстро очистить все поля.

📤 Расширенные возможности отправки

1 Добавление подписи к письму (настройки пользователя).

2 Возможность форматирования текста (tkinter.Text с жирным, курсивным и различными вариантами шрифта).

3 Отправка HTML-писем с возможностью форматирования. 
"""


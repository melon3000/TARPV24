from tkinter import filedialog
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

def vali_pilt():
    global file
    file = filedialog.askopenfilename()
    file_name = os.path.basename(file)  # Извлекаем только название файла
    lisa.configure(text=file_name)  # Отображаем только имя файла
    return file

def saada():
    kellele = email.get()
    text = kiri.get("1.0", END)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "nikitosik.pidoras@gmail.com"
    password = "rwks xdlx cxfk mpvr"
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(text)
    msg["Subject"] = "E-kiri saatmine"
    msg["From"] = f"{sender_email}"
    msg["To"] = kellele
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)
        lisa.config(text="E-kiri saadetud")
        email.delete(0, END)
        teema.delete(0, END)
        kiri.delete("1.0", END)

    except Exception as e:
        lisa.config(text=f"Viga: {e}")

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

#-----------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------
aken.mainloop()
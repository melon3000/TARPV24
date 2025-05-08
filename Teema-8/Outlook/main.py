from tkinter.font import BOLD, ITALIC
import customtkinter as ctk
from tkinter import filedialog, messagebox
import smtplib, ssl
from email.message import EmailMessage
import imghdr
import os

# ----------------------------------------------------------------------------------------------------------------------------
# Глобальная переменная для файла
selected_image_path = None

def upload_image():
    global selected_image_path
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if filename:
        selected_image_path = filename
        image_label.configure(text=f"Pilt: {os.path.basename(filename)}")
    else:
        selected_image_path = None
        image_label.configure(text="Pilt pole valitud")

def send_email():
    global selected_image_path
    email = email_entry.get()
    teema = teema_entry.get()
    message = kiri_text.get("1.0", "end-1c")

    if not email or not teema or not message:
        messagebox.showerror("Viga", "Kõik väljad peavad olema täidetud!")
        return

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "nikitosik.pidoras@gmail.com"
    password = "rwks xdlx cxfk mpvr" 

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = teema
    msg['From'] = sender_email
    msg['To'] = email

    if selected_image_path:
        with open(selected_image_path, 'rb') as f:
            img_data = f.read()
            img_type = imghdr.what(None, img_data)
            img_name = os.path.basename(selected_image_path)
        msg.add_attachment(img_data, maintype='image', subtype=img_type, filename=img_name)

    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("Teade", "E-kiri on edukalt saadetud!")
    except Exception as e:
        messagebox.showerror("Tekkis viga!", str(e))
    finally:
        server.quit()

# ----------------------------------------------------------------------------------------------------------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("NewMail")
app.geometry("500x720")
app.resizable(width=False, height=False)

# ----------------------------------------------------------------------------------------------------------------------------
BG_COLOR = "#2D2D30"
INPUT_COLOR = "#3C3C3C"
TEXT_COLOR = "#FFFFFF"
ACCENT_COLOR = "#0078D7"
# ----------------------------------------------------------------------------------------------------------------------------
app.configure(bg=BG_COLOR)

title_label = ctk.CTkLabel(app, text="E-MAIL", text_color=TEXT_COLOR, font=("Segoe UI", 26, "bold"))
title_label.pack(pady=(20, 10))

glow_label = ctk.CTkLabel(app, text="───────────────", text_color=ACCENT_COLOR, font=("Segoe UI", 16))
glow_label.pack(pady=(0, 20))

# Email
email_label = ctk.CTkLabel(app, text="EMAIL:", text_color=TEXT_COLOR, font=("Segoe UI", 14, BOLD))
email_label.pack(anchor="w", padx=30)
email_entry = ctk.CTkEntry(app, width=500, fg_color=INPUT_COLOR, border_color=ACCENT_COLOR, text_color=TEXT_COLOR, corner_radius=10)
email_entry.pack(padx=30, pady=8)

# Teema
teema_label = ctk.CTkLabel(app, text="TEEMA:", text_color=TEXT_COLOR, font=("Segoe UI", 14, BOLD))
teema_label.pack(anchor="w", padx=30, pady=(20, 0))
teema_entry = ctk.CTkEntry(app, width=500, fg_color=INPUT_COLOR, border_color=ACCENT_COLOR, text_color=TEXT_COLOR, corner_radius=10)
teema_entry.pack(padx=30, pady=8)

# Lisa pilt
pilt_label = ctk.CTkLabel(app, text="LISA PILT:", text_color=TEXT_COLOR, font=("Segoe UI", 14, BOLD))
pilt_label.pack(anchor="w", padx=30, pady=(20, 0))
upload_button = ctk.CTkButton(app, text="Laadi pilt", command=upload_image, fg_color=ACCENT_COLOR, corner_radius=10)
upload_button.pack(padx=30, pady=8)

image_label = ctk.CTkLabel(app, text="Pilt pole valitud", text_color=TEXT_COLOR, font=("Segoe UI", 12, ITALIC))
image_label.pack(anchor="center", padx=30, pady=5)

# Kiri
kiri_label = ctk.CTkLabel(app, text="KIRI:", text_color=TEXT_COLOR, font=("Segoe UI", 14, BOLD))
kiri_label.pack(anchor="w", padx=30, pady=(20, 0))
kiri_text = ctk.CTkTextbox(app, width=500, height=150, fg_color=INPUT_COLOR, border_color=ACCENT_COLOR, text_color=TEXT_COLOR, corner_radius=10)
kiri_text.pack(padx=30, pady=8)

# Saada
send_button = ctk.CTkButton(app,text="Saada",command=send_email,fg_color=ACCENT_COLOR,corner_radius=10,font=("Segoe UI", 14))
send_button.pack(pady=30)

app.mainloop()

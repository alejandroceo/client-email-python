import tkinter as tk
from tkinter import messagebox, PhotoImage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Datos del correo
SENDER_EMAIL = "emails@email.website"  # Cambia esto por tu correo electrónico
SENDER_PASSWORD = "password#"    # Cambia esto por tu contraseña

# Función para enviar el correo
def send_email():
    try:
        receiver_email = receiver_entry.get()
        subject = subject_entry.get()
        body = body_text.get("1.0", tk.END)

        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Configura el servidor SMTP (ejemplo con Gmail)
        server = smtplib.SMTP('mail.privateemail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        server.quit()

        messagebox.showinfo("Éxito", "Correo enviado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el correo: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Cliente de Email")

# Cargar y colocar el logo
logo = PhotoImage(file="/home/predator/Escritorio/email-python/logos.png")  # Asegúrate de cambiar esta ruta a la ubicación de tu logo
logo_label = tk.Label(root, image=logo)
logo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Estilos
label_font = ('Arial', 12, 'bold')
entry_font = ('Arial', 12)
button_font = ('Arial', 12, 'bold')
bg_color = '#f0f0f0'
entry_bg_color = '#ffffff'
button_bg_color = '#4caf50'
button_fg_color = '#ffffff'
padding = {'padx': 10, 'pady': 5}

# Configurar el color de fondo
root.configure(bg=bg_color)

# Crear y colocar los widgets
tk.Label(root, text="Destinatario:", font=label_font, bg=bg_color).grid(row=1, column=0, sticky=tk.W, **padding)
receiver_entry = tk.Entry(root, width=50, font=entry_font, bg=entry_bg_color)
receiver_entry.grid(row=1, column=1, **padding)

tk.Label(root, text="Asunto:", font=label_font, bg=bg_color).grid(row=2, column=0, sticky=tk.W, **padding)
subject_entry = tk.Entry(root, width=50, font=entry_font, bg=entry_bg_color)
subject_entry.grid(row=2, column=1, **padding)

tk.Label(root, text="Cuerpo del mensaje:", font=label_font, bg=bg_color).grid(row=3, column=0, sticky=tk.W, **padding)
body_text = tk.Text(root, width=50, height=10, font=entry_font, bg=entry_bg_color)
body_text.grid(row=3, column=1, **padding)

send_button = tk.Button(root, text="Enviar", font=button_font, bg=button_bg_color, fg=button_fg_color, command=send_email)
send_button.grid(row=4, column=1, sticky=tk.E, **padding)

# Añadir más espacio entre los campos
for child in root.winfo_children():
    child.grid_configure(pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()

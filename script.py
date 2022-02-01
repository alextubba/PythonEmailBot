import smtplib, ssl
import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Input a message!")
greeting.pack()

entry = tk.Entry(fg="yellow", bg="grey", width=25)
entry.pack()

greeting2 = tk.Label(text="Input a gmail to send to!")
greeting2.pack()

entry2 = tk.Entry(fg="yellow", bg="grey", width=25)
entry2.pack()

button = tk.Button(
    text="Send!",
    width=20,
    height=3,
    bg="grey",
    fg="yellow",
)

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "culp_alexander@student.mahoningctc.com"
password = "800D0FAa1"

def SendMessage():
    message = entry.get()
    receiver_email = entry2.get()

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

button.bind("<Button-1>", SendMessage)
button.pack()

window.mainloop()
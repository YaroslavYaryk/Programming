import socket
import threading
import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog


HOST = "127.0.0.1"
PORT = 9998


class Client:

    def __init__(self, host, port):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tk.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring(
            "Nickname", "Enter your nickname!!!", parent=msg)

        self.gui_done = False
        self.running = True

        thread_gui_loop = threading.Thread(target=self.gui_loop)
        thread_recieve = threading.Thread(target=self.recieve)

        thread_gui_loop.start()
        thread_recieve.start()

    def gui_loop(self):

        self.win = tk.Tk()
        self.win.configure(bg="lightgray")

        self.chat_label = tk.Label(self.win, text="Chat:", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")

        self.msg_label = tk.Label(self.win, text="Chat:", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tk.Text(self.win, height=5)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tk.Button(self.win, text="send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()

    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode('utf_8'))
        self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def recieve(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf_8')

                if message == "NICK":
                    self.sock.send(self.nickname.encode('utf_8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state="normal")
                        self.text_area.insert('end', message)
                        self.text_area.yview()
                        self.text_area.config(state='disabled')
            except Exception as e:
                self.sock.close()
                break


Client(HOST, PORT)

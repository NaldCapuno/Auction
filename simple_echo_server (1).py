import sys
import tkinter as tk
from python_banyan.banyan_base import BanyanBase
import threading


class EchoServer(BanyanBase):
    def __init__(self):
        super(EchoServer, self).__init__(process_name='Server')

        self.set_subscriber_topic('echo')

        # window
        self.main = tk.Tk()
        self.main.title("SERVER")
        self.main.resizable(False, False)

        self.textbox = tk.Text(self.main, width=35, height=20, state=tk.DISABLED)
        self.textbox.grid(row=0, column=0, padx=10, pady=10)

        # Start the Banyan receive loop in a separate thread
        self.thread = threading.Thread(target=self.receive_loop)
        self.thread.start()

        self.main.mainloop()

    def incoming_message_processing(self, topic, payload):
        self.textbox.configure(state=tk.NORMAL)
        self.textbox.insert(tk.END, f"{payload} is ready...\n")
        self.textbox.configure(state=tk.DISABLED)
        print(payload, 'is ready...')


def echo_server():
    EchoServer()


if __name__ == '__main__':
    echo_server()

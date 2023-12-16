import tkinter as tk
import threading
import time as t
from python_banyan.banyan_base import BanyanBase

class EchoServer(BanyanBase):
    def __init__(self):
        super(EchoServer, self).__init__(process_name='Server')

        self.set_subscriber_topic('echo')

        def start():
            self.time = int(self.entry.get())
            self.button.configure(state=tk.DISABLED)
            threading.Thread(target=self.countdown).start() 

        self.main = tk.Tk()
        self.main.title("SERVER")
        self.main.resizable(False, False)

        self.textbox = tk.Text(self.main, width=45, height=20, state=tk.DISABLED)
        self.textbox.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.label = tk.Label(self.main, text="Countdown (Seconds):")
        self.label.grid(row=1, column=0, padx=10, pady=10)

        self.entry = tk.Entry(self.main)
        self.entry.grid(row=1, column=1, padx=5, pady=10)

        self.button = tk.Button(self.main, text="Start", command=start)
        self.button.grid(row=1, column=2, padx=10, pady=10)

        self.thread = threading.Thread(target=self.receive_loop)
        self.thread.start()

        self.main.mainloop()

    def countdown(self):
        while True:
            self.publish_payload(self.time, 'reply')
            if self.time == 0:
                self.button.configure(state=tk.NORMAL)
                break
            t.sleep(1)
            self.time -= 1

    def incoming_message_processing(self, topic, payload):
        self.textbox.configure(state=tk.NORMAL)
        self.textbox.insert(tk.END, f"{payload} is ready...\n")
        self.textbox.configure(state=tk.DISABLED)


def echo_server():
    EchoServer()


if __name__ == '__main__':
    echo_server()

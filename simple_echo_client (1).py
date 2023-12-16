import sys
import tkinter as tk
from python_banyan.banyan_base import BanyanBase


class EchoClient(BanyanBase):
    def __init__(self):
        super(EchoClient, self).__init__(process_name='Client')

        self.set_subscriber_topic('reply')

        self.client_name = ''

        def accept():
            def client_window(name):
                self.client = tk.Tk()
                self.client.title(f"CLIENT {name}")
                self.client.resizable(False, False)
                self.client.mainloop()

            self.name = self.entry.get()
            self.client_name = self.name
            self.publish_payload(self.client_name, 'echo')
            self.main.destroy()
            client_window(self.client_name)
            self.receive_loop()

        #tkinter window
        self.main = tk.Tk()
        self.main.title("ENTER YOUR NAME")
        self.main.resizable(False, False)

        self.entry = tk.Entry(self.main, width=35)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        self.button = tk.Button(self.main, text="Accept", command=accept)
        self.button.grid(row=0, column=1, padx=10, pady=10)

        self.main.mainloop()

    def incoming_message_processing(self, topic, payload):
        print(payload)


def echo_client():
    EchoClient()


if __name__ == '__main__':
    echo_client()

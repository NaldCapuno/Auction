import sys
import tkinter as tk
from python_banyan.banyan_base import BanyanBase
import threading


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
                
                self.button_bid = tk.Button(text="Bid", width=10)
                self.button_bid.grid(row=0, column=0, padx=10, pady=10)

                self.button_sell = tk.Button(text="Sell", width=10)
                self.button_sell.grid(row=0, column=1, padx=5, pady=10)

                self.label_time = tk.Label(text=f"Time Left: second(s)")
                self.label_time.grid(row=0, column=2, padx=5, pady=10)

                self.client.mainloop()

            self.name = self.entry.get()
            self.client_name = self.name
            self.publish_payload(self.client_name, 'echo')
            self.main.destroy()
            client_window(self.client_name)

        # window
        self.main = tk.Tk()
        self.main.title("ENTER YOUR NAME")
        self.main.resizable(False, False)

        self.entry = tk.Entry(self.main, width=35)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        self.button = tk.Button(self.main, text="Accept", command=accept)
        self.button.grid(row=0, column=1, padx=10, pady=10)

        # Start the Banyan receive loop in a separate thread
        self.thread = threading.Thread(target=self.receive_loop)
        self.thread.start()

        self.main.mainloop()

    def incoming_message_processing(self, topic, payload):
        print(payload)


def echo_client():
    EchoClient()


if __name__ == '__main__':
    echo_client()

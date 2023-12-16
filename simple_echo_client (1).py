import tkinter as tk
import threading
from python_banyan.banyan_base import BanyanBase


class EchoClient(BanyanBase):
    def __init__(self):
        super(EchoClient, self).__init__(process_name='Client')

        self.set_subscriber_topic('reply')

        self.client_name = ''

        def accept():
            self.client_name = self.main_entry.get()
            self.publish_payload(self.client_name, 'echo')
            self.main.destroy()
            self.client_window()

        self.main = tk.Tk()
        self.main.title("ENTER YOUR NAME")
        self.main.resizable(False, False)

        self.main_entry = tk.Entry(self.main, width=35)
        self.main_entry.grid(row=0, column=0, padx=10, pady=10)

        self.main_button = tk.Button(self.main, text="Accept", command=accept)
        self.main_button.grid(row=0, column=1, padx=10, pady=10)

        self.thread = threading.Thread(target=self.receive_loop)
        self.thread.start()

        self.main.mainloop()

    def client_window(self):
        self.client = tk.Tk()
        self.client.title(f"CLIENT {self.client_name}")
        self.client.resizable(False, False)
        
        self.client_button_bid = tk.Button(self.client, text="Bid", width=10)
        self.client_button_bid.grid(row=0, column=0, padx=10, pady=10)

        self.client_button_sell = tk.Button(self.client, text="Sell", width=10)
        self.client_button_sell.grid(row=0, column=1, padx=5, pady=10)

        self.client_label_time = tk.Label(self.client, text=f"Time Left:")
        self.client_label_time.grid(row=0, column=2, padx=5, pady=10)

        self.client_text_time = tk.Text(self.client, width=5, height=1, state=tk.DISABLED)
        self.client_text_time.grid(row=0, column=3, padx=10, pady=10)

        self.client.mainloop()

    def incoming_message_processing(self, topic, payload):
        self.client_text_time.configure(state=tk.NORMAL)
        self.client_text_time.delete('1.0', tk.END)
        self.client_text_time.insert(tk.END, payload)
        self.client_text_time.configure(state=tk.DISABLED)


def echo_client():
    EchoClient()


if __name__ == '__main__':
    echo_client()

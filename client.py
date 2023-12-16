import customtkinter as ctk
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

        # main
        self.main = ctk.CTk()
        self.main.title("ENTER YOUR NAME")
        self.main.resizable(False, False)

        self.main_entry = ctk.CTkEntry(self.main, width=200)
        self.main_entry.grid(row=0, column=0, padx=10, pady=10)

        self.main_button = ctk.CTkButton(self.main, text="Accept", command=accept, width=50)
        self.main_button.grid(row=0, column=1, padx=10, pady=10)

        threading.Thread(target=self.receive_loop).start()

        self.main.mainloop()

    def client_window(self):
        self.client = ctk.CTk()
        self.client.title(f"CLIENT {self.client_name}")
        self.client.resizable(False, False)
        
        # top
        self.client_button_bid = ctk.CTkButton(self.client, text="Bid", command=self.bid_window, width=75)
        self.client_button_bid.grid(row=0, column=0, padx=10, pady=10)

        self.client_button_sell = ctk.CTkButton(self.client, text="Sell", command=self.sell_window, width=75)
        self.client_button_sell.grid(row=0, column=1, padx=5, pady=10)

        self.client_label_time = ctk.CTkLabel(self.client, text="Time Left:")
        self.client_label_time.grid(row=0, column=2, padx=5, pady=10)

        self.client_text_time = ctk.CTkTextbox(self.client, width=50, height=10, state=ctk.DISABLED)
        self.client_text_time.grid(row=0, column=3, padx=10, pady=10)
        
        # item bidding
        self.client_label_bidding = ctk.CTkLabel(self.client, text="Item for BIDDING:")
        self.client_label_bidding.grid(row=1, columnspan=4)        
        
        self.client_text_bidding = ctk.CTkTextbox(self.client, width=300, height=150, state=ctk.DISABLED)
        self.client_text_bidding.grid(row=2, columnspan=4, padx=10, pady=10)
        
        # item selling
        self.client_label_selling = ctk.CTkLabel(self.client, text="Item you are SELLING:")
        self.client_label_selling.grid(row=3, columnspan=4)

        self.client_text_selling = ctk.CTkTextbox(self.client, width=300, height=150, state=ctk.DISABLED)
        self.client_text_selling.grid(row=4, columnspan=4, padx=10, pady=10)

        # highest bidder
        self.client_label_highest = ctk.CTkLabel(self.client, text="Highest BIDDER:")
        self.client_label_highest.grid(row=5, columnspan=4)

        self.client_text_highest = ctk.CTkTextbox(self.client, width=300, height=150, state=ctk.DISABLED)
        self.client_text_highest.grid(row=6, columnspan=4, padx=10, pady=10)

        self.client.mainloop()

    def bid_window(self):
        self.bid = ctk.CTk()
        self.bid.title("BIDDING...")
        self.bid.resizable(False, False)

        self.bid.mainloop()

    def sell_window(self):
        self.sell = ctk.CTk()
        self.sell.title("SELLING...")
        self.sell.resizable(False, False)

        self.sell.mainloop()

    def incoming_message_processing(self, topic, payload):
        self.client_text_time.configure(state=ctk.NORMAL)
        self.client_text_time.delete('1.0', ctk.END)
        self.client_text_time.insert(ctk.END, payload)
        self.client_text_time.configure(state=ctk.DISABLED)


def echo_client():
    EchoClient()


if __name__ == '__main__':
    echo_client()

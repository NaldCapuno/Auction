import customtkinter as ctk
import threading
from CTkListbox import CTkListbox
from python_banyan.banyan_base import BanyanBase

class EchoClient(BanyanBase):
    def __init__(self):
        super(EchoClient, self).__init__(process_name='Client')

        self.set_subscriber_topic('reply')

        self.client_name = ''

        def accept_name():
            self.client_name = self.main_entry.get()
            self.publish_payload({'client_name':self.client_name}, 'echo')
            self.main.destroy()
            self.client_window()

        # main
        self.main = ctk.CTk()
        self.main.title("ENTER YOUR NAME")
        self.main.resizable(False, False)

        self.main_entry = ctk.CTkEntry(self.main, width=200)
        self.main_entry.grid(row=0, column=0, padx=10, pady=10)

        self.main_button = ctk.CTkButton(self.main, text="Accept", command=accept_name, width=50)
        self.main_button.grid(row=0, column=1, padx=10, pady=10)

        threading.Thread(target=self.receive_loop).start()

        self.main.mainloop()

    def client_window(self):
        self.client = ctk.CTk()
        self.client.title(f"CLIENT {self.client_name}")
        self.client.resizable(False, False)
        
        # top
        self.client_button_bid = ctk.CTkButton(self.client, text="Bid", command=self.bid_window, width=75, state=ctk.DISABLED)
        self.client_button_bid.grid(row=0, column=0, padx=10, pady=10)

        self.client_button_sell = ctk.CTkButton(self.client, text="Sell", command=self.sell_window, width=75, state=ctk.DISABLED)
        self.client_button_sell.grid(row=0, column=1, padx=5, pady=10)

        self.client_label_time = ctk.CTkLabel(self.client, text="Time Left:")
        self.client_label_time.grid(row=0, column=2, padx=5, pady=10)

        self.client_text_time = ctk.CTkTextbox(self.client, width=50, height=10, state=ctk.DISABLED)
        self.client_text_time.grid(row=0, column=3, padx=10, pady=10)
        
        # item bidding
        self.client_label_bidding = ctk.CTkLabel(self.client, text="Item for BIDDING:")
        self.client_label_bidding.grid(row=1, columnspan=4)        
        
        self.client_listbox_bidding = CTkListbox(self.client, width=270, height=125)
        self.client_listbox_bidding._scrollbar.configure(height=0)
        self.client_listbox_bidding.grid(row=2, columnspan=4, padx=10, pady=10)
        
        # item selling
        self.client_label_selling = ctk.CTkLabel(self.client, text="Item you are SELLING:")
        self.client_label_selling.grid(row=3, columnspan=4)

        self.client_listbox_selling = CTkListbox(self.client, width=270, height=125)
        self.client_listbox_selling._scrollbar.configure(height=0)
        self.client_listbox_selling.grid(row=4, columnspan=4, padx=10, pady=10)

        # highest bidder
        self.client_label_highest = ctk.CTkLabel(self.client, text="Highest BIDDER:")
        self.client_label_highest.grid(row=5, columnspan=4)

        self.client_listbox_highest = CTkListbox(self.client, width=270, height=125)
        self.client_listbox_highest._scrollbar.configure(height=0)
        self.client_listbox_highest.grid(row=6, columnspan=4, padx=10, pady=10)

        self.client.mainloop()

    def bid_window(self):
        self.bid = ctk.CTk()
        self.bid.title("BIDDING...")
        self.bid.resizable(False, False)

        self.bidder_name = self.client_name
        self.bid_item_name = self.client_listbox_bidding.get()
        self.bid_item_price = 0

        def accept_bid():
            self.bid_item_price = self.bid_entry_price.get()

            self.publish_payload({'bid_item_name':self.bid_item_name, 'bid_item_price':self.bid_item_price, 'bidder_name':self.bidder_name}, 'echo')

            self.bid.destroy()

        # bid
        self.bid_label_item = ctk.CTkLabel(self.bid, text=f"{self.bid_item_name}:")
        self.bid_label_item.grid(row=0, column=0, padx=10, pady=10)

        self.bid_entry_price = ctk.CTkEntry(self.bid, width=100)
        self.bid_entry_price.grid(row=0, column=1, pady=10)

        self.bid_button_accept = ctk.CTkButton(self.bid, text='Accept', command=accept_bid, width=50)
        self.bid_button_accept.grid(row=0, column=2, padx=10, pady=10)

        self.bid.mainloop()

    def sell_window(self):
        self.sell = ctk.CTk()
        self.sell.title("SELLING...") 
        self.sell.resizable(False, False)

        self.seller_name = self.client_name
        self.sell_item_name = ''
        self.sell_item_price = 0

        def accept_sell():
            self.sell_item_name = self.sell_entry_item.get()
            self.sell_item_price = int(self.sell_entry_price.get())
            
            self.client_listbox_selling.insert(ctk.END, f"{self.sell_item_name} Php{self.sell_item_price}")

            self.publish_payload({'sell_item_name':self.sell_item_name, 'sell_item_price':self.sell_item_price, 'seller_name':self.seller_name}, 'echo')

            self.sell.destroy()

        # item
        self.sell_label_item = ctk.CTkLabel(self.sell, text='Item:')
        self.sell_label_item.grid(row=0, column=0, padx=10, pady=10)

        self.sell_entry_item = ctk.CTkEntry(self.sell, width=100)
        self.sell_entry_item.grid(row=0, column=1)

        # price
        self.sell_label_price = ctk.CTkLabel(self.sell, text='Price:')
        self.sell_label_price.grid(row=0, column=2, padx=10, pady=10)

        self.sell_entry_price = ctk.CTkEntry(self.sell, width=100)
        self.sell_entry_price.grid(row=0, column=3)

        # accept
        self.sell_button_accept = ctk.CTkButton(self.sell, text='Accept', command=accept_sell, width=50)
        self.sell_button_accept.grid(row=0, column=4, padx=10, pady=10)

        self.sell.mainloop()

    def incoming_message_processing(self, topic, payload):
        if 'time' in payload:
            self.client_text_time.configure(state=ctk.NORMAL)
            self.client_text_time.delete('1.0', ctk.END)
            self.client_text_time.insert(ctk.END, payload['time'])
            self.client_text_time.configure(state=ctk.DISABLED)
            self.client_button_bid.configure(state=ctk.NORMAL)
            self.client_button_sell.configure(state=ctk.NORMAL)
            if payload['time'] == 0:
                self.client_button_bid.configure(state=ctk.DISABLED)
                self.client_button_sell.configure(state=ctk.DISABLED)

        if 'sell_item_name' in payload and 'sell_item_price' in payload and 'seller_name' in payload:
            if payload['seller_name'] == self.client_name:
                pass

            else:
                self.client_listbox_bidding.insert(ctk.END, f"{payload['sell_item_name']}, Php{payload['sell_item_price']} [{payload['seller_name']}]")


def echo_client():
    EchoClient()


if __name__ == '__main__':
    echo_client()

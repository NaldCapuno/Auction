import customtkinter as ctk
import threading
import time as t
from CTkMessagebox import CTkMessagebox
from python_banyan.banyan_base import BanyanBase

class EchoServer(BanyanBase):
    def __init__(self):
        super(EchoServer, self).__init__(process_name='Server')

        self.set_subscriber_topic('echo')

        self.time = 0

        def start():
            self.time = int(self.main_entry.get())
            if self.time > 0:
                self.main_entry.configure(state=ctk.DISABLED)
                self.main_button_start.configure(state=ctk.DISABLED)
                self.main_button_close.configure(state=ctk.NORMAL)
                threading.Thread(target=self.countdown).start() 
            else:
                CTkMessagebox(title='Error', message='Invalid Time!', icon='cancel')

        def close():
            self.time = 1
            self.main_button_close.configure(state=ctk.DISABLED)

        # main
        self.main = ctk.CTk()
        self.main.title("SERVER")
        self.main.resizable(False, False)

        self.main_textbox = ctk.CTkTextbox(self.main, width=330, height=450, state=ctk.DISABLED)
        self.main_textbox.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        self.main_label = ctk.CTkLabel(self.main, text="Countdown (Seconds):")
        self.main_label.grid(row=1, column=0, padx=10, pady=10)

        self.main_entry = ctk.CTkEntry(self.main, width=50)
        self.main_entry.grid(row=1, column=1, padx=10, pady=10)

        self.main_button_start = ctk.CTkButton(self.main, text="Start", command=start, width=50)
        self.main_button_start.grid(row=1, column=2, pady=10)

        self.main_button_close = ctk.CTkButton(self.main, text="Close", command=close, width=50, state=ctk.DISABLED)
        self.main_button_close.grid(row=1, column=3, padx=10, pady=10)

        threading.Thread(target=self.receive_loop).start()

        self.main.mainloop()

    def countdown(self):
        while True:
            self.publish_payload({'time':self.time}, 'reply')
            if self.time == 0:
                self.main_entry.configure(state=ctk.NORMAL)
                self.main_button_start.configure(state=ctk.NORMAL)
                break
            t.sleep(1)
            self.time -= 1

    def incoming_message_processing(self, topic, payload):
        if 'client_name' in payload:
            self.main_textbox.configure(state=ctk.NORMAL)
            self.main_textbox.insert(ctk.END, f"{payload['client_name']} is ready...\n")
            self.main_textbox.configure(state=ctk.DISABLED)

        if 'sell_item_name' in payload and 'sell_item_price' in payload and 'seller_name' in payload:
            self.main_textbox.configure(state=ctk.NORMAL)
            self.main_textbox.insert(ctk.END, f"Selling: {payload['sell_item_name']}, Php{payload['sell_item_price']} [{payload['seller_name']}]\n")
            self.main_textbox.configure(state=ctk.DISABLED)
            self.publish_payload({'sell_item_name':payload['sell_item_name'], 'sell_item_price':payload['sell_item_price'], 'seller_name':payload['seller_name']}, 'reply')

        if 'bid_item_name' in payload and 'bid_price' in payload and 'bidder_name' in payload:
            self.main_textbox.configure(state=ctk.NORMAL)
            self.main_textbox.insert(ctk.END, f"Bidding: {payload['bid_item_name']} => {payload['bid_price']} [{payload['bidder_name']}]\n")
            self.main_textbox.configure(state=ctk.DISABLED)


def echo_server():
    EchoServer()


if __name__ == '__main__':
    echo_server()

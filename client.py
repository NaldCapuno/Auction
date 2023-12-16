import tkinter as tk
from tkinter import messagebox
from python_banyan.banyan_base import BanyanBase

class BiddingApp(BanyanBase):
    def __init__(self, main):
        super().__init__(process_name='EchoClient')

        # Window
        self.main = main
        self.main.title("ENTER YOUR NAME")
        self.main.resizable(False, False)
        self.main.configure(bg='#d3d3d3')
        self.set_subscriber_topic('send')

        # Entry
        self.entry = tk.Entry(self.main, width=35)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        # Button
        self.button = tk.Button(self.main, text="Accept", command=self.accept, width=5)
        self.button.grid(row=0, column=1, padx=10, pady=10)

    def accept(self):
        name = self.entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter a valid name.")
        else:
            self.main.destroy() 
            ClientWindow(name)

class ClientWindow:
    def __init__(self, name):
        # Window
        self.client = tk.Tk()
        self.client.title(f"CLIENT {name}")
        self.client.resizable(False, False)
        self.client.configure(bg='#d3d3d3')

        # Button
        self.button_bid = tk.Button(self.client, text="Bid", command=self.bidding, width=10)
        self.button_bid.grid(row=0, column=0, padx=10, pady=10)

        self.button_sell = tk.Button(self.client, text="Sell", command=self.selling, width=10)
        self.button_sell.grid(row=0, column=1, padx=5, pady=10)

        # Label
        self.label_time = tk.Label(self.client, text=f"TIME LEFT: second(s)", bg='#d3d3d3')
        self.label_time.grid(row=0, column=3, padx=5, pady=10)

        self.label_item_for_bidding = tk.Label(self.client, text=f"Item for BIDDING:", bg='#d3d3d3')
        self.label_item_for_bidding.grid(row=1, columnspan=4)

        self.label_item_your_are_selling = tk.Label(self.client, text=f"Item your are SELLING:", bg='#d3d3d3')
        self.label_item_your_are_selling.grid(row=3, columnspan=4)

        self.label_highest_bidder = tk.Label(self.client, text=f"Highest BIDDER:", bg='#d3d3d3')
        self.label_highest_bidder.grid(row=5, columnspan=4)

        # Text Box
        self.box_bidding = tk.Text(self.client, height=10, width=45, state=tk.DISABLED)
        self.box_bidding.grid(row=2, column=0, padx=10, pady=5, columnspan=4)

        self.box_selling = tk.Text(self.client, height=10, width=45, state=tk.DISABLED)
        self.box_selling.grid(row=4, column=0, padx=10, pady=5, columnspan=4)

        self.box_bidder = tk.Text(self.client, height=10, width=45, state=tk.DISABLED)
        self.box_bidder.grid(row=6, column=0, padx=10, pady=5, columnspan=4)

    def bidding(self):
        BiddingWindow()

    def selling(self):
        SellingWindow()

class BiddingWindow:
    def __init__(self):
        # Window
        self.bidding = tk.Tk()
        self.bidding.title(f"BIDDING...")
        self.bidding.resizable(False, False)
        self.bidding.configure(bg='#d3d3d3')

class SellingWindow:
    def __init__(self):
        # Window
        self.selling = tk.Tk()
        self.selling.title(f"SELLING...")
        self.selling.resizable(False, False)
        self.selling.configure(bg='#d3d3d3')

        # Label
        self.label_item = tk.Label(self.selling, text="Item:", bg='#d3d3d3')
        self.label_item.grid(row=0, column=0, padx=10, pady=10)

        self.label_price = tk.Label(self.selling, text="Price:", bg='#d3d3d3')
        self.label_price.grid(row=0, column=2, padx=10, pady=10)

        # Entry
        self.entry_item = tk.Entry(self.selling, width=10)
        self.entry_item.grid(row=0, column=1, pady=10)

        self.entry_price = tk.Entry(self.selling, width=10)
        self.entry_price.grid(row=0, column=3, pady=10)

        # Button
        self.button = tk.Button(self.selling, text="Accept", command=self.add_sell, width=5)
        self.button.grid(row=0, column=4, padx=10, pady=10)

    def add_sell(self):
        item = str(self.entry_item.get())
        price = int(self.entry_price.get())

if __name__ == "__main__":
    main = tk.Tk()
    app = BiddingApp(main)
    main.mainloop()
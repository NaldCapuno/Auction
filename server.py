import tkinter as tk
from tkinter import messagebox
from python_banyan.banyan_base import BanyanBase

class AuctionServer(BanyanBase):
    def __init__(self, main):
        super().__init__(process_name='EchoServer')

        # Window
        self.main = main
        self.main.title("SERVER")
        self.main.resizable(False, False)
        self.main.configure(bg='#d3d3d3')
        self.countdown_running = False

        # Text Box
        self.box = tk.Text(self.main, height=35, width=45, state=tk.DISABLED)
        self.box.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        # Label
        self.label = tk.Label(self.main, text="Countdown (Seconds):", bg='#d3d3d3')
        self.label.grid(row=1, column=0, padx=10, pady=10)

        # Entry
        self.entry = tk.Entry(self.main, width=10)
        self.entry.grid(row=1, column=1, padx=10, pady=10)

        # Button
        self.button_start = tk.Button(self.main, text="Start", command=self.start_countdown, width=5)
        self.button_start.grid(row=1, column=2, padx=5, pady=10)

        self.button_close = tk.Button(self.main, text="Close", command=self.close_countdown, width=5)
        self.button_close.grid(row=1, column=3, padx=5, pady=10)

    def start_countdown(self):
        try:
            seconds = int(self.entry.get())
            if seconds <= 0:
                raise ValueError("Please enter a positive integer.")
            self.entry.configure(state=tk.DISABLED)
            self.button_start.configure(state=tk.DISABLED)
            self.countdown(seconds)
            self.countdown_close = False
            messagebox.showinfo("Info", f"Countdown started for {seconds} seconds!")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def countdown(self, seconds):
        if seconds > 0:
            print(f"Time remaining: {seconds}")
            self.main.after(1000, lambda: self.countdown(seconds - 1))
        else:
            self.entry.configure(state=tk.NORMAL)
            self.button_start.configure(state=tk.NORMAL)
            messagebox.showinfo("Info", f"Countdown finished!")

    def close_countdown(self):
        self.main.destroy()

if __name__ == "__main__":
    main = tk.Tk()
    app = AuctionServer(main)
    main.mainloop()
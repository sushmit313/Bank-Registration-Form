import tkinter as tk
from tkinter import messagebox

class BankRegistrationForm:
    def __init__(self, zedy):
        self.zedy = zedy
        self.zedy.title("Bank Registration Form")

        # Variables to store user inputs
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.confirm_password = tk.StringVar()
        self.phone = tk.StringVar()
        self.address = tk.StringVar()
        self.country = tk.StringVar()
        self.checkbox = tk.BooleanVar()

        # GUI components
        self.label_first_name = tk.Label(zedy, text="First Name :")
        self.entry_first_name = tk.Entry(zedy, textvariable=self.first_name)
        
        self.label_last_name = tk.Label(zedy, text="Last Name :")
        self.entry_last_name = tk.Entry(zedy, textvariable=self.last_name)

        self.label_email = tk.Label(zedy, text="Email :")
        self.entry_email = tk.Entry(zedy, textvariable=self.email)

        self.label_password = tk.Label(zedy, text="Password :")
        self.entry_password = tk.Entry(zedy, show="*", textvariable=self.password)

        self.label_confirm_password = tk.Label(zedy, text="Confirm Password :")
        self.entry_confirm_password = tk.Entry(zedy, show="*", textvariable=self.confirm_password)

        self.label_phone = tk.Label(zedy, text="Phone :")
        self.entry_phone = tk.Entry(zedy, textvariable=self.phone)

        self.label_address = tk.Label(zedy, text="Address :")
        self.entry_address = tk.Entry(zedy, textvariable=self.address)

        self.label_country = tk.Label(zedy, text="Country :")
        self.entry_country = tk.Entry(zedy, textvariable=self.country)

        self.checkbox = tk.Checkbutton(zedy, text="I agree to the terms and conditions", variable=self.checkbox)

        self.submit_button = tk.Button(zedy, text="Submit", command=self.submit_form)

        # Pack GUI components
        self.label_first_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_first_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_last_name.grid(row=1, column=1, padx=10, pady=5)

        self.label_email.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.label_password.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_password.grid(row=3, column=1, padx=10, pady=5)

        self.label_confirm_password.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_confirm_password.grid(row=4, column=1, padx=10, pady=5)

        self.label_phone.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_phone.grid(row=5, column=1, padx=10, pady=5)

        self.label_address.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_address.grid(row=6, column=1, padx=10, pady=5)

        self.label_country.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_country.grid(row=7, column=1, padx=10, pady=5)

        self.checkbox.grid(row=8, column=0, columnspan=2, pady=5)

        self.submit_button.grid(row=9, column=0, columnspan=2, pady=10)

    def submit_form(self):
        # Validate the form
        if not all([self.first_name.get(), self.last_name.get(),
                    self.email.get(), self.password.get(),
                    self.confirm_password.get(), self.phone.get(),
                    self.address.get(), self.country.get()]):
            messagebox.showerror("Error", "All fields must be filled")
            return

        if self.password.get() != self.confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match")
            return

        if not self.checkbox.get():
            messagebox.showerror("Error", "Please agree to the terms and conditions")
            return

        # If all validation passes, show a success message (you can implement further actions here)
        messagebox.showinfo("Success", "Registration Successful!")

# Create the main Tkinter window
zedy = tk.Tk()
app = BankRegistrationForm(zedy)

# Run the Tkinter event loop
zedy.mainloop()

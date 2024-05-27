from tkinter import *
from tkinter import ttk


def main():
    window = Tk()
    window.title("Address Entry Form")

    frame1 = ttk.Frame(relief=SUNKEN)
    frame2 = ttk.Frame(relief=SUNKEN)

    first_name_label = ttk.Label(text="First Name:", master=frame1)
    first_name_entry = ttk.Entry(master=frame1)
    first_name_label.grid(row=0, column=0, sticky="e")
    first_name_entry.grid(row=0, column=1, sticky="ew")

    last_name_label = ttk.Label(text="Last Name:", master=frame1)
    last_name_entry = ttk.Entry(master=frame1)
    last_name_label.grid(row=1, column=0, sticky="e")
    last_name_entry.grid(row=1, column=1, sticky="ew")

    address_line_1_label = ttk.Label(text="Address Line 1:", master=frame1)
    address_line_1_entry = ttk.Entry(master=frame1)
    address_line_1_label.grid(row=2, column=0, sticky="e")
    address_line_1_entry.grid(row=2, column=1, sticky="ew")

    address_line_2_label = ttk.Label(text="Address Line 2:", master=frame1)
    address_line_2_entry = ttk.Entry(master=frame1)
    address_line_2_label.grid(row=3, column=0, sticky="e")
    address_line_2_entry.grid(row=3, column=1, sticky="ew")

    city_label = ttk.Label(text="City:", master=frame1)
    city_entry = ttk.Entry(master=frame1)
    city_label.grid(row=4, column=0, sticky="e")
    city_entry.grid(row=4, column=1, sticky="ew")

    state_province_label = ttk.Label(text="State/Province:", master=frame1)
    state_province_entry = ttk.Entry(master=frame1)
    state_province_label.grid(row=5, column=0, sticky="e")
    state_province_entry.grid(row=5, column=1, sticky="ew")

    postal_code_label = ttk.Label(text="Postal Code:", master=frame1)
    postal_code_entry = ttk.Entry(master=frame1)
    postal_code_label.grid(row=6, column=0, sticky="e")
    postal_code_entry.grid(row=6, column=1, sticky="ew")

    country_label = ttk.Label(text="Country:", master=frame1)
    country_entry = ttk.Entry(master=frame1)
    country_label.grid(row=7, column=0, sticky="e")
    country_entry.grid(row=7, column=1, sticky="ew")

    frame1.pack(fill=X)
    window.mainloop()
    return


if __name__ == '__main__':
    main()

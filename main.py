import tkinter as tk

def convert():
    try:
        value = float(entry_value.get())
        from_unit = unit_var.get()
        to_unit = to_unit_var.get()

        # Conversion factors
        factors = {
            ('Miles', 'Kilometers'): 1.60934,
            ('Kilometers', 'Miles'): 0.621371,
            ('Meters', 'Feet'): 3.28084,
            ('Feet', 'Meters'): 0.3048,
            ('Yards', 'Meters'): 0.9144,
            ('Meters', 'Yards'): 1.09361,
        }

        result = value * factors[(from_unit, to_unit)]
        result_str = f"{value} {from_unit} is {result:.2f} {to_unit}"
        label_result.config(text=result_str)
    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Unit Converter")

# Create and place widgets
label_value = tk.Label(root, text="Value:")
label_value.grid(row=0, column=0, padx=10, pady=10)

entry_value = tk.Entry(root)
entry_value.grid(row=0, column=1, padx=10, pady=10)

label_from_unit = tk.Label(root, text="From Unit:")
label_from_unit.grid(row=1, column=0, padx=10, pady=10)

unit_options = ['Miles', 'Kilometers', 'Meters', 'Feet', 'Yards']
unit_var = tk.StringVar(value=unit_options[0])
from_unit_menu = tk.OptionMenu(root, unit_var, *unit_options)
from_unit_menu.grid(row=1, column=1, padx=10, pady=10)

label_to_unit = tk.Label(root, text="To Unit:")
label_to_unit.grid(row=2, column=0, padx=10, pady=10)

to_unit_var = tk.StringVar(value=unit_options[1])
to_unit_menu = tk.OptionMenu(root, to_unit_var, *unit_options)
to_unit_menu.grid(row=2, column=1, padx=10, pady=10)

btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.grid(row=3, columnspan=2, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=4, columnspan=2, pady=10)

# Start the main loop
root.mainloop()

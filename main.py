import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World App")

# Set the size of the window
root.geometry("300x200")

# Configure the grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a label widget with the text "Hello, World!"
label = tk.Label(root, text="Hello, World!", font=("Helvetica", 16))

# Position the label in the center of the grid
label.grid(row=0, column=0, sticky="nsew")

# Run the application
root.mainloop()


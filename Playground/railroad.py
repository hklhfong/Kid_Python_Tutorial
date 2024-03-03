import tkinter as tk
from tkinter import messagebox

def make_decision(decision):
    if decision == 'pull':
        messagebox.showinfo("Outcome", "You decided to pull the lever. The trolley switches tracks and kills one person, but you save five people.")
    else:
        messagebox.showinfo("Outcome", "You decided to do nothing. The trolley stays on its course and kills five people.")
    root.destroy()  # Close the window after the choice is made

# Set up the main window
root = tk.Tk()
root.title("Trolley Problem")

# Set up the scenario text
scenario_text = ("A runaway trolley is heading down the tracks towards five people tied up and unable to move. "
                 "You are standing next to a lever that controls the switch. If you pull the lever, the trolley will switch to another track, "
                 "but there is one person tied up on that track. Do you pull the lever to save five and sacrifice one, "
                 "or do nothing and allow the trolley to kill the five people?")
label = tk.Label(root, text=scenario_text, wraplength=400)
label.pack(pady=20)

# Set up the decision buttons
pull_button = tk.Button(root, text="Pull the lever", command=lambda: make_decision('pull'))
pull_button.pack(side=tk.LEFT, padx=20, pady=20)

do_nothing_button = tk.Button(root, text="Do nothing", command=lambda: make_decision('do nothing'))
do_nothing_button.pack(side=tk.RIGHT, padx=20, pady=20)

# Start the GUI event loop
root.mainloop()

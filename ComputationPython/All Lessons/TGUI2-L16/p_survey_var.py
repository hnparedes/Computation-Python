"""A programming language survey written in Python with Tkinter"""

import tkinter as tk

# Create the root window
root = tk.Tk()

# Set the title
root.title('CS Problem Solving and Solution Survey')

# Set the root window size
root.geometry('640x480+300+300')
root.resizable(False, False)

# Widgets

# Use a Label to show the title
title = tk.Label(
    root,
    text='Please take survey',
    font='Arial 16 bold',
    bg='black',
    fg='white'
)

# String vars for strings
name_var = tk.StringVar(root)
name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root, textvariable=name_var, justify='left')

# Boolean var for True/False
like_var = tk.BooleanVar()
language_inp = tk.Checkbutton(
    root, variable=like_var, text='Check this box if you like Python', anchor='w',
    justify='left'
)

# Int var for whole numbers
num_var = tk.IntVar(value=3)
num_label = tk.Label(text='How many hours do you work on Python homework a week?')
num_inp = tk.Spinbox(
    root,
    textvariable=num_var,
    from_=0,
    to=1000,
    increment=1
)

# OptionMenu with variables
language_var = tk.StringVar(value='Any')
language_label = tk.Label(
    root,
    text='What is the best programming language?'
)
language_choices = (
    'Any', 'C', 'C++', 'Java', 'Javascript', 'Python'
)
language__inp = tk.OptionMenu(
    root, language_var, *language_choices
)

# Label and radio buttons for expecting an A
python_label = tk.Label(root, text='Do you expect an A in COP2080?')
alpha_frame = tk.Frame(root)
python_var = tk.BooleanVar()
alpha_yes_inp = tk.Radiobutton(
    alpha_frame,
    text='Yes',
    value=True,
    variable=python_var
)
python_no_inp = tk.Radiobutton(
    alpha_frame,
    text='If not, try forming study groups',
    value=False,
    variable=python_var
)

# New OptionMenu for CS concentration
concentration_var = tk.StringVar(value='Select concentration')
concentration_label = tk.Label(
    root,
    text='What is your concentration?'
)
concentration_choices = (
    'Adv Topics', 'Software Engineering', 'Cyber Security',
    'Game Development', 'AI', 'Big Data', 'Autonomous Systems'
)
concentration_inp = tk.OptionMenu(
    root, concentration_var, *concentration_choices
)

# Haiku section
python_haiku_label = tk.Label(root, text='Write a haiku about Python')
python_haiku_inp = tk.Text(root, height=3)

# Submit button and output line
submit_btn = tk.Button(root, text='Submit Survey')
output_var = tk.StringVar(value='')
output_line = tk.Label(
    root,
    textvariable=output_var,
    anchor='w',
    justify='left'
)

# Geometry Management #

# Title
title.grid(columnspan=2)

# Name label and input
name_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
name_inp.grid(row=1, column=1, sticky='we')

# Like Python Checkbutton
language_inp.grid(row=2, columnspan=2, sticky='we')
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))

# Language OptionMenu
language_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
language__inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)

# Expecting an A radio buttons
python_label.grid(row=8, columnspan=2, sticky=tk.W)
alpha_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
python_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
alpha_frame.grid(row=9, columnspan=2, sticky=tk.W)

# Concentration OptionMenu
concentration_label.grid(row=6, columnspan=2, sticky=tk.W)
concentration_inp.grid(row=7, columnspan=2, sticky=tk.W + tk.E, padx=25)

# Haiku label and input
python_haiku_label.grid(row=10, sticky=tk.W)
python_haiku_inp.grid(row=11, columnspan=2, sticky='NSEW')

# Submit button and output
submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky='NSEW')

# Configure grid columns and rows
root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

# Behavior on submit


def on_submit():
    """Run when the user submits the form"""
    name = name_var.get()
    number = num_var.get()
    language_ = language_var.get()
    python_liker = like_var.get()
    python_user = python_var.get()
    concentration = concentration_var.get()
    haiku = python_haiku_inp.get('1.0', tk.END)

    # Output message
    message = f'Thanks for taking the survey, {name}.\n'
    if not python_liker:
        message += "You should give Python another chance!\n"
    else:
        message += f'Enjoy studying {number} hours on Python vs {language_} \n'

    if python_user:
        message += 'Enjoy programming Python!'
    else:
        message += 'May you successfully avoid programming in Python'

    if concentration != 'Select concentration':
        message += f'\n{concentration} is a great concentration!\n'

    if haiku.strip():
        message += f'\n\nYour Haiku:\n{haiku}'

    output_var.set(message)


# Configure submit button
submit_btn.configure(command=on_submit)

# Execute App
root.mainloop()

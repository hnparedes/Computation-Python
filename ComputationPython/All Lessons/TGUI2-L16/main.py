# Tkinter Basics

# p_survey_var.py
# Create the root window
# root = tk.Tk()

# set the title
# root.title('CS Problem-Solving and Solution Survey’)

# set the root window size
# root.geometry('640x480+300+300')
# root.resizable(False, False)

# title = tk.Label(root, text='Please take survey', font=('Arial 16 bold'),
#                  bg='black', fg='white')

# Tkinter Stringvar()

# Use string vars for strings
# name_var = tk.StringVar(root)
# name_label = tk.Label(root, text='What is your name?')
# name_inp = tk.Entry(root, textvariable=name_var)

# Use boolean var for True/False
# like_var = tk.BooleanVar()
# language_inp = tk.Checkbutton(root, variable=like_var,
#                               text='Check this box if you like Python')

# Use int var for whole numbers
# Value can set a default
# num_var = tk.IntVar(value=3)
# num_label = tk.Label(text='How many hours do you work on Python homework a week?')

# note that even with an intvar, the key is still 'textvariable'
# num_inp = tk.Spinbox(root, textvariable=num_var, from_=0, to=1000, increment=1)

# Tkinter OptionMenu

# Use OptionMenu with variables instead of Listbox
# language_var = tk.StringVar(value='Any')
# language_label = tk.Label(root, text='What is the best programming language?’ )
# language_choices = ('Any', 'C', 'C++', 'Java', 'Javascript', 'Python’)
# language__inp = tk.OptionMenu(root, language_var, *language_choices)
# python_label = tk.Label(root, text='Do you expect an A in COP2080?')

# Use a Frame to keep widgets together
# alpha_frame = tk.Frame(root)
# python_var = tk.BooleanVar()

# The radio buttons are connected by using the same variable
# alpha_yes_inp = tk.Radiobutton(alpha_frame, text='Yes', value=True, variable=python_var)

# On Submit Function
# def on_submit():
"""To be run when the user submits the form"""

# Vars all use 'get()' to retreive their variables
# name = name_var.get()
# Because of IntVar, .get() will try to convert
# the contents of num_var to int.
# try:
#  number = num_var.get()
# except tk.TclError:
#  number = 10000

# OptionMenu makes things simple
# language_ = language_var.get()

# Checkbutton and Radiobutton values
# python_liker = like_var.get()
# python_user = python_var.get()

# Text widgets require a range
# haiku = python_haiku_inp.get('1.0', tk.END)

# Build gui_scrape.py

# gui_scrape.py
# from tkinter import *
# from tkinter import ttk,filedialog,messagebox

# f __name__ == "__main__": execute logic if run directly
# _root = Tk() instantiate instance of Tk class
# _root.title('Scrape app')

# _mainframe = ttk.Frame(_root, padding='5 5 5 5 ') root is parent of frame
# _mainframe.grid(row=0, column=0, sticky=("E", "W", "N", "S")) placed on first row,col of parent
# frame can extend itself in all cardinal directions
# _url_frame = ttk.LabelFrame(_mainframe, text='URL', padding='5 5 5 5') label frame
# _url_frame.grid(row=0, column=0, sticky=("E","W")) only expands E W
# _url_frame.columnconfigure(0, weight=1)
# _url_frame.rowconfigure(0, weight=1) behaves when resizing

# Frames of gui_scrape.py

# _url_frame = ttk.LabelFrame(
# _mainframe, text='URL', padding='5 5 5 5') label frame
# _url_frame.grid(row=0, column=0, sticky=("E","W")) only expands E W
# _url_frame.columnconfigure(0, weight=1)
# _url_frame.rowconfigure(0, weight=1) behaves when resizing

# _url = StringVar()
# _url.set('http://localhost:8000') sets initial value of _url
# _url_entry = ttk.Entry(
# _url_frame, width=40, textvariable=_url) text box
# _url_entry.grid(row=0, column=0, sticky=(E, W, S, N), padx=5)

# grid mgr places object at position
# _fetch_btn = ttk.Button(_url_frame, text='Fetch info', command=fetch_url) create button

# fetch_url() is callback for button press
# _fetch_btn.grid(row=0, column=1, sticky=W, padx=5)

# img_frame contains Lisbox and Radio Frame
# _img_frame = ttk.LabelFrame(_mainframe, text='Content', padding='9 0 0 0')
# _img_frame.grid(row=1, column=0, sticky=(N, S, E, W))

# Listbox of gui_scrape.py

# Set _img_frame as parent of Listbox and _images is variable tied to
# _images = StringVar()
# _img_listbox = Listbox(_img_frame, listvariable=_images, height=6, width=25)
# _img_listbox.grid(row=0, column=0, sticky=(E, W), pady=5)

# Scrollbar can move vertical
# _scrollbar = ttk.Scrollbar(_img_frame, orient=VERTICAL, command=_img_listbox.yview)
# _scrollbar.grid(row=0, column=1, sticky=(S, N), pady=6)
# _img_listbox.configure(yscrollcommand=_scrollbar.set)

# Listbox occupies (0,0) on _img_frame.
# Scrollbar occupies (0,1) so _radio_frame goes to (0,2)
# _radio_frame = ttk.Frame(_img_frame)
# _radio_frame.grid(row=0, column=2, sticky=(N, S, W, E))

# Labels and json

# _choice_lbl = ttk.Label(_radio_frame, text="Choose how to save images")
# _choice_lbl.grid(row=0, column=0, padx=5, pady=5)
# _save_method = StringVar()
# _save_method.set('img')

# Radiobutton connected to _save_method variable
# Know which button is selected by checking value

# _img_only_radio = ttk.Radiobutton(_radio_frame, text='As Images', variable=_save_method, value='img')
# _img_only_radio.grid(row=1, column=0,padx=5, pady=2, sticky="W")
# _img_only_radio.configure(state='normal')
# _json_radio = ttk.Radiobutton(_radio_frame, text='As JSON', variable=_save_method, value='json')
# _json_radio.grid(row=2, column=0, padx=5, pady=2, sticky="W")

# Buttons

# _scrape_btn = ttk.Button(_mainframe, text='Scrape!', command=save)
# _scrape_btn.grid(row=2, column=0, sticky=E, pady=5)

# _status_frame = ttk.Frame(_root, relief='sunken', padding='2 2 2 2')
# _status_frame.grid(row=1, column=0, sticky=("E", "W", "S"))
# _status_msg = StringVar() need modified when update status text
# _status_msg.set('Tye a URL to start scraping...')
# _status= ttk.Label(_status_frame, textvariable=_status_msg, anchor=W)
# _status.grid(row=0, column=0, sticky=(E, W))

# _root.mainloop() listens for events, blocks any code that comes after it

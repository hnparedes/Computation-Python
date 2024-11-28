# Introducting TK and Tkinter

# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)

#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()

# Create a directory for Web Server
# <div class="container-fluid">
#   <div class="image">
#     <img src="img/cupcakes.jpg" alt="rows of cupcakes" class="img-fluid">
#   </div>
#   <div class="text">

# Create scrape.py
# scrape.py
# import argparse
# import base64
# import json
# from pathlib import Path
# from bs4 import BeautifulSoup
# import requests

# Building scraper.py
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Scrape a webpage.')
#     parser.add_argument('-t', '--type', choices=['all', 'png', 'jpg'], default='all',
#                         help='The image type we want to scrape.')

#     parser.add_argument('-f', '--format', choices=['img', 'json'], default='img',
#                         help='The format images are saved to.')
#     parser.add_argument('url', help='The URL we want to scrape for images.')
#     args = parser.parse_args()
#     scrape(args.url, args.format, args.type)

# argparse
# Building scraper.py
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Scrape a webpage.')
#     parser.add_argument('-t', '--type', choices=['all', 'png', 'jpg'], default='all',
#     help='The image type we want to scrape.')

#     parser.add_argument('-f', '--format', choices=['img', 'json'], default='img',
#     help='The format images are saved to.')

#     parser.add_argument('url', help='The URL we want to scrape for images.')

#     args = parser.parse_args()
#     scrape(args.url, args.format, args.type)

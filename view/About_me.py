from tkinter import *
from PIL import Image, ImageTk

class AboutMe:

    def __init__(self):

        self.win = Toplevel()
        self.win.title("About Me")

        frame = Frame(self.win, padx=10, pady=10)
        frame.pack()

        image = Image.open("images\mahditermeh.jpg")
        image = image.resize((150, 150))
        self.photo = ImageTk.PhotoImage(image)
        img_label = Label(frame, image=self.photo)
        img_label.grid(row=0, column=0, padx=10)

        about_text = """Hi, I'm Mahdi Termeh, a computer engineering student.
This project was part of a Python class I took outside the university.
 
It gave me a better and deeper understanding of concepts like object-oriented programming, working with databases, and real-world project structure.
        
I’d like to keep working on similar projects in the future to improve my skills and learn even more through practice.
        """

        text_label = Label(frame, text=about_text, justify="left", wraplength=300, font=("Arial", 10))
        text_label.grid(row=0, column=1, sticky="w")

        self.win.mainloop()
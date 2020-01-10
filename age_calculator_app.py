# This App is to calculate the calculate and display the CURRENT age of a person.
from PIL import Image, ImageTk
import datetime
import tkinter as tk
from io import BytesIO
import requests


# create frame (initialize frame)
window = tk.Tk()

# create frame (geometry)
window.geometry("400x500")

# Set the title of the frame
window.title("Age Calculator App")

# Image link url
img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTqPYAgPe293fJLiJw-0wiXH6hkvfqBM7_pZnXiVRSV3halljtZ"


# adding labels
person_label = tk.Label(text="Name")
person_label.grid(column=0, row=1)

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=2)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=3)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=4)

person_entry = tk.Entry()
person_entry.grid(column=1, row=1)

year_entry = tk.Entry()
year_entry.grid(column=1, row=2)

month_entry = tk.Entry()
month_entry.grid(column=1, row=3)

day_entry = tk.Entry()
day_entry.grid(column=1, row=4)

def calculate_age():
    person = Person(person_entry.get(), datetime.date(int(year_entry.get()),
                                          int(month_entry.get()),
                                          int(day_entry.get())))
    text_answer = tk.Text(master=window, height=20, width=30)
    text_answer.grid(column=1, row=6)
    answer_text = "{name} is currently {age} years old!".format(name=person_entry.get(), age=person.age())
    text_answer.insert(tk.END, answer_text)

calculate_button = tk.Button(text="Calculate Now", command=calculate_age)
calculate_button.grid(column=1, row=5)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

#chris = Person("Chris", datetime.date(1940, 8, 20))

# ***** To Open and Load Image Locally, Uncomment the 5 lines of code below *****

#image = Image.open('') # <-- Add path of image in ''
#image.thumbnail((100, 100), Image.ANTIALIAS) # Image resolution specifications
#photo = ImageTk.PhotoImage(image) # To turn into a tkinter image
#label_image = tk.Label(image=photo) # A label to store images
#label_image.grid(column=1, row=0)

# Method 2 - ***** Open and load an Image from the Web *****
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel = tk.Label(window, image=img)
panel.grid(column=1, row=0)


window.mainloop()









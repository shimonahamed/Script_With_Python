from tkinter import Label, Tk

import time

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("1005x250")
app_window.resizable(1,1)

text_font= ("Boulder", 78, 'bold')

background = "#f2e750"

foreground="#363529"

border_width = 45
label = Label(app_window, font=text_font, bg=background, fg=foreground )
label.grid(row=0, column=1)

def digital_clock():
    name=("CLOCK:")
    name2 = ("DATE:")
    time_live = time.strftime(name+"%I:%M:%S %p")
    day_live = time.strftime(name2 + "%m/%d/%Y")
    label.config(text=time_live +'\n'+ day_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
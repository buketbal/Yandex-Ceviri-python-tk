# coding=utf-8
import os
from Tkinter import *
from yandex_translate import YandexTranslate
import clipboard

# Copied string
Text = clipboard.paste()

# Yandex api
translate = YandexTranslate('Your Yandex Api Key')

Translated = ""

if Text is not None:
    Translated = translate.translate(Text, 'tr')['text'][0]

message = """
%s
---
%s
""" % (Text, Translated)


# User interface
class Application(Frame):
    def widgets(self):
        self.LABEL = Label(self)
        self.LABEL["text"] = message
        self.LABEL["wraplength"] = 200
        self.LABEL["fg"] = "black"
        self.LABEL.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.widgets()


if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("")
    app.master.geometry("200x200+0+0")
    app.master.maxsize(width=300, height=300)
    app.mainloop()

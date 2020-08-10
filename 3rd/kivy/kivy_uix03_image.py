# coding:utf-8

from kivy.uix.image import Image
from kivy.app import App

class Program(App):

    def build(self):
        resim = Image(source = "resim.jpg")

        return resim

Program().run()

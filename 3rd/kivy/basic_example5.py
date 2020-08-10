#!/usr/bin/env python
# -*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

# gerekli sınıfları import ettik

class Program(App):
    def build(self):

        duzen = FloatLayout() # pencere düzenimizi tanımladık

        buton = Button(text = "Merhaba",
                                size_hint = (.1,.1),
                                pos = (10,10))

        duzen.add_widget(buton) # butonumuzu yerleştiriyoruz

        return duzen


Program().run()

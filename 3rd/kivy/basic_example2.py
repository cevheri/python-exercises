# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label


class Program(App):
    def on_start(self):
        self.title = "Welcome"
        # bir takım işlemler...

    def on_stop(self):
        # Uygulama kapatılırken...
        pass

    def on_pause(self):
        # Uygulama arkaplana alınırken...
        # Burda return True yapmanız gerekiyor
        return True

    def on_resume(self):
        # Tekrar giriş yapıldığında yazımızı değiştiriyoruz
        self.label.text = "Programa tekrar hoşgeldiniz"

    def build(self):
        self.label = Label(text="Merhaba Dünya")
        return self.label


Program().run()

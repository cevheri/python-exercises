# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Program(App):

        def build(self):
                self.govde = BoxLayout(orientation = "vertical")

                self.yazi = Label(text = "Bildiri Ekranı")
                self.buton = Button(text = "Tıkla",size_hint_y = .3)

                self.buton.bind(on_press = self.press)
                # Basılma olayını self.press fonksiyonuna bağladık
                # Yani butona basıldığı anda self.press fonksiyonumuz çalışacaktır

                self.buton.bind(on_release = self.release)
                # Bırakılma olayını self.release fonksiyonuna bağladık
                # Yani buton bırakıldığı anda self.release fonksiyonumuz çalışacaktır

                self.govde.add_widget(self.yazi)
                self.govde.add_widget(self.buton)

                return self.govde

        def press(self,nesne):
                self.yazi.text = "Buton'a basıldı"

        def release(self,nesne):
                self.yazi.text = "Buton bırakıldı"


Program().run()

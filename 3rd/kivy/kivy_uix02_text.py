# coding: utf-8

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Program(App):
    def build(self):

        self.anaDuzen = BoxLayout(orientation = "vertical") # Elemanların hepsini tutan ana pencere düzenimiz

        self.ilkSatir = BoxLayout()
        self.ikinciSatir = BoxLayout()

        self.nick = Label(text = "Nick")
        self.nickKutu = TextInput(multiline = False)

        self.sifre = Label(text = "Şifre")
        self.sifreKutu = TextInput(multiline = False,
                              password = True,
                              password_mask = "?")

        self.buton = Button(text = "Giriş Yap")
        self.buton.bind(on_press = self.kontrol) # Butonumuza tıklama olayı ekledik


        self.ilkSatir.add_widget(self.nick)
        self.ilkSatir.add_widget(self.nickKutu)

        self.ikinciSatir.add_widget(self.sifre)
        self.ikinciSatir.add_widget(self.sifreKutu)

        # Şimdi hepsini ana düzene yerleştiriyoruz

        self.anaDuzen.add_widget(self.ilkSatir)
        self.anaDuzen.add_widget(self.ikinciSatir)
        self.anaDuzen.add_widget(self.buton)

        return self.anaDuzen

    def kontrol(self,event = None):
        if(self.nickKutu.text == "admin" and self.sifreKutu.text == "12345"):
            print("Giriş Başarılı")

        else:
            print("Hatalı Giriş")


Program().run()


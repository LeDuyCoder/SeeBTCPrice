from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.layout import Layout
from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock
import requests

def getPriceBTC():
    url = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")
    text = url.json()
    prite = text["data"]["amount"]
    return prite

def updatePriceBTC(self):
    ScreenMain().UpdatePrice(ScreenMain)

Window.size = (300,200)
check = 0

class ScreenMain(Widget):
    number = 0
    price = ObjectProperty(number)
    red = NumericProperty(0)
    green = NumericProperty(0)
    blue = NumericProperty(1)
    def getPrice(self):
        print(price)

    def UpdatePriceBTC(self, arg):
        global check
        self.price = 0+float(getPriceBTC())
        if float(getPriceBTC()) != float(check):
            if float(getPriceBTC()) >= float(check):
                self.red = 26/255
                self.green = 255/255
                self.blue = 26/255
            else:
                self.red = 1
                self.green = 0
                self.blue = 0
            check = float(getPriceBTC())

        #print(getPriceBTC())

    def UpdatePrice(self, cls):
        self.price += 1
        Clock.schedule_interval(self.UpdatePriceBTC, 60/60.)
        self.price = 0+float(getPriceBTC())

class AppBTC(MDApp):
    def build(self):
        return Builder.load_file("BTC.kv")

if __name__ == "__main__":
    AppBTC().run()
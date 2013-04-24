import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.app import App
#from kivy.interactive import InteractiveLauncher

import mysql.connector

cnx = mysql.connector.connect(user='karanvirsngh', password='ether0110',
                              host='SQL09.FREEMYSQL.NET',
                              database='karant')

cursor = cnx.cursor()

cursor.execute("SELECT * FROM Writers")
karanvir="oi"
print cursor
for Name in cursor:
    print Name[1]
    karanvir=Name[1]

class ProductDetailScreen(Widget):
    pass

class ProductScreen(Widget):
    pass

class ProductFilterScreen(Widget):
    pass

class MainScreen(Widget):
    def show_product_screen(self):
        return ProductScreen()

    def on_pause(self):
        return True

class ArtofBeerApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    ArtofBeerApp().run()

#interactiveLauncher = InteractiveLauncher(ArtofBeerApp()).run()
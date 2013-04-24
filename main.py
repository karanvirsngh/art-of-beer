import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, SwapTransition, WipeTransition, FadeTransition, SlideTransition

#from kivy.interactive import InteractiveLauncher

#import mysql.connector

#cnx = mysql.connector.connect(user='karanvirsngh', password='ether0110',
                              #host='SQL09.FREEMYSQL.NET',
                              #database='karant')

#cursor = cnx.cursor()

#cursor.execute("SELECT * FROM Writers")
#karanvir="oi"
#print cursor
#for Name in cursor:
#    print Name[1]
#    karanvir=Name[1]

#sm.add_widget(ProductDetailScreen(name='Product_Detail_Screen'))
#sm.add_widget(ProductFilterScreen(name='Product_Filter_Screen'))
#sm.current = 'Main_Screen'
# Create the manager
#sm = ScreenManager()
# Add few screens
#for i in xrange(4):
 #   screen = Screen(name='Title %d' % i)
 #   sm.add_widget(screen)

# By default, the first screen added into the ScreenManager will be
# displayed. Then, you can change to another screen:

# Let's display the screen named 'Title 2'
# The transition will be automatically used.
#sm.current = 'Title 2'
Builder.load_string('''
#:kivy 1.0.9

<MainScreen>:
    FloatLayout:
        size: root.width, root.height
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                source: 'images/main_background.jpg'
                size: root.size
        
        Button:
            color: (0, 0, 0, 1)
            italic: True
            text: 'Start Exporing Art of Beer'
            font_size: '20sp'
            background_color: (1, 1, 1, .3)
            color: (0, 0, 0, 1)
            on_press: root.on_click()
           
<ProductScreen>:
    FloatLayout:
        size: root.width, root.height
        canvas:
            Color:
                rgb: 0, 0, 1
            Rectangle:
                size: root.size
        ListView:
            size_hint: .8, .8
        Button:
            text: 'Go back'
            size_hint: None, None
            size: 150, 50
            on_press: root.on_click()
''')
class ProductScreen(Screen):
    def on_click(self):
        sm.transition = SlideTransition(direction='left')
        sm.current = 'Main_Screen'
        #sm.transition = SlideTransition(direction="up")


#class ProductDetailScreen(Screen):
#    pass

#class ProductFilterScreen(Screen):
#    pass

class MainScreen(Screen):
    def on_click(self):
        sm.transition = WipeTransition(direction='right')
        sm.current = 'Product_Screen'

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='Main_Screen'))
sm.add_widget(ProductScreen(name='Product_Screen'))
#sm.add_widget(Product_Detail_Screen(name='Product_Detail_Screen'))
#sm.add_widget(ProductFilterScreen(name='ProductFilterScreen'))

class ArtofBeerApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    ArtofBeerApp().run()

#interactiveLauncher = InteractiveLauncher(ArtofBeerApp()).run()
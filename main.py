import kivy
import os
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation
from kivy.adapters.listadapter import ListAdapter
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListItemButton, ListView, SelectableView
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
                rgb: 1, 0, 0
            Rectangle:
                size: root.size

        Button:
            text: 'Go back'
            size_hint: None, None
            size: 150, 50
            on_press: root.on_click()
        Button:
            text: 'Product Detail'
            size_hint: None, None
            size: 250, 50
            pos_hint: {'x':0.8, 'y':0.0}
            on_press: root.click_product_detail_screen()


[ProductItem@SelectableView+BoxLayout]:
    size_hint_y: ctx.size_hint_y
    size_hint_x: ctx.size_hint_x
    height: ctx.height
    width: ctx.width
    Image:
        source: ctx.source
        size: root.size
    Label:
        text: ctx.text
    #ListItemButton:
    #    text: ctx.text
    #    is_selected: ctx.is_selected





<ProductDetailScreen>:
    FloatLayout:
        size: root.width, root.height
        canvas:
            Color:
                rgb: 0.3, 0.3, 0.3
            Rectangle:
                size: root.size
        Button:
            text: 'Product Screen'
            size_hint: None, None
            size: 250, 50
            pos_hint: {'x':0.0, 'y':0.0}
            on_press: root.click_product_screen()

<ProductFilterScreen>:
    FloatLayout:
        size: root.width, root.height
        canvas:
            Color:
                rgb: 1, 0, 0
            Rectangle:
                size: root.size
        Button:
            text: 'Main Menu'
            size_hint: None, None
            size: 250, 50
            pos_hint: {'x':0.0, 'y':0.0}
            on_press: root.click_main_screen()
        Button:
            text: 'Product List Screen'
            size_hint: None, None
            size: 250, 50
            pos_hint: {'x':0.8, 'y':0.0}
            on_press: root.click_product_list_screen()
''')

class ProductScreen(Screen):
    
    def __init__(self, **kwargs):
        super(ProductScreen, self).__init__(**kwargs)

        data = { str(i): {'text': str(i) } for i in xrange(100) }
        #data = { str(i): {'text': str(i), 'is_selected': False} for i in xrange(100) }
        list_item_args_converter = lambda row_index, rec: {'text': rec['text'],
                                #'is_selected': rec['is_selected'],
                                'size_hint_y': None,
                                'size_hint_x': None,
                                'height': 100,
                                'width': 100,
                                'source': 'images/Batch19.jpg'}

        list_adapter = ListAdapter(data=data,
                           template='ProductItem',
                           args_converter=list_item_args_converter)

        dict_adapter = DictAdapter(sorted_keys=[str(i) for i in xrange(100)],
                           data=data,
                           args_converter=list_item_args_converter,
                           template='ProductItem')
        list_view = ListView(adapter=dict_adapter)
        list_view.size_hint = (0.5,1.0)
        list_view.pos_hint = {'x':.3, 'y':0.0}

        self.add_widget(list_view)

        #Get all image file name in /images/
        image_name_list = []
        for i in os.listdir('./images/'):
            image_name_list.append(i)
        #First Horizontal Scrollable View
        layout = GridLayout(cols=30, spacing=10, size_hint_x=None)
        #Make sure the height is such that there is something to scroll.
        layout.bind(minimum_width=layout.setter('width'))
        for file_name in image_name_list:
            float_layout = FloatLayout(size_hint_x=None, size_hint_y=None, height=150, width=150)
            #image_view = Image(source='im')
            btn = Button(text=file_name, size_hint_y=None, size_hint_x=None, height=150, width=150)
            layout.add_widget(btn)
        scroll_view_one = ScrollView(size_hint=(1.0, None), height=150, pos_hint={'x':0.0,'y':0.3})
        scroll_view_one.do_scroll_y=False
        scroll_view_one.do_scroll_x=True
        scroll_view_one.add_widget(layout)
        self.add_widget(scroll_view_one)
        #Second Horizontal Scrollable View
        #layout_two

    def on_click(self):
        sm.transition = WipeTransition(direction='left')
        sm.current = 'Product_Filter_Screen'
        #sm.transition = SlideTransition(direction="up")
    def click_product_detail_screen(self):
        sm.transition = FadeTransition()
        sm.current = 'Product_Detail_Screen'

class ProductDetailScreen(Screen):

    def __init__(self, **kwargs):
        super(ProductDetailScreen, self).__init__(**kwargs)
        button = Button(text='hi', size=(50, 50), size_hint=(None, None), pos_hint={'x':0.3,'y':0.3})
        self.add_widget(button)

    def animate(self):
        anim = Animation(x=100, y=100)
        anim.start(button)
        #self.add_widget(button)

    def click_product_screen(self):
            sm.transition = WipeTransition(direction='left')
            sm.current = 'Product_Screen'

class ProductFilterScreen(Screen):
    def __init__(self, **kwargs):
        super(ProductFilterScreen, self).__init__(**kwargs)

    def click_main_screen(self):
        sm.transition = WipeTransition(direction='left')
        sm.current = 'Main_Screen'

    def click_product_list_screen(self):
        sm.transition = WipeTransition(direction='right')
        sm.current = 'Product_Screen'

class MainScreen(Screen):
    def on_click(self):
        sm.transition = WipeTransition(direction='right')
        sm.current = 'Product_Filter_Screen'

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='Main_Screen'))
sm.add_widget(ProductScreen(name='Product_Screen'))
sm.add_widget(ProductDetailScreen(name='Product_Detail_Screen'))
sm.add_widget(ProductFilterScreen(name='Product_Filter_Screen'))

class ArtofBeerApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    ArtofBeerApp().run()

#interactiveLauncher = InteractiveLauncher(ArtofBeerApp()).run()
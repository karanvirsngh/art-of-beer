import kivy
import os
import time
import re
import sys
import sqlite3

kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation
from kivy.adapters.listadapter import ListAdapter
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListItemButton, ListView, SelectableView
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, SwapTransition, WipeTransition, FadeTransition, SlideTransition

conn = sqlite3.connect("aob.db") # or use :memory: to put it in RAM
 
cursor = conn.cursor()

if(len(sys.argv)>1):
    if(sys.argv[1]=="create"):
        #create a table
        cursor.execute("""CREATE TABLE beers
                         (name text, des text,\
                         dark boolean, light boolean,\
                         can boolean, bottle boolean,\
                         craft boolean, domestic boolean, import boolean, specialty boolean,\
                         sports boolean, dining boolean, party boolean, club boolean)\
                        """)
        # insert some data
        cursor.execute("INSERT INTO beers VALUES ('Molson Canadian Light','Molson Canadian Light','1','0','1','0','0','0','0','1','1','1','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Molson Ice','Molson Ice','0','1','0','1','0','0','0','1','0','1','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Sparks Lemonade','Sparks Lemonade','1','0','1','0','0','0','0','1','1','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Redds Apple Ale','Redds Apple Ale','1','0','1','0','0','0','0','1','1','1','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Sparks','Sparks','0','1','0','1','0','0','0','1','0','1','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Third Shift','Third Shift','1','0','0','1','0','0','0','1','1','0','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Sparks Iced Tea','Sparks Iced Tea','1','0','0','1','0','0','0','1','1','1','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Fosters Ale','Fosters Ale','0','1','0','1','0','0','0','1','0','0','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Sharps','Sharps','0','1','1','0','0','0','0','1','0','1','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Sparks Blackberry','Sparks Blackberry','0','1','1','0','0','0','0','1','1','1','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Molson Canadian','Molson Canadian','0','1','0','1','0','0','0','1','1','0','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Molson Golden','Molson Golden','0','1','0','1','0','0','0','1','0','0','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Molson XXX','Molson XXX','1','0','0','1','0','0','0','1','0','1','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Fosters','Fosters','0','1','0','1','0','0','0','1','1','1','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Coors NA','Coors NA','1','0','0','1','0','0','0','1','1','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Keystone','Keystone','0','1','1','0','0','1','0','0','0','1','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Steel Reserve','Steel Reserve','0','1','1','0','0','1','0','0','1','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Icehouse','Icehouse','0','1','0','1','0','1','0','0','0','0','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Miller Chill','Miller Chill','0','1','1','0','0','1','0','0','1','1','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Hamms','Hamms','0','1','1','0','0','1','0','0','0','0','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Miller 64','Miller 64','1','0','1','0','0','1','0','0','1','1','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Mickeys Ice','Mickeys Ice','1','0','0','1','0','1','0','0','0','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Keystone Ice','Keystone Ice','0','1','1','0','0','1','0','0','1','1','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Keystone Light','Keystone Light','1','0','1','0','0','1','0','0','0','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Miller High Life Light','Miller High Life Light','0','1','0','1','0','1','0','0','0','0','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('MGD','MGD','0','1','1','0','0','1','0','0','1','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Steel Reserve Six','Steel Reserve Six','0','1','1','0','0','1','0','0','0','0','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Miller High Life','Miller High Life','0','1','1','0','0','1','0','0','0','1','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Olde English','Olde English','1','0','0','1','0','1','0','0','0','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Mils Best Ice','Mils Best Ice','0','1','0','1','0','1','0','0','0','1','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Steel Reserve Triple','Steel Reserve Triple','1','0','1','0','0','1','0','0','0','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Magnum','Magnum','0','1','0','1','0','1','0','0','1','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Coors Light','Coors Light','0','1','1','0','0','1','0','0','0','0','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('HG800','HG800','0','1','0','1','0','1','0','0','0','0','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Extra Gold','Extra Gold','0','1','0','1','0','1','0','0','1','1','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Miller Lite','Miller Lite','0','1','0','1','0','1','0','0','0','0','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Mils Best Light','Mils Best Light','0','1','0','1','0','1','0','0','0','0','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Mickeys','Mickeys','0','1','0','1','0','1','0','0','1','1','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Red Dog','Red Dog','0','1','0','1','0','1','0','0','0','0','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Coors Banquet','Coors Banquet','0','1','0','1','0','1','0','0','1','1','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Mils Best','Mils Best','0','1','0','1','0','1','0','0','0','0','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Killians Red','Killians Red','1','0','1','0','1','0','0','0','1','1','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Weinhard Redwood Flats Amber','Weinhard Redwood Flats Amber','1','0','1','0','1','0','0','0','0','1','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Leines Creamy Dark','Leines Creamy Dark','0','1','0','1','1','0','0','0','0','0','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Leines Red Lager','Leines Red Lager','1','0','1','0','1','0','0','0','0','1','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Leines Sunset Wheat','Leines Sunset Wheat','0','1','1','0','1','0','0','0','0','0','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Blue Moon Summer Honey','Blue Moon Summer Honey','0','1','0','1','1','0','0','0','1','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Leines Fireside Nut Brown','Leines Fireside Nut Brown','0','1','0','1','1','0','0','0','0','1','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Leines Classic Amber','Leines Classic Amber','0','1','0','1','1','0','0','0','1','0','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Leines Honey Weiss','Leines Honey Weiss','1','0','1','0','1','0','0','0','1','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Leines Oktoberfest','Leines Oktoberfest','1','0','1','0','1','0','0','0','0','1','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Lein Light','Lein Light','0','1','0','1','1','0','0','0','0','0','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Blue Moon Harvest Pumpkin','Blue Moon Harvest Pumpkin','1','0','1','0','1','0','0','0','1','1','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Blue Moon Belgian White','Blue Moon Belgian White','1','0','0','1','1','0','0','0','0','1','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Leines Berry Weiss','Leines Berry Weiss','0','1','1','0','1','0','0','0','1','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Blue Moon Spring Blonde','Blue Moon Spring Blonde','0','1','0','1','1','0','0','0','0','1','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Blue Moon Winter Abbey','Blue Moon Winter Abbey','0','1','0','1','1','0','0','0','1','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Lein','Lein','0','1','0','1','1','0','0','0','1','1','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Weinhard Woodland Pass IPA','Weinhard Woodland Pass IPA','0','1','0','1','1','0','0','0','0','0','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Weinhard Private Reserve','Weinhard Private Reserve','0','1','1','0','1','0','0','0','0','1','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Coors Winterfest','Coors Winterfest','1','0','0','1','1','0','0','0','0','0','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Batch 19','Batch 19','1','0','1','0','1','0','0','0','1','1','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Leines Summer Shandy','Leines Summer Shandy','0','1','1','0','1','0','0','0','0','1','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Tyskie','Tyskie','0','1','0','1','0','0','1','0','1','0','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Peroni','Peroni','1','0','1','0','0','0','1','0','0','0','1','0')")
        cursor.execute("INSERT INTO beers VALUES ('Lech','Lech','1','0','1','0','0','0','1','0','0','0','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Aguila','Aguila','0','1','0','1','0','0','1','0','0','1','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Cusquena','Cusquena','1','0','0','1','0','0','1','0','1','0','0','1')")
        cursor.execute("INSERT INTO beers VALUES ('Cristal','Cristal','1','0','0','1','0','0','1','0','0','1','1','1')")
        cursor.execute("INSERT INTO beers VALUES ('Pilsner Urquell','Pilsner Urquell','0','1','0','1','0','0','1','0','1','0','0','0')")
        cursor.execute("INSERT INTO beers VALUES ('Grolsch Premium','Grolsch Premium','0','1','0','1','0','0','1','0','0','1','1','0')")


        # save data to database
        conn.commit()
#from kivy.interactive import InteractiveLauncher

#import mysql.connector

#cnx = mysql.connector.connect(user='karanvirsngh', password='ether0110',
                              #host='SQL09.FREEMYSQL.NET',
                              #database='karant')

# cursor = cnx.cursor()

# cursor.execute("SELECT * FROM Writers")
# karanvir="oi"
# print cursor
# for Name in cursor:
#    print Name[1]
#    karanvir=Name[1]

#sm.add_widget(ProductDetailScreen(name='Product_Detail_Screen'))
#    sm.add_widget(ProductFilterScreen(name='Product_Filter_Screen'))
#sm.current = 'Main_Screen'
#Create the manager
#sm = ScreenManager()
#Add few screens
#for i in xrange(4):
#   screen = Screen(name='Title %d' % i)
#   sm.add_widget(screen)

#By default, the first screen added into the ScreenManager will be
#displayed. Then, you can change to another screen:

#Let's display the screen named 'Title 2'
#The transition will be automatically used.
# sm.current = 'Title 2'

# Sqllite
# conn = sqlite3.connect("aob.db") # or use :memory: to put it in RAM
# cursor = conn.cursor()


# if(sys.argv[1]=="create"):
#     #create a table
#     cursor.execute("""CREATE TABLE beers
#                      (name text, des text,\
#                      dark boolean, light boolean,\
#                      can boolean, bottle boolean, keg boolean,\
#                      craft boolean, domestic boolean, import boolean, specialty boolean,\
#                      sports boolean, dining boolean, beach boolean,\
#                      party boolean, club boolean,\
#                      tags text)\
#                     """)
#     # insert some data
#     cursor.execute("INSERT INTO beers VALUES\
#                  ('sharps', 'fosters-txt',\
#                     '1','0','0','1','0','0','0','0','1','0','0','1','1','0','tag1')")
#     cursor.execute("INSERT INTO beers VALUES\
#                  ('fosters', 'foster-txt',\
#                     '0','1','0','1','0','0','0','0','1','1','0','1','1','0','tag2')")

#     # save data to database
#     conn.commit()

Builder.load_string('''
#:kivy 1.0.9
<MainScreen>:
    FloatLayout:
        size: root.width, root.height
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                size: root.size
        RelativeLayout:
            size_x: root.width
            size_y: root.height
            Image:
                allow_stretch: True
                keep_ratio: False
                size: root.width, root.height
                source: 'images/SplashScreen.jpg'
           
<ProductScreen>:
    FloatLayout:
        size: root.width, root.height
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                size: root.size
        RelativeLayout:
            size_x: root.width
            size_hint_y: 0.05
            pos_hint: {'x':0, 'y':0.45}
            Image:
                allow_stretch: True
                keep_ratio: False
                size: root.width, root.height
                source: 'images/product_list_gradient.jpg'
        RelativeLayout:
            size_x: root.width
            size_hint_y: 0.05
            pos_hint: {'x':0.0, 'y':0.05}
            Image:
                allow_stretch: True
                keep_ratio: False
                size: root.width, root.height
                source: 'images/product_list_gradient.jpg'

        RelativeLayout:
            size_x: root.width
            size_hint_y: 0.15
            pos_hint: {'x':0.0,'y':.85}
            Image:
                allow_stretch: True
                keep_ratio: False
                size: root.width, root.height
                source: 'images/navigation_bar_gradient.jpg'
            Button:
                text: 'Go back'
                size_hint: None, None
                size: 150, 50
                pos_hint: {'x':0.0, 'y':0.3}
                on_press: root.on_click()
                background_normal: 'images/chromeButtonUp.gif'
                allow_stretch: True
                keep_ratio: False
            Button:
                text: 'Product Detail'
                size_hint: None, None
                size: 250, 50
                pos_hint: {'x':0.8, 'y':0.3}
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
                rgb: 1.0, 1.0, 1.0
            Rectangle:
                source: 'images/detail_background.png'
                size: root.size
        RelativeLayout:
            size_x: root.width
            size_hint_y: 0.15
            pos_hint: {'x':0.0,'y':.85}
            Image:
                allow_stretch: True
                keep_ratio: False
                size: root.width, root.height
                source: 'images/navigation_bar_gradient.jpg'
            Button:
                text: 'Product Screen'
                size_hint: None, None
                size: 250, 50
                pos_hint: {'x':0.0, 'y':0.3}
                on_press: root.click_product_screen()
            Button:
                text: 'Main Menu'
                size_hint: None, None
                size: 250, 50
                pos_hint: {'x':0.8, 'y':0.3}
                on_press: root.click_main_screen()

<ProductFilterScreen>:
    FloatLayout:
        #spacing: 10
        size: root.width, root.height
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                size: root.size
        RelativeLayout:
            size_x: root.width
            size_hint_y: 0.15
            pos_hint: {'x':0.0,'y':.85}
            Image:
                allow_stretch: True
                keep_ratio: False
                size: root.width, root.height
                source: 'images/navigation_bar_gradient.jpg'
            Button:
                text: 'Main Menu'
                size_hint: None, None
                size: 250, 50
                pos_hint: {'x':0.0, 'y':0.3}
                on_press: root.click_main_screen()
            Button:
                text: 'Product List Screen'
                size_hint: None, None
                size: 250, 50
                pos_hint: {'x':0.8, 'y':0.3}
                on_press: root.click_product_list_screen()
            Button:
                text: 'Sample Detail Screen'
                size_hint: None, None
                size: 250, 50
                pos_hint: {'x':1.6, 'y':0.3}
                on_press: root.click_product_detail_screen()
        RelativeLayout:
            size_x: root.width
            size_hint_y: 0.15
            pos: 0, 0
            Image:
                allow_stretch: True
                keep_ratio: False
                size: root.width, root.height
                source: 'images/navigation_bar_gradient.jpg'
''')

class ProductScreen(Screen):
    query_result = None
    scroll_view_one = ScrollView(bar_color= [0,0,0,0], size_hint=(1.0, None), height=240, pos_hint={'x':0.0,'y':0.5})
    scroll_view_two = ScrollView(bar_color= [0,0,0,0], size_hint=(1.0, None), height=240, pos_hint={'x':0.0,'y':0.1})

    def __init__(self, **kwargs):
        super(ProductScreen, self).__init__(**kwargs)

        #data = { str(i): {'text': str(i) } for i in xrange(100) }
        #data = { str(i): {'text': str(i), 'is_selected': False} for i in xrange(100) }
        #list_item_args_converter = lambda row_index, rec: {'text': rec['text'],
        #                        #'is_selected': rec['is_selected'],
        #                        'size_hint_y': None,
        #                        'size_hint_x': None,
        #                        'height': 100,
        #                        'width': 100,
        #                        'source': 'images/Batch19.jpg'}

        #list_adapter = ListAdapter(data=data,
        #                   template='ProductItem',
        #                   args_converter=list_item_args_converter)

        #dict_adapter = DictAdapter(sorted_keys=[str(i) for i in xrange(100)],
        #                   data=data,
        #                   args_converter=list_item_args_converter,
        #                   template='ProductItem')
        #list_view = ListView(adapter=dict_adapter)
        #list_view.size_hint = (0.5,1.0)
        #list_view.pos_hint = {'x':.3, 'y':0.0}

        #self.add_widget(list_view)

        #Get all image file name in Images Craft Bottles
        first_list = []
        second_list = []
        if self.query_result is None:
            i = 0
            for name in os.listdir('./images/bottles/'):
                if i%2 == 0:
                    first_list.append(name)
                else:
                    second_list.append(name)
                i = i + 1
            #get all Items
        else:
            i = 0
            for name in self.query_result:
                if i%2 == 0:
                    first_list.append(name)
                else:
                    second_list.append(name)
                i = i + 1
        print first_list
        print second_list

        craft_image_list = []

        for i in os.listdir('./images/bottles/'):
            craft_image_list.append(i)
        #First Horizontal Scrollable View
        grid_one_layout = GridLayout(cols=len(craft_image_list), spacing=10, size_hint_x=None)
        #Make sure the height is such that there is something to scroll.
        grid_one_layout.bind(minimum_width=grid_one_layout.setter('width'))
        for file_name in craft_image_list:
            anchor_one_layout = AnchorLayout(size_hint_x=None, size_hint_y=None, height=240, width=200, anchor_x='center', anchor_y='bottom')
            btn = Button(text=file_name, color=[0,0,0,0], size_hint_y=None, size_hint_x=None, height=240, width=200, background_color=[1,1,1,1], background_normal='images/bottles/{f_name}'.format(f_name=file_name))
            btn.bind(on_press=self.on_item_click)
            beer_name = file_name[:-4]
            label = Label(text=beer_name, color=[0,0,0,1], italic=True, font_size='12dp', size_hint=(None, None), height=30, width=anchor_one_layout.width, halign='center', pos_hint={'x':0,'y':0})
            anchor_one_layout.add_widget(btn)
            anchor_one_layout.add_widget(label)
            grid_one_layout.add_widget(anchor_one_layout)

        self.scroll_view_one.do_scroll_y=False
        self.scroll_view_one.do_scroll_x=True
        self.scroll_view_one.add_widget(grid_one_layout)
        self.add_widget(self.scroll_view_one)

        #Get all image file name in Images Domestic Bottles
        domestic_image_list = []
        for i in os.listdir('./images/bottles/'):
            domestic_image_list.append(i)
        #First Horizontal Scrollable View
        grid_two_layout = GridLayout(cols=len(domestic_image_list), spacing=10, size_hint_x=None)
        #Make sure the height is such that there is something to scroll.
        grid_two_layout.bind(minimum_width=grid_two_layout.setter('width'))
        for file_name in domestic_image_list:
            anchor_two_layout = AnchorLayout(size_hint_x=None, size_hint_y=None, height=240, width=200, anchor_x='center', anchor_y='bottom')
            btn = Button(text=file_name, color=[0,0,0,0], size_hint_y=None, size_hint_x=None, height=240, width=200, background_color=[1,1,1,1], background_normal='images/bottles/{f_name}'.format(f_name=file_name))
            btn.bind(on_press=self.on_item_click)
            beer_name = file_name[:-4]
            label = Label(text=beer_name, color=[0,0,0,1], italic=True, font_size='12dp', size_hint=(None, None), height=30, width=anchor_two_layout.width, halign='center', pos_hint={'x':0,'y':0})
            anchor_two_layout.add_widget(btn)
            anchor_two_layout.add_widget(label)
            grid_two_layout.add_widget(anchor_two_layout)

        self.scroll_view_two.do_scroll_y=False
        self.scroll_view_two.do_scroll_x=True
        self.scroll_view_two.add_widget(grid_two_layout)
        self.add_widget(self.scroll_view_two)
        #Second Horizontal Scrollable View
        #layout_two
    def on_item_click(self, btn):
        beer_name = btn.text
        beer_description = 'aroma hops, brewing cold filter sparge. hefe, hydrometer cask lauter aroma hops bottom fermenting yeast, pitching wheat beer glass. specific gravity hop back trappist, " bunghole abbey aroma hops lager, brew oxidized crystal malt keg." finishing hops, fermentation brewhouse crystal malt. conditioning tank; aau, ipa barley rims lagering-- hydrometer sparge sparge. cask conditioning dry stout trappist bitter. bacterial shelf life units of bitterness hop back dextrin sparge imperial adjunct. hydrometer conditioning tank filter lager lambic, " barley," lager gravity."'
        print beer_name
        sm.transition = SlideTransition(direction='left')
        sm.current = 'Product_Detail_Screen'
        # PERFORM SECOND QUERY HERE to narrow to one item
        name = beer_name[:-4]
        print name
        cursor.execute("SELECT * FROM beers WHERE name = '%s'"%(name))
        result = cursor.fetchall()
        print result
        # resul product detail class's populate function
        product_detail_instance = sm.get_screen('Product_Detail_Screen')
        product_detail_instance.show_item(beer_name, beer_description)

    def on_click(self):
        sm.transition = SlideTransition(direction='right')
        sm.current = 'Product_Filter_Screen'
        #Reset query list
        self.reset_list()
        #sm.transition = SlideTransition(direction="up")
    def click_product_detail_screen(self):

        sm.transition = FadeTransition()
        sm.current = 'Product_Detail_Screen'
        self.reset_list()
        self.set_list()

    def update_list(self, query):
        # Perform List Updates
        self.query_result = query
        #self.remove_widget(self.scroll_view_one)
        #self.remove_widget(self.scroll_view_two)
    def reset_list(self):
        self.query_result = None

    def set_list(self):
        #Get all image file name in Images Craft Bottles
        first_list = []
        second_list = []
        if self.query_result is None:
            i = 0
            for name in os.listdir('./images/bottles/'):
                if i%2 == 0:
                    first_list.append(name)
                else:
                    second_list.append(name)
                i = i + 1
            #get all Items
        else:
            i = 0
            for name in self.query_result:
                if i%2 == 0:
                    first_list.append(name+'.jpg')
                else:
                    second_list.append(name+'.jpg')
                i = i + 1
        # Clear widget first
        self.scroll_view_one.clear_widgets()
        self.scroll_view_two.clear_widgets()
        self.remove_widget(self.scroll_view_one)
        self.remove_widget(self.scroll_view_two)
        #First Horizontal Scrollable View
        grid_one_layout = GridLayout(cols=len(first_list), spacing=10, size_hint_x=None)
        #Make sure the height is such that there is something to scroll.
        grid_one_layout.bind(minimum_width=grid_one_layout.setter('width'))
        for file_name in first_list:
            anchor_one_layout = AnchorLayout(size_hint_x=None, size_hint_y=None, height=240, width=200, anchor_x='center', anchor_y='bottom')
            btn = Button(text=file_name, color=[0,0,0,0], size_hint_y=None, size_hint_x=None, height=240, width=200, background_color=[1,1,1,1], background_normal='images/bottles/{f_name}'.format(f_name=file_name))
            btn.bind(on_press=self.on_item_click)
            beer_name = file_name[:-4]
            label = Label(text=beer_name, color=[0,0,0,1], italic=True, font_size='12dp', size_hint=(None, None), height=30, width=anchor_one_layout.width, halign='center', pos_hint={'x':0,'y':0})
            anchor_one_layout.add_widget(btn)
            anchor_one_layout.add_widget(label)
            grid_one_layout.add_widget(anchor_one_layout)

        self.scroll_view_one.add_widget(grid_one_layout)
        self.add_widget(self.scroll_view_one)

        #First Horizontal Scrollable View
        grid_two_layout = GridLayout(cols=len(second_list), spacing=10, size_hint_x=None)
        #Make sure the height is such that there is something to scroll.
        grid_two_layout.bind(minimum_width=grid_two_layout.setter('width'))
        for file_name in second_list:
            anchor_two_layout = AnchorLayout(size_hint_x=None, size_hint_y=None, height=240, width=200, anchor_x='center', anchor_y='bottom')
            btn = Button(text=file_name, color=[0,0,0,0], size_hint_y=None, size_hint_x=None, height=240, width=200, background_color=[1,1,1,1], background_normal='images/bottles/{f_name}'.format(f_name=file_name))
            btn.bind(on_press=self.on_item_click)
            beer_name = file_name[:-4]
            label = Label(text=beer_name, color=[0,0,0,1], italic=True, font_size='12dp', size_hint=(None, None), height=30, width=anchor_two_layout.width, halign='center', pos_hint={'x':0,'y':0})
            anchor_two_layout.add_widget(btn)
            anchor_two_layout.add_widget(label)
            grid_two_layout.add_widget(anchor_two_layout)

        self.scroll_view_two.add_widget(grid_two_layout)
        self.add_widget(self.scroll_view_two)

class ProductDetailScreen(Screen):
    beer_description = 'This is a description of the best beer in the world'
    logoImage = Image(size_hint=(0.15,0.15), pos_hint={'x':0.00,'y':0.7}, source='images/main_logo.jpg', allow_stretch=True, keep_ratio=True)
    nameLabel = Label(text='{name}'.format(name='Beer Name'), italic=True, font_size=(30), color=[1,1,1,1], pos_hint={'x':0.25,'y':0.878}, size_hint=(.5,.12))
    bottleImage_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(0.5,0.85), pos=(0.0,0.0))
    bottleImage = Image(size=(300, 425), size_hint=(None, None), source='images/bottles/{name}'.format(name='Aguila.jpg'), allow_stretch=True, keep_ratio=True)
    nameLabel_two = Label(font_size='14sp', bold=True,color=[0,0,0,1], size_hint=(0.5, 0.1), pos_hint={'x':0.5,'y':0.65}, halign='left', text_size=(700, 30))
    locationLabel = Label(text='Location: Unknown', font_size='12sp', color=[0,0,0,1], size_hint=(0.5, 0.1), pos_hint={'x':0.5,'y':0.6}, halign='left', text_size=(700, 30))
    priceLabel = Label(text='$$', font_size='12sp', color=[0,0,0,1], size_hint=(0.5,0.1), pos_hint={'x':0.5,'y':0.55}, halign='left', text_size=(700, 30))
    descriptionAnchor = BoxLayout(orientation='vertical', anchor_y='top', anchor_x='left', size_hint=(1.0,0.5))
    descriptionLabel = Label(text='{desc}'.format(desc=beer_description), font_size='10sp', size_hint=(1.0,1.0), text_size=(700, 500), halign='left', valign='top', color=[0,0,0,1])
    info_layout = RelativeLayout(orietation='vertical', size_hint=(0.5,.85), pos_hint={'x':0.5,'y':0.0})
    def __init__(self, **kwargs):
        super(ProductDetailScreen, self).__init__(**kwargs)
        # File name of the beer selected
        # NEEDS TO BE SET
        #bottle_name = ('Coors_Lightbottle.jpg')
        # Beer name from the given bottle name
        #beer_name = re.sub('[^a-zA-Z0-9\n]', ' ', bottle_name)
        #beer_name = beer_name[:-4]
        # Beer text description pulled cfrom the given beer_name
        # NEEDS TO BE SET
        self.descriptionAnchor.add_widget(self.descriptionLabel)
        # self.info_layout.add_widget(self.nameLabel_two)
        # self.info_layout.add_widget(self.locationLabel)
        # self.info_layout.add_widget(self.priceLabel)

        self.info_layout.add_widget(self.descriptionAnchor)
        self.bottleImage_layout.add_widget(self.bottleImage)
        # Get all the tags for the given beer
        # NEEDS TO BE SET
        beer_tags = 'sports football stadium party coors molson light beer mountains'
        tag_list = []
        for i in beer_tags.split():
            tag_list.append(i)
        # Horizontal Scrollable View
        grid_one_layout = GridLayout(cols=30, spacing=5, size_hint_x=None)
        # Make sure the height is such that there is something to scroll.
        grid_one_layout.bind(minimum_width=grid_one_layout.setter('width'))
        for tag_name in tag_list:
            relative_one_layout = AnchorLayout(size_hint_x=None, size_hint_y=None, height=30, width=100)
            btn = Button(size_hint_y=None, size_hint_x=None, height=30, width=100, background_color=[1,1,1,1])
            label = Label(text=tag_name, color=[0,0,0,1], size_hint=(None, None), height=30, width=relative_one_layout.width, halign='center', pos_hint={'x':0,'y':0})
            relative_one_layout.add_widget(btn)
            relative_one_layout.add_widget(label)
            grid_one_layout.add_widget(relative_one_layout)

        scroll_view_one = ScrollView(bar_color=[0,0,0,0], size_hint=(1.0, None), height=30, pos_hint={'x':0.0,'y':0.0})
        scroll_view_one.do_scroll_y=False
        scroll_view_one.do_scroll_x=True
        scroll_view_one.add_widget(grid_one_layout)
        #self.add_widget(scroll_view_one)


        # Add wigets to the product detail page
        self.add_widget(self.logoImage)
        self.add_widget(self.bottleImage_layout)
        self.add_widget(self.nameLabel)

        self.add_widget(self.nameLabel_two)
        self.add_widget(self.locationLabel)
        self.add_widget(self.priceLabel)
        self.add_widget(self.info_layout)

    def animate(self):
        anim = Animation(x=100, y=100)
        anim.start(button)
        #self.add_widget(button)

    def click_main_screen(self):
        sm.transition = WipeTransition(direction='left')
        sm.current = 'Main_Screen'
        # Reset list
        product_screen = sm.get_screen('Product_Screen')
        product_screen.reset_list()

    def click_product_screen(self):
            sm.transition = WipeTransition(direction='left')
            sm.current = 'Product_Screen'

    def show_item(self, name, description):
        self.nameLabel.text = name[:-4]
        self.bottleImage.source = 'images/bottles/' + name
        self.logoImage.source = 'images/logos/' + name
        self.descriptionLabel.text = description
        self.nameLabel_two.text = name[:-4]

class ProductFilterScreen(Screen):
    # Dictionary that contains all the fields. 1 represents selected, 0 is not selected.
    query_dict = {'light':0, 'dark':0, 'bottle':0, 'can':0, 'craft':0, 'domestic':0, 'import':0, 'specialty':0, 'sports':0, 'dining':0, 'party':0, 'club':0}
    #Stacklayout for each selection screen            
    box_layout_one = BoxLayout(size_hint=(1.0, 0.2), pos=(0, 300), spacing=2)
    box_layout_two = BoxLayout(size_hint=(1.0, 0.2), pos=(1300, 300), spacing=2)
    box_layout_three = BoxLayout(size_hint=(1.0, 0.2), pos=(1300, 300), spacing=2)
    box_layout_four = BoxLayout(size_hint=(1.0, 0.2), pos=(1300, 300), spacing=2)
    stack_layout_one = StackLayout(orientation='lr-tb', spacing=0, size_hint=(1.0,0.8))
    stack_layout_two = StackLayout(orientation='lr-tb', spacing=0, size_hint=(1.0,0.8), pos=(1300, 0))
    stack_layout_three = StackLayout(orientation='lr-tb', spacing=0, size_hint=(1.0,0.8), pos=(1300, 0))
    stack_layout_four = StackLayout(orientation='lr-tb', spacing=0, size_hint=(1.0,0.8), pos=(1300, 0))
    # Light/Dark Beer Button
    lightbeer_button = Button(text='Light Beer', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    darkbeer_button = Button(text='Dark Beer', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    skip_one_button = Button(text='Skip', size_hint=(1.0,1.0), background_color=[.3,.3,.3,1.0])
    # Bottle/Can Beer Button
    bottlebeer_button = Button(text='Bottle Beer', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    canbeer_button = Button(text='Canned Beer', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    skip_two_button = Button(text='Skip', size_hint=(1.0,1.0), background_color=[.3,.3,.3,1.0])
    # Types of Beer Button
    craftbeer_button = Button(text='Craft Beer', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    domesticbeer_button = Button(text='Domestic Beer', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    importbeer_button = Button(text='Import Beer', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    specialtybeer_button = Button(text='Specialty Beer', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    skip_three_button = Button(text='Skip', size_hint=(1.0,1.0), background_color=[.3,.3,.3,1.0])
    # Special Tags
    sportsbeer_button = Button(text='Sports', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    diningbeer_button = Button(text='Dining', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    partybeer_button = Button(text='Party', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    clubbeer_button = Button(text='Club', color=[0,0,0,1], size_hint=(1.0,1.0), background_normal='images/filter_button_gradient.jpg')
    skip_four_button = Button(text='Skip', size_hint=(1.0,1.0), background_color=[.3,.3,.3,1.0])

    def stack_animation_complete(self, animation, widget):
        widget.pos=(1300, 300)

    def stack_one_item_select(self, btn):
        # Check What's Selected
        if btn.text == 'Light Beer':
            self.query_dict['light'] = 1
        elif btn.text == 'Dark Beer':
            self.query_dict['dark'] = 1
        out_anim = Animation(x=-700, y=300, t='in_out_back', duration=1.0)
        out_anim.bind(on_complete=self.stack_animation_complete)
        out_anim.start(self.box_layout_one)
        #Animation.cancel_all(self.stack_layout_one, 'x', 'y')
        in_anim = Animation(x=0, y=300, t='in_out_back', duration=1.2)
        in_anim.start(self.box_layout_two)

    def stack_two_item_select(self, btn):
        # Check What's Selected
        if btn.text == 'Bottle Beer':
            self.query_dict['bottle'] = 1
        elif btn.text == 'Canned Beer':
            self.query_dict['can'] = 1
        out_anim = Animation(x=-700, y=300, t='in_out_back', duration=1.0)
        out_anim.bind(on_complete=self.stack_animation_complete)
        out_anim.start(self.box_layout_two)
        #Animation.cancel_all(self.stack_layout_one, 'x', 'y')
        in_anim = Animation(x=0, y=300, t='in_out_back', duration=1.2)
        in_anim.start(self.box_layout_three)

    def stack_three_item_select(self, btn):
        # Check What's Selected
        if btn.text == 'Craft Beer':
            self.query_dict['craft'] = 1
        elif btn.text == 'Domestic Beer':
            self.query_dict['domestic'] = 1
        elif btn.text == 'Import Beer':
            self.query_dict['import'] = 1
        elif btn.text == 'Specialty Beer':
            self.query_dict['specialty'] = 1
        out_anim = Animation(x=-700, y=300, t='in_out_back', duration=1.0)
        out_anim.bind(on_complete=self.stack_animation_complete)
        out_anim.start(self.box_layout_three)
        #Animation.cancel_all(self.stack_layout_one, 'x', 'y')
        in_anim = Animation(x=0, y=300, t='in_out_back', duration=1.2)
        in_anim.start(self.box_layout_four)

    def stack_four_item_select(self, btn):
        if btn.text == 'Sports':
            self.query_dict['sports'] = 1
        elif btn.text == 'Dining':
            self.query_dict['dining'] = 1
        elif btn.text == 'Party':
            self.query_dict['party'] = 1
        elif btn.text == 'Club':
            self.query_dict['club'] = 1
        
        # Reset stack layout positions
        self.box_layout_one.pos=(0,300)
        #self.box_layout_two.pos=(1300,400)
        #self.box_layout_three.pos=(1300,400)
        self.box_layout_four.pos=(1300,300) 
        #---------------------------------------------------
        for i in self.query_dict:
            print i + str(self.query_dict[i])
        result_q=[]
        for i in self.query_dict:
            print i + str(self.query_dict[i])
            if(self.query_dict[i]==1):
                result_q.append(i)
            
        print result_q
        #search parameter to be passed to sql db
        search_p=''
        for i,j in enumerate(result_q):
            search_p=search_p+j+'='+'1'
            if(i+1<len(result_q)):
               search_p=search_p+' and '
        print search_p

        #PERFORM SQL QUERY HERE
        #todo: include the case where all filters were skipped
        cursor.execute('SELECT name FROM beers where %s'%(search_p))
        allentries=cursor.fetchall()
        #print allentries
        result = [str(entry[0]) for entry in allentries]
        print result
        #---------------------------------------------------
        #RESET QUERY DIRECTIONARY
        for k in self.query_dict.keys():
            self.query_dict[k] = 0
        #Animate Screen Transition
        sm.transition = SlideTransition(direction='left')
        sm.current = 'Product_Screen'
        product_list_screen = sm.get_screen('Product_Screen')
        product_list_screen.update_list(result)
        product_list_screen.set_list()

        #out_anim = Animation(x=-700, y=0, t='in_out_back', duration=1.2)
        #out_anim.bind(on_complete=self.stack_animation_complete)
        #out_anim.start(self.stack_layout_one)
        #Animation.cancel_all(self.stack_layout_one, 'x', 'y')
        #in_anim = Animation(x=0, y=0, t='in_out_back', duration=1.2)
        #in_anim.start(self.stack_layout_two)

    def __init__(self, **kwargs):
        super(ProductFilterScreen, self).__init__(**kwargs)
        #StackLayout
        #stack_layout = StackLayout(orientation='lr-tb', size_hint=(1.0,0.9))
        #stack_layout = ObjectProperty(None)
        self.lightbeer_button.bind(on_press=self.stack_one_item_select)
        self.darkbeer_button.bind(on_press=self.stack_one_item_select)
        self.skip_one_button.bind(on_press=self.stack_one_item_select)

        self.bottlebeer_button.bind(on_press=self.stack_two_item_select)
        self.canbeer_button.bind(on_press=self.stack_two_item_select)
        self.skip_two_button.bind(on_press=self.stack_two_item_select)

        self.craftbeer_button.bind(on_press=self.stack_three_item_select)
        self.domesticbeer_button.bind(on_press=self.stack_three_item_select)
        self.importbeer_button.bind(on_press=self.stack_three_item_select)
        self.specialtybeer_button.bind(on_press=self.stack_three_item_select)
        self.skip_three_button.bind(on_press=self.stack_three_item_select)

        self.sportsbeer_button.bind(on_press=self.stack_four_item_select)
        self.diningbeer_button.bind(on_press=self.stack_four_item_select)
        self.partybeer_button.bind(on_press=self.stack_four_item_select)
        self.clubbeer_button.bind(on_press=self.stack_four_item_select)
        self.skip_four_button.bind(on_press=self.stack_four_item_select)

        # First Stack View
        self.box_layout_one.add_widget(self.lightbeer_button)
        self.box_layout_one.add_widget(self.darkbeer_button)
        self.box_layout_one.add_widget(self.skip_one_button)
        # Second Stack View
        self.box_layout_two.add_widget(self.bottlebeer_button)
        self.box_layout_two.add_widget(self.canbeer_button)
        self.box_layout_two.add_widget(self.skip_two_button)
        # Third Stack View
        self.box_layout_three.add_widget(self.craftbeer_button)
        self.box_layout_three.add_widget(self.domesticbeer_button)
        self.box_layout_three.add_widget(self.importbeer_button)
        self.box_layout_three.add_widget(self.specialtybeer_button)
        self.box_layout_three.add_widget(self.skip_three_button)
        # Four Stack View
        self.box_layout_four.add_widget(self.sportsbeer_button)
        self.box_layout_four.add_widget(self.diningbeer_button)
        self.box_layout_four.add_widget(self.partybeer_button)
        self.box_layout_four.add_widget(self.clubbeer_button)
        self.box_layout_four.add_widget(self.skip_four_button)

        self.add_widget(self.box_layout_one)
        self.add_widget(self.box_layout_two)   
        self.add_widget(self.box_layout_three)
        self.add_widget(self.box_layout_four)

    def click_main_screen(self):
        sm.transition = WipeTransition(direction='left')
        sm.current = 'Main_Screen'

    def click_product_list_screen(self):
        sm.transition = WipeTransition(direction='right')
        sm.current = 'Product_Screen'
        screen = sm.get_screen('Product_Screen')
        screen.reset_list()
        screen.set_list()

    def click_product_detail_screen(self):
        sm.transition = WipeTransition(direction='right')
        sm.current = 'Product_Detail_Screen'

class MainScreen(Screen):
    float_layout = AnchorLayout(size_hint=(1.0, 0.4), pos=(0,0))
    image = Image(size_hint=(1.0, 1.0), source='images/main_background.jpg', allow_stretch=True, keep_ratio=False)
    box_layout = BoxLayout(size_hint=(1.0, 1.0), orientation='vertical', pos=(0,0), spacing=5, padding=[0,10])
    anchor_one_layout = AnchorLayout(size_hint=(1.0,0.3), anchor_x='center', anchor_y='center')
    anchor_two_layout = AnchorLayout(size_hint=(1.0,0.3), anchor_x='center', anchor_y='center')
    button_one = Button(size_hint=(0.3,1.0), text='Find your Matching', italic=True, font_size='20sp', background_color=(1,1,1,1))
    button_two = Button(size_hint=(0.3,1.0), text='Product Catalog', italic=True, font_size='20sp', background_color=(1,1,1,1))
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.button_one.bind(on_press=self.on_click_filter)
        self.button_two.bind(on_press=self.on_click_product_catalog)
        self.anchor_one_layout.add_widget(self.button_one)
        self.anchor_two_layout.add_widget(self.button_two)
        self.box_layout.add_widget(self.anchor_one_layout)
        self.box_layout.add_widget(self.anchor_two_layout)
        self.float_layout.add_widget(self.image)
        self.float_layout.add_widget(self.box_layout)
        self.add_widget(self.float_layout)

    def on_click_filter(self, btn):
        anim = Animation(x=0, y=-700, duration=1.0)
        anim.bind(on_complete=self.animation_complete)
        anim.start(self.float_layout)
        sm.transition = WipeTransition(direction='right')
        sm.current = 'Product_Filter_Screen'
    def on_click_product_catalog(self, btn):
        sm.transition = SlideTransition(direction='left')
        sm.current = 'Product_Screen'
    def animation_complete(self, animation, widget):
        widget.pos=(0,0)

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
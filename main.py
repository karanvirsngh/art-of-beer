import kivy
import os
import time
import re

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
            size_hint_y: 0.2
            pos: 0, 630
            Image:
                allow_stretch: True
                keep_ratio: False
                size: root.width, root.height
                source: 'images/button_gradient.jpg'
            Button:
                text: 'Go back'
                size_hint: None, None
                size: 150, 50
                pos_hint: {'x':0.0, 'y':0.3}
                on_press: root.on_click()
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
                rgb: 0.3, 0.3, 0.3
            Rectangle:
                size: root.size
        Button:
            text: 'Main Menu'
            size_hint: None, None
            size: 250, 50
            pos_hint: {'x':0.0, 'y':0.0}
            on_press: root.click_main_screen()
        Button:
            text: 'Product Screen'
            size_hint: None, None
            size: 250, 50
            pos_hint: {'x':0.4, 'y':0.0}
            on_press: root.click_product_screen()
        RelativeLayout:
            size_x: root.width
            size_hint_y: 0.05
            pos_hint: {'x':0, 'y':0.828}
            Image:
                allow_stretch: True
                keep_ratio: False
                size: root.width, root.height
                source: 'images/product_list_gradient.jpg'
        RelativeLayout:
            size_x: root.width
            size_hint_y: 0.05
            pos_hint: {'x':0.0, 'y':0.305}
            Image:
                allow_stretch: True
                keep_ratio: False
                size: root.width, root.height
                source: 'images/product_list_gradient.jpg'

<ProductFilterScreen>:
    BoxLayout:
        spacing: 10
        size: root.width, root.height
        canvas:
            Color:
                rgb: 1, 1, 1
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
        Button:
            text: 'Sample Detail Screen'
            size_hint: None, None
            size: 250, 50
            pos_hint: {'x':1.6, 'y':0.0}
            on_press: root.click_product_detail_screen()
''')

class ProductScreen(Screen):
    
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
        craft_image_list = []
        for i in os.listdir('./images/Craft/bottles/'):
            craft_image_list.append(i)
        #First Horizontal Scrollable View
        grid_one_layout = GridLayout(cols=30, spacing=10, size_hint_x=None)
        #Make sure the height is such that there is something to scroll.
        grid_one_layout.bind(minimum_width=grid_one_layout.setter('width'))
        for file_name in craft_image_list:
            relative_one_layout = AnchorLayout(size_hint_x=None, size_hint_y=None, height=200, width=200)
            btn = Button(size_hint_y=None, size_hint_x=None, height=200, width=200, background_color=[1,1,1,1], background_normal='images/Craft/bottles/{name}'.format(name=file_name))
            label = Label(text=file_name, color=[0,0,0,1], size_hint=(None, None), height=30, width=relative_one_layout.width, halign='center', pos_hint={'x':0,'y':0})
            relative_one_layout.add_widget(btn)
            relative_one_layout.add_widget(label)
            grid_one_layout.add_widget(relative_one_layout)

        scroll_view_one = ScrollView(bar_color= [0,0,0,0], size_hint=(1.0, None), height=200, pos_hint={'x':0.0,'y':0.5})
        scroll_view_one.do_scroll_y=False
        scroll_view_one.do_scroll_x=True
        scroll_view_one.add_widget(grid_one_layout)
        self.add_widget(scroll_view_one)

        #Get all image file name in Images Domestic Bottles
        domestic_image_list = []
        for i in os.listdir('./images/Domestic/bottles/'):
            domestic_image_list.append(i)
        #First Horizontal Scrollable View
        grid_two_layout = GridLayout(cols=30, spacing=10, size_hint_x=None)
        #Make sure the height is such that there is something to scroll.
        grid_two_layout.bind(minimum_width=grid_two_layout.setter('width'))
        for file_name in domestic_image_list:
            relative_two_layout = AnchorLayout(size_hint_x=None, size_hint_y=None, height=200, width=200)
            btn = Button(size_hint_y=None, size_hint_x=None, height=200, width=200, background_color=[1,1,1,1], background_normal='images/Domestic/bottles/{name}'.format(name=file_name))
            label = Label(text=file_name, color=[0,0,0,1], size_hint=(None, None), height=30, width=relative_two_layout.width, halign='center', pos_hint={'x':0,'y':0})
            relative_two_layout.add_widget(btn)
            relative_two_layout.add_widget(label)
            grid_two_layout.add_widget(relative_two_layout)

        scroll_view_two = ScrollView(bar_color= [0,0,0,0], size_hint=(1.0, None), height=200, pos_hint={'x':0.0,'y':0.1})
        scroll_view_two.do_scroll_y=False
        scroll_view_two.do_scroll_x=True
        scroll_view_two.add_widget(grid_two_layout)
        self.add_widget(scroll_view_two)
        #Second Horizontal Scrollable View
        #layout_two

    def on_click(self):
        sm.transition = SlideTransition(direction='right')
        sm.current = 'Product_Filter_Screen'
        #sm.transition = SlideTransition(direction="up")
    def click_product_detail_screen(self):
        sm.transition = FadeTransition()
        sm.current = 'Product_Detail_Screen'

class ProductDetailScreen(Screen):

    def __init__(self, **kwargs):
        super(ProductDetailScreen, self).__init__(**kwargs)
        # File name of the beer selected
        # NEEDS TO BE SET
        bottle_name = ('Coors_Lightbottle.jpg')
        # Beer name from the given bottle name
        beer_name = re.sub('[^a-zA-Z0-9\n]', ' ', bottle_name)
        beer_name = beer_name[:-10]
        # Beer text description pulled from the given beer_name
        # NEEDS TO BE SET
        beer_description = ('This is a description of the best beer in the world')
        # Button definitions of visual wigets
        logoButton = Button(size=(200, 70), size_hint=(None, None), pos_hint={'x':0.0,'y':0.88}, background_color=[1,1,1,1], background_normal='images/main_logo.jpg')
        nameButton = Button(text='{name}'.format(name=beer_name), font_size=(30), color=[255,0,0,1], pos_hint={'x':0.25,'y':0.878}, size_hint=(.5,.12), background_color=[.3,.3,.3,1.0])
        bottleButton = Button(size=(200, 283), size_hint=(None, None), pos_hint={'x':0.0,'y':0.355}, background_color=[1,1,1,1], background_normal='images/Domestic/bottles/{name}'.format(name=bottle_name))
        descriptionButton = Button(text='{desc}'.format(desc=beer_description), pos_hint={'x':0.25,'y':0.355}, size_hint=(.5,.475), background_color=[.3,.3,.3,1.0])
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
            btn = Button(size_hint_y=None, size_hint_x=None, height=30, width=100, background_color=[1,1,1,1], background_normal='images/filter_item_background.jpg')
            label = Label(text=tag_name, color=[0,0,0,1], size_hint=(None, None), height=30, width=relative_one_layout.width, halign='center', pos_hint={'x':0,'y':0})
            relative_one_layout.add_widget(btn)
            relative_one_layout.add_widget(label)
            grid_one_layout.add_widget(relative_one_layout)

        scroll_view_one = ScrollView(bar_color= [0,0,0,0], size_hint=(1.0, None), height=30, pos_hint={'x':0.0,'y':0.25})
        scroll_view_one.do_scroll_y=False
        scroll_view_one.do_scroll_x=True
        scroll_view_one.add_widget(grid_one_layout)
        self.add_widget(scroll_view_one)


        # Add wigets to the product detail page
        self.add_widget(logoButton)
        self.add_widget(bottleButton)
        self.add_widget(nameButton)
        self.add_widget(descriptionButton)

    def animate(self):
        anim = Animation(x=100, y=100)
        anim.start(button)
        #self.add_widget(button)

    def click_main_screen(self):
        sm.transition = WipeTransition(direction='left')
        sm.current = 'Main_Screen'

    def click_product_screen(self):
            sm.transition = WipeTransition(direction='left')
            sm.current = 'Product_Screen'

class ProductFilterScreen(Screen):
    # Dictionary that contains all the fields. 1 represents selected, 0 is not selected.
    query_dict = {'light':0, 'dark':0, 'bottle':0, 'can':0, 'craft':0, 'domestic':0, 
                'import':0, 'specialty':0, 'sport':0, 'dining':0, 'party':0, 'club':0}
    #Stacklayout for each selection screen            
    stack_layout_one = StackLayout(orientation='lr-tb', spacing=0, size_hint=(1.0,0.9))
    stack_layout_two = StackLayout(orientation='lr-tb', spacing=0, size_hint=(1.0,0.9), pos=(1200, 0))
    stack_layout_three = StackLayout(orientation='lr-tb', spacing=0, size_hint=(1.0,0.9), pos=(1200, 0))
    stack_layout_four = StackLayout(orientation='lr-tb', spacing=0, size_hint=(1.0,0.9), pos=(1200, 0))
    # Light/Dark Beer Button
    lightbeer_button = Button(text='Light Beer', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    darkbeer_button = Button(text='Dark Beer', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    skip_one_button = Button(text='Skip', size_hint=(.333,.3), background_color=[.3,.3,.3,1.0])
    # Bottle/Can Beer Button
    bottlebeer_button = Button(text='Bottle Beer', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    canbeer_button = Button(text='Canned Beer', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    skip_two_button = Button(text='Skip', size_hint=(.333,.3), background_color=[.3,.3,.3,1.0])
    # Types of Beer Button
    craftbeer_button = Button(text='Craft Beer', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    domesticbeer_button = Button(text='Domestic Beer', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    importbeer_button = Button(text='Import Beer', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    specialtybeer_button = Button(text='Specialty Beer', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    skip_three_button = Button(text='Skip', size_hint=(.333,.3), background_color=[.3,.3,.3,1.0])
    # Special Tags
    sportsbeer_button = Button(text='Sports', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    diningbeer_button = Button(text='Dining', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    partybeer_button = Button(text='Party', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    clubbeer_button = Button(text='Club', size_hint=(.333,.3), background_normal='images/filter_item_background.jpg')
    skip_four_button = Button(text='Skip', size_hint=(.333,.3), background_color=[.3,.3,.3,1.0])

    def stack_animation_complete(self, animation, widget):
        self.remove_widget(widget)

    def stack_one_item_select(self, btn):
        # Check What's Selected
        if btn.getter('text') == 'Light Beer':
            self.query_dict['light'] = 1
        elif btn.getter('text') == 'Dark Beer':
            self.query_dict['dark'] = 1
        out_anim = Animation(x=-700, y=0, t='in_out_back', duration=1.0)
        out_anim.bind(on_complete=self.stack_animation_complete)
        out_anim.start(self.stack_layout_one)
        #Animation.cancel_all(self.stack_layout_one, 'x', 'y')
        in_anim = Animation(x=0, y=0, t='in_out_back', duration=1.2)
        in_anim.start(self.stack_layout_two)

    def stack_two_item_select(self, btn):
        # Check What's Selected
        if btn.getter('text') == 'Bottle Beer':
            self.query_dict['bottle'] = 1
        elif btn.getter('text') == 'Canned Beer':
            self.query_dict['can'] = 1
        out_anim = Animation(x=-700, y=0, t='in_out_back', duration=1.0)
        out_anim.bind(on_complete=self.stack_animation_complete)
        out_anim.start(self.stack_layout_two)
        #Animation.cancel_all(self.stack_layout_one, 'x', 'y')
        in_anim = Animation(x=0, y=0, t='in_out_back', duration=1.2)
        in_anim.start(self.stack_layout_three)

    def stack_three_item_select(self, btn):
        # Check What's Selected
        if btn.getter('text') == 'Craft Beer':
            self.query_dict['craft'] = 1
        elif btn.getter('text') == 'Domestic Beer':
            self.query_dict['domestic'] = 1
        elif btn.getter('text') == 'Import Beer':
            self.query_dict['import'] = 1
        elif btn.getter('text') == 'Specialty Beer':
            self.query_dict['specialty'] = 1
        out_anim = Animation(x=-700, y=0, t='in_out_back', duration=1.0)
        out_anim.bind(on_complete=self.stack_animation_complete)
        out_anim.start(self.stack_layout_three)
        #Animation.cancel_all(self.stack_layout_one, 'x', 'y')
        in_anim = Animation(x=0, y=0, t='in_out_back', duration=1.2)
        in_anim.start(self.stack_layout_four)

    def stack_four_item_select(self, btn):
        if btn.getter('text') == 'Sports':
            self.query_dict['sport'] = 1
        elif btn.getter('text') == 'Dining':
            self.query_dict['dining'] = 1
        elif btn.getter('text') == 'Party':
            self.query_dict['party'] = 1
        elif btn.getter('text') == 'Club':
            self.query_dict['club'] = 1
        self.remove_widget(self.stack_layout_four)
        # Reset stack layout positions
        self.stack_layout_one.pos=(0,0)
        self.stack_layout_two.pos=(1200,0)
        self.stack_layout_three.pos=(1200,0)
        self.stack_layout_four.pos=(1200,0)
        #PERFORM SQL QUERY HERE


        #---------------------------------------------------
        #RESET QUERY DIRECTIONARY
        for k in self.query_dict.keys():
            self.query_dict[k] = 0
        #Animate Screen Transition
        sm.transition = SlideTransition(direction='left')
        sm.current = 'Product_Screen'
        # Re-add all the widgets
        self.add_widget(self.stack_layout_one)
        self.add_widget(self.stack_layout_two)
        self.add_widget(self.stack_layout_three)
        self.add_widget(self.stack_layout_four)

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
        self.stack_layout_one.add_widget(self.lightbeer_button)
        self.stack_layout_one.add_widget(self.darkbeer_button)
        self.stack_layout_one.add_widget(self.skip_one_button)
        # Second Stack View
        self.stack_layout_two.add_widget(self.bottlebeer_button)
        self.stack_layout_two.add_widget(self.canbeer_button)
        self.stack_layout_two.add_widget(self.skip_two_button)
        # Third Stack View
        self.stack_layout_three.add_widget(self.craftbeer_button)
        self.stack_layout_three.add_widget(self.domesticbeer_button)
        self.stack_layout_three.add_widget(self.importbeer_button)
        self.stack_layout_three.add_widget(self.specialtybeer_button)
        self.stack_layout_three.add_widget(self.skip_three_button)
        # Four Stack View
        self.stack_layout_four.add_widget(self.sportsbeer_button)
        self.stack_layout_four.add_widget(self.diningbeer_button)
        self.stack_layout_four.add_widget(self.partybeer_button)
        self.stack_layout_four.add_widget(self.clubbeer_button)
        self.stack_layout_four.add_widget(self.skip_four_button)

        self.add_widget(self.stack_layout_one)
        self.add_widget(self.stack_layout_two)   
        self.add_widget(self.stack_layout_three)
        self.add_widget(self.stack_layout_four)

    def click_main_screen(self):
        sm.transition = WipeTransition(direction='left')
        sm.current = 'Main_Screen'

    def click_product_list_screen(self):
        sm.transition = WipeTransition(direction='right')
        sm.current = 'Product_Screen'

    def click_product_detail_screen(self):
        sm.transition = WipeTransition(direction='right')
        sm.current = 'Product_Detail_Screen'

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
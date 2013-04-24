import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.app import App

import mysql.connector

cnx = mysql.connector.connect(user='karanvirsngh', password='ether0110',
                              host='SQL09.FREEMYSQL.NET',
                              database='karant')

cursor = cnx.cursor()

#cursor.execute("SELECT * FROM Writers WHERE Name=%s",("Jack London"))
cursor.execute("SELECT * FROM Writers")
karanvir="oi"
print cursor
for Name in cursor:
    print Name[1]
    karanvir=Name[1]
    
Builder.load_string('''
<HelloWorldScreen>:
    cols: 2
    Label:
        text: 'Welcome to the Hello world %s'%(root.karanvir)
    Button:
        text: 'Click me! %d' % root.counter
        on_release: root.my_callback()
    Button:
        text: 'Click me! %d' % root.counter
        on_release: root.my_callback()
    Bubble:
        BubbleButton:
            text: 'Cut'
        BubbleButton:
            text: 'Copy'
        BubbleButton:
            text: 'Paste'
    Slider:
        orientation: 'vertical'
    
''')

class HelloWorldScreen(GridLayout):
#    conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
#    cursor = conn.cursor()
#    cursor.execute("""CREATE TABLE albums
#                  (title text, artist text) 
#               """)
#               # insert some data
#    cursor.execute("INSERT INTO albums VALUES ('Glow', 'Andy Hunter')")
#    cursor.execute("INSERT INTO albums VALUES ('Blow', 'RAndy Junter')")
# 
#     # save data to database
#    conn.commit()
#    
#    cursor.execute('SELECT title FROM albums')
#    allentries=cursor.fetchall()
#    karanvir=allentries[1][0]
    karanvir=karanvir
    counter = NumericProperty(0)
    def my_callback(self):
        print 'The button have been pushed'
        self.counter += 1

class HelloWorldApp(App):
    def build(self):
        return HelloWorldScreen()

if __name__ == '__main__':
    
    #print 1
    HelloWorldApp().run()

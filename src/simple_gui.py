#!/usr/bin/env python3

from unicodedata import name
import rospy
from std_msgs.msg import Bool,Int8
from kivymd.app import MDApp
from kivy.lang import Builder


class BlahApp(MDApp):

    # defult code 
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('/home/gokulkrishna_s/gui_ws/src/ros_tutorials_gui/src/ros_gui.kv')
    
# used to display UI components in .kv file    
    def build(self):
        return self.screen

# used to publish true when button is pressed
    def my_function(self,*args):
        print("Button pressed")
        self.screen.ids.my_label.text='Button Pressed'
        self.screen.ids.my_button.md_bg_color= "red"
        msg = True
        pub.publish(msg)

# used to publish slider values when slider is moved
    def slider_function(self,slider_value):
        print(int(slider_value))
        msg = int(slider_value)
        slider_pub.publish(msg)


if __name__=='__main__':

    pub=rospy.Publisher('/button',Bool,queue_size=1)
    slider_pub=rospy.Publisher('/slider',Int8,queue_size=1)
    rospy.init_node('simple_gui',anonymous=True)
    BlahApp().run()
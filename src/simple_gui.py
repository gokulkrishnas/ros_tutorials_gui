#!/usr/bin/env python3

from unicodedata import name
import rospy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatIconButton


class BlahApp(MDApp):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.screen = Builder.load_file('/home/gokulkrishna_s/gui_ws/src/ros_tutorials_gui/src/ros_gui.kv')
    
    def build(self):
        
        return self.screen

if __name__=='__main__':
    rospy.init_node('simple_gui',anonymous=True)

    BlahApp().run()
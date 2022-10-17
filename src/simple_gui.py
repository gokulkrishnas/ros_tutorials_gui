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
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        return (
            MDScreen(
                MDRoundFlatIconButton(
                    text="Click here",
                    icon="language-python",
                    line_color=(0.25, 0.25, 0.25, 0.25),
                    size_hint=(0.15,0.15),
                    pos_hint={"center_x": .25, "center_y": .25},
                )
            )
        )
        #return self.screen

if __name__=='__main__':
    rospy.init_node('simple_gui',anonymous=True)

    BlahApp().run()
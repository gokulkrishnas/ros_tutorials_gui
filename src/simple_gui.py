from unicodedata import name
import rospy
from kivy.config import Config
Config.set('kivy','keyboard_mode','systemanddock')
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder


class BlahApp(MDApp):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.screen = Builder.load_file('/home/gokulkrishna_s/gui_ws/src/ros_tutorials_gui/src/ros_gui.kv')
    
    def build(self):
        return self.screen

if __name__=='__main__':
    # rospy.init_node('simple_gui',anonymous=True)

    BlahApp().run()
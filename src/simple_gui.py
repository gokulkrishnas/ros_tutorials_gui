from unicodedata import name
import rospy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton


class BlahApp(MDApp):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.screen = Builder.load_file('/home/gokulkrishna_s/gui_ws/src/ros_tutorials_gui/src/ros_gui.kv')
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return (
            MDScreen(
                MDRectangleFlatIconButton(
                    text="MDRectangleFlatIconButton",
                    icon="language-python",
                    line_color=(1, 1, 1, 1),
                    pos_hint={"center_x": .5, "center_y": .5},
                )
            )
        )
        return self.screen

if __name__=='__main__':
    # rospy.init_node('simple_gui',anonymous=True)

    BlahApp().run()
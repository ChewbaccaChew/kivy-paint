from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')


class TestApp(App):

    def build(self):
        return Button(text='This is Button!',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5},
                      font_size=22,
                      background_color=[0, 1, 0, 1],
                      background_normal='',
                      on_press=self.btn_press,
                      on_release=self.btn_free)

    def btn_press(self, instance):
        print('Button pressed')
        instance.text = 'Button pressed!'

    def btn_free(self, instance):
        instance.text = 'This is Button!'


if __name__ == '__main__':
    TestApp().run()

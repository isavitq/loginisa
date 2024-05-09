from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image

class LoginScreen(Screen):
    def _init_(self, **kwargs):
        super(LoginScreen, self)._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Labels
        label_login = Label(text="Login", size_hint_y=None, height=50)

        # Inputs
        self.input_email = TextInput(hint_text='Email', multiline=False, size_hint_y=None, height=50)
        self.input_senha = TextInput(hint_text='Senha', multiline=False, password=True, size_hint_y=None, height=50)

        # Buttons
        btn_entrar = Button(text="Entrar", size_hint_y=None, height=50)
        btn_cadastrar = Button(text="Cadastrar", size_hint_y=None, height=50)

        # Adding functionality to the buttons
        btn_entrar.bind(on_press=self.on_enter_click)
        btn_cadastrar.bind(on_press=self.on_register_click)

        self.oie = Image(source="/Users/aluno.sesipaulista/Downloads/oie.png")

        layout.add_widget(self.oie)
        layout.add_widget(label_login)
        layout.add_widget(self.input_email)
        layout.add_widget(self.input_senha)
        layout.add_widget(btn_entrar)
        layout.add_widget(btn_cadastrar)

        self.add_widget(layout)

    def on_enter_click(self, instance):
        # Handle the 'Entrar' button click
        pass

    def on_register_click(self, instance):
        # Handle the 'Cadastrar' button click
        pass

class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        return sm

if __name__ == '__main__':
    LoginApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class SimuladorLayout(BoxLayout):
    def generar_tarjeta(self):
        self.ids.resultado.text = "Tarjeta generada: 4001 1234 5678 9010\nPIN: 1234"

class SimuladorApp(App):
    def build(self):
        return SimuladorLayout()

if __name__ == '__main__':
    SimuladorApp().run()

from kivy.app import App
from kivy.lang import Builder

author = 'Thomas Cornes'

MILES_TO_KM = 1.6


class MilesConverterApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    def handle_calculate(self):
        value = self.validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()

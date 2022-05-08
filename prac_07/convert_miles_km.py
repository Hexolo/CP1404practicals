from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETRES = 1.60934


class DistanceConversionApp(App):

    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        miles = self.get_validated_miles()
        km = miles * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(km)

    def handle_increment(self, change):
        number = self.get_validated_miles() + change
        self.root.ids.input_number.text = str(number)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            number = float(self.root.ids.input_number.text)
            return number
        except ValueError:
            return 0


DistanceConversionApp().run()

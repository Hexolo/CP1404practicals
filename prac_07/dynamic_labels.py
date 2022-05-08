from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicWidgetApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct Main App"""
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456", "OJ "
                                                                                                               "Simpson": "0984536869"}

    def build(self):
        """Build Kivy Gui"""
        self.title = "Dynamic Widget"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widget()
        return self.root

    def create_widget(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for name in self.name_to_phone:
            # create a button for each data entry, specifying the text and id
            # (although text and id are the same in this case, you should see how this works)
            temp_label = Label(text=name)
            # add the button to the "entries_box" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicWidgetApp().run()

from PyQt5 import QtWidgets, uic

from rena.presets.presets_utils import set_stream_preset_info, set_preset_value


class CustomPropertyWidget(QtWidgets.QWidget):
    def __init__(self, parent, stream_name, property_entry, property_name, property_value):
        """
        :param lsl_data_buffer: dict, passed by reference. Do not modify, as modifying it makes a copy.
        :rtype: object
        """
        super().__init__()
        self.parent = parent
        self.ui = uic.loadUi("ui/CustomPropertyWidget.ui", self)

        self.stream_name = stream_name
        self.property_entry = property_entry
        self.property_name = property_name

        self.set_property_label(property_name)
        self.set_property_value(property_value)

        self.PropertyLineEdit.textChanged.connect(self.update_value_in_settings)

    def set_property_label(self, label_name):
        self.PropertyLabel.setText(label_name)

    def set_property_value(self, value):
        self.PropertyLineEdit.setText(str(value))

    def update_value_in_settings(self):
        set_preset_value(self.property_entry, self.property_name, self.PropertyLineEdit.text())


class IntCustomPropertyWidget(CustomPropertyWidget):

    def __init__(self, parent, stream_name, property_entry, property_name, property_value):
        super().__init__(parent, stream_name, property_entry, property_name, property_value)


# class IntCustomPropertyWidget(CustomPropertyWidget):
#     def __init__(self, parent, stream_name, entry, property_name, property_value):
#         super().__init__(parent, stream_name, property_name, property_value)
#
#     def update_value_in_settings(self):
#         setattr()
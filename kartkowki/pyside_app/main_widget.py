from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QLineEdit, QCheckBox, QPushButton, QListWidget, QListWidgetItem, \
    QMessageBox


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Kartkowka")
        self.edit_line = QLineEdit(self)
        self.checkbox = QCheckBox(self)
        button = QPushButton(self)
        self.list = QListWidget(self)

        button.clicked.connect(self.add_record)
        self.list.itemClicked.connect(self.show_info)

        layout = QGridLayout(self)
        layout.addWidget(self.edit_line, 0, 0, 1, 2)
        layout.addWidget(self.checkbox, 1, 0)
        layout.addWidget(button, 2, 0, 1, 2)
        layout.addWidget(self.list, 3, 0, 1, 2)

    def __check_exist(self, record):
        records = [self.list.item(i).text() for i in range(self.list.count())]
        return record in records

    def __get_item(self):
        text, counter, is_checked = self.list.currentItem().data(Qt.UserRole)
        counter += 1
        self.list.currentItem().setData(Qt.UserRole, (text, counter, is_checked))

        return text, counter, is_checked

    def add_record(self):
        text = self.edit_line.text()

        if len(text) and not self.__check_exist(text):
            item = QListWidgetItem(text)
            is_checked = self.checkbox.isChecked()
            item.setData(Qt.UserRole, (text, 0, is_checked))
            self.list.addItem(item)
            self.edit_line.clear()

    def show_info(self):
        text, counter, is_checked = self.__get_item()

        if counter < 2:
            QMessageBox.information(self, "item", f"text: {text}\nis checked: {is_checked}")
        else:
            self.list.takeItem(self.list.row(self.list.currentItem()))

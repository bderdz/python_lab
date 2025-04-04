from PySide6.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QLabel, QMessageBox

from fraction.fraction import Fraction


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculator")

        self.left_numerator = QLineEdit(self)
        self.left_denominator = QLineEdit(self)
        self.operation = QLineEdit(self)
        self.right_numerator = QLineEdit(self)
        self.right_denominator = QLineEdit(self)
        button = QPushButton("=", self)
        self.result_numerator = QLabel(self)
        self.result_denominator = QLabel(self)

        button.clicked.connect(self.calculate)

        layout = QGridLayout(self)
        layout.addWidget(self.left_numerator, 0, 0)
        layout.addWidget(self.left_denominator, 1, 0)
        layout.addWidget(self.operation, 0, 1, 2, 1)
        layout.addWidget(self.right_numerator, 0, 2)
        layout.addWidget(self.right_denominator, 1, 2)
        layout.addWidget(button, 0, 3, 2, 1)
        layout.addWidget(self.result_numerator, 0, 4)
        layout.addWidget(self.result_denominator, 1, 4)

    def calculate(self):
        try:
            sign = self.operation.text()
            a = Fraction(int(self.left_numerator.text()), int(self.left_denominator.text()))
            b = Fraction(int(self.right_numerator.text()), int(self.right_denominator.text()))
            result = a

            match sign:
                case "+":
                    result += b
                case "-":
                    result -= b
                case "*":
                    result *= b
                case "/":
                    result /= b

            self.result_numerator.setText(str(result.numerator))
            self.result_denominator.setText(str(result.denominator))
        except Exception as e:
            QMessageBox.critical(self, "Error", e.__str__())
            return

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QGridLayout, QWidget, QPushButton, QVBoxLayout

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator App")
        self.setGeometry(100, 100, 800, 600)  # Adjusted window size

        # Create a central widget and set layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a text area for input on the top
        self.input_area = QTextEdit()
        self.input_area.setFixedHeight(100)  # Set a fixed height for the input area
        layout.addWidget(self.input_area)

        # Create financial functions keypad
        self.create_financial_keypad(layout)

        # Create numeric keypad with arithmetic operators
        self.create_numeric_keypad(layout)

        # Create statistical functions keypad
        self.create_statistical_keypad(layout)

        # Create a results area with scrollbars
        self.create_results_area(layout)

    def create_financial_keypad(self, layout):
        financial_layout = QGridLayout()
        financial_buttons = [
            'PV', 'FV', 'Rate',
            'Periods', 'Compounding', 'Amortization'
        ]

        for i, button in enumerate(financial_buttons):
            btn = QPushButton(button)
            btn.clicked.connect(lambda checked, b=button: self.on_button_click(b))
            financial_layout.addWidget(btn, i // 3, i % 3)

        layout.addLayout(financial_layout)

    def create_numeric_keypad(self, layout):
        numeric_layout = QGridLayout()
        numeric_buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'Clear', '=', '+'
        ]

        for i, button in enumerate(numeric_buttons):
            btn = QPushButton(button)
            btn.clicked.connect(lambda checked, b=button: self.on_button_click(b))
            numeric_layout.addWidget(btn, i // 4, i % 4)  # Adjusted to 4 columns

        layout.addLayout(numeric_layout)

    def create_statistical_keypad(self, layout):
        statistical_layout = QGridLayout()
        statistical_buttons = [
            'Average', 'Std Dev', 'Min',
            'Max'
        ]

        for i, button in enumerate(statistical_buttons):
            btn = QPushButton(button)
            btn.clicked.connect(lambda checked, b=button: self.on_button_click(b))
            statistical_layout.addWidget(btn, i // 2, i % 2)

        layout.addLayout(statistical_layout)

    def create_results_area(self, layout):
        # Create a scroll area for the results
        self.results_area = QTextEdit()
        self.results_area.setReadOnly(True)  # Make it read-only
        self.results_area.setFixedHeight(200)  # Set a fixed height for the results area
        layout.addWidget(self.results_area)

    def on_button_click(self, button):
        if button == 'Clear':
            self.input_area.clear()  # Clear the input area
            self.results_area.clear()  # Clear the results area
        elif button == '=':
            # Here you can implement the calculation logic
            # For now, let's just display the input in the results area
            self.results_area.setPlainText(self.input_area.toPlainText())
        else:
            current_text = self.input_area.toPlainText()
            self.input_area.setPlainText(current_text + button + ' ')  # Append button value to input area

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())


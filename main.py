import sys
from datetime import datetime

from PyQt6.QtWidgets import QApplication,QLabel, QWidget, QGridLayout, QLineEdit, QPushButton


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age calculator")
        grid = QGridLayout()
        self.setLayout(grid)

        #create widgets
        name_label = QLabel("Name: ")
        self.name_line_edit = QLineEdit()

        dob_label = QLabel("Date of Birth DD/MM/YYYY: ")
        self.dob_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel()

        #add widgets to grid
        grid.addWidget(name_label,0, 0)
        grid.addWidget(self.name_line_edit,0,1)
        grid.addWidget(dob_label,1,0)
        grid.addWidget(self.dob_line_edit,1,1)
        grid.addWidget(calculate_button,2,0,1,2)
        grid.addWidget(self.output_label,3,0,1,2)

    def calculate_age(self):
        try:
            current_year = datetime.now().year
            date_of_birth =self.dob_line_edit.text()
            name = self.name_line_edit.text()
            year_of_birth = datetime.strptime(date_of_birth,"%d/%m/%Y").date().year
            age = current_year - year_of_birth
            self.output_label.setText(f"{name} is {age} years old")

        except ValueError:
            error_text="Please enter Name and DOB correctly"
            self.output_label.setText(error_text)



app=QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())

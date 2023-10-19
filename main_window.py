''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)

window = QWidget()

# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
btn_Menu = QPushButton('Меню')
# кнопка прибирає вікно і повертає його після закінчення таймера
btn_Sleep = QPushButton('Відпочити')
# введення кількості хвилин
box_Time = QSpinBox()
box_Time.setValue(30)
lb_Time = QLabel('секунд')
# кнопка відповіді "Ок" / "Наступний"
btn_OK = QPushButton('Відповісти')
# текст питання
lb_Question = QLabel('1')

# Опиши групу перемикачів
radio_group_box = QGroupBox('Варіанти відповідей')
radio_group = QButtonGroup()

rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('1')
rbtn_3 = QRadioButton('1')
rbtn_4 = QRadioButton('1')

radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)

# Опиши панень з результатами
answer_group_box = QGroupBox('Результат тесту')
lb_Resultat = QLabel('') # правильно / неправильно
lb_Correct = QLabel('') # правильна відповідь

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()
layout_h3 = QHBoxLayout()
layout_v1 = QVBoxLayout()
layout_v2 = QVBoxLayout()
layout_h4 = QHBoxLayout()


layout_h1.addWidget(btn_Menu)
layout_h1.addStretch(1)
layout_h1.addWidget(btn_Sleep)
layout_h1.addWidget(box_Time)
layout_h1.addWidget(lb_Time)

layout_h2.addWidget(lb_Question)

layout_v1.addWidget(rbtn_1)
layout_v1.addWidget(rbtn_2)
layout_v2.addWidget(rbtn_3)
layout_v2.addWidget(rbtn_4)
layout_h3.addLayout(layout_v1)
layout_h3.addLayout(layout_v2)
radio_group_box.setLayout(layout_h3)

layout_v3 = QVBoxLayout()
layout_v3.addWidget(lb_Resultat)
layout_v3.addWidget(lb_Correct)
answer_group_box.setLayout(layout_v3)
answer_group_box.hide()



layout_h4.addWidget(btn_OK)

line = QVBoxLayout()
line.addLayout(layout_h1, stretch=1)
line.addLayout(layout_h2, stretch=2)
line.addWidget(radio_group_box, stretch=8)
line.addWidget(answer_group_box, stretch=8)
line.addStretch(1)
line.addLayout(layout_h4)
line.addStretch(1)
line.addSpacing(5)

window.setLayout(line)
window.resize(550, 450)


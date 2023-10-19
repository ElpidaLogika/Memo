from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])

from main_window import *
from menu_window import *

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0      # кількість відповідей
        self.count_right = 0    # кількість правильних відповідей
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

questions = [q1, q2, q3, q4] 
radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 

def new_question():
    global curent_question
    curent_question = choice(questions)

    lb_Question.setText(curent_question.question)
    lb_Correct.setText(curent_question.answer)

    shuffle(radio_buttons)
    radio_buttons[0].setText(curent_question.answer)
    radio_buttons[1].setText(curent_question.wrong_answer1)
    radio_buttons[2].setText(curent_question.wrong_answer2)
    radio_buttons[3].setText(curent_question.wrong_answer3)

new_question()

def check():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_Correct.text():
                curent_question.got_right()
                lb_Resultat.setText('Вірно!')
                break
    else:
        lb_Resultat.setText('Не вірно!')
        curent_question.got_wrong()

    

def click_ok():
    if btn_OK.text() == 'Відповісти':
        check()
        # rbtn_1.hide()
        # rbtn_2.hide()
        # rbtn_3.hide()
        # rbtn_4.hide()
        radio_group_box.hide()
        answer_group_box.show()
        btn_OK.setText('Наступне запитання')
    else:
        new_question()
        # rbtn_1.show()
        # rbtn_2.show()
        # rbtn_3.show()
        # rbtn_4.show()
        radio_group_box.show()
        answer_group_box.hide()
        btn_OK.setText('Відповісти')

btn_OK.clicked.connect(click_ok)


def menu_generation():
    if curent_question.count_ask == 0:
        stat = 0
    else:
        stat = int(curent_question.count_right / curent_question.count_ask * 100)
    
    text = f'Разів відповіли: {curent_question.count_ask}\nВірних відповідей: {curent_question.count_right}\nУспішність: {stat}%'
    lb_statistic.setText(text)
    menu.show()
    window.hide()

btn_Menu.clicked.connect(menu_generation)

def back_menu():
    menu.hide()
    window.show()

btn_back.clicked.connect(back_menu)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),
                     le_wrong_ans1.text(), le_wrong_ans2.text(),
                     le_wrong_ans3.text())

    questions.append(new_q)
    clear()


btn_add.clicked.connect(add_question)

window.show()
app.exec_()

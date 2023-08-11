# напиши здесь код третьего экрана приложения
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from instr import *
class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self. initUI()
        self.set_appear()
        self.show()
    def results(self):
        if self.exp.person.age < 7:
            self.index = 0
            return 'Возраст должен быть больше 7 лет'

        self.index = (4 * (int(self.exp.test1) + int(self.exp.test2) + int(self.exp.test3)) - 200) / 10
        if self.exp.person.age == 7 or self.exp.person.age == 8:
            if self.index > 21:
                return txt_res1
            elif 21 > self.index >= 17:
                return txt_res2
            elif 17 > self.index >= 12:
                return txt_res3 
            elif 12 > self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.age == 9 or self.exp.person.age == 10:
            if self.index > 19.5:
                return txt_res1
            elif 19.5 > self.index >= 15.5:
                return txt_res2
            elif 15.5 > self.index >= 10.5:
                return txt_res3 
            elif 10.5 > self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.age == 11 or self.exp.person.age == 12:
            if self.index > 18:
                return txt_res1
            elif 18 > self.index >= 14:
                return txt_res2
            elif 14 > self.index >= 9:
                return txt_res3 
            elif 9 > self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.age == 13 or self.exp.person.age == 14:
            if self.index > 16.5:
                return txt_res1
            elif 16.5 > self.index >= 12.5:
                return txt_res2
            elif 12.5 > self.index >= 7.5:
                return txt_res3 
            elif 7.5 > self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.age >= 15:
            if self.index > 15:
                return txt_res1
            elif 15 > self.index >= 11:
                return txt_res2
            elif 11 > self.index >= 6:
                return txt_res3 
            elif 6 > self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5
    def initUI(self):
        self.heart_text = QLabel(txt_heartwork + self.results())
        self.index_r = QLabel(txt_index + str(self.index))
        self.line = QVBoxLayout()
        self.line.addWidget(self.index_r)
        self.line.addWidget(self.heart_text)
        self.setLayout(self.line)
        self.setStyleSheet('font-size: 48px')
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

import pyautogui
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Gui

#实例化主窗口
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Gui.Ui_MainWindow()
        self.ui.setupUi(self)

#创建存储数据类
class Save_Data:
    mouse_choose = ''
    click_way = ''

#*********************************** RidioButton触发函数 ***********************************#
def radiobutton1():
    if gui.ui.mouse_choose_rb1.isChecked():
        Save_Data.mouse_choose = 'left'
    else:
        Save_Data.mouse_choose = 'right'

def radiobutton2():
    if gui.ui.click_way_rb1.isChecked():
        Save_Data.click_way = 1
    else:
        Save_Data.click_way = 2

#*********************************** 选择点击位置函数 ***********************************#
def choose_pos(*event):
    pos_x,pos_y = pyautogui.position()
    click_pos = " "+str(pos_x)+","+str(pos_y)+" "
    gui.ui.click_pos_le.setText(click_pos)

#*********************************** 开始点击函数 ***********************************#
def start_click(*event):

    try:
        click_pos = eval(gui.ui.click_pos_le.text())
        interval_data = float(gui.ui.interval_le.text())
        click_time = int(gui.ui.click_time_le.text())

        for i in range(click_time):
            pyautogui.moveTo(click_pos,duration = 0.001)
            pyautogui.click(clicks = Save_Data.click_way,
            duration=0,
            button = Save_Data.mouse_choose,
            interval = interval_data)
        pyautogui.alert("执行完成!")
    except ValueError:
        pyautogui.alert("参数设置错误，请重新输入正确的参数!")
    except SyntaxError:
        pyautogui.alert("参数设置错误，请重新输入正确的参数!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainWindow()

    # *********************************** 触发函数设置 ***********************************#
    gui.ui.mouse_choose_rb1.toggled.connect(radiobutton1)
    gui.ui.click_way_rb1.toggled.connect(radiobutton2)

    gui.ui.choose_pos_btn.clicked.connect(choose_pos)
    gui.ui.start_btn.clicked.connect(start_click)
    #设置快捷键
    gui.ui.choose_pos_btn.setShortcut("F9")
    gui.ui.start_btn.setShortcut("F10")

    # *********************************** LineEdit设置范围 ***********************************#
    TimeValidator = QIntValidator(1, 9999999)
    gui.ui.click_time_le.setValidator(TimeValidator)
    gui.ui.interval_le.setValidator(QDoubleValidator())

    gui.show()
    sys.exit(app.exec_())
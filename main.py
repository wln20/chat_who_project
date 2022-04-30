import pyautogui
import time

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget
from functools import partial

import Project_GUI         #GUI的代码文件名为Project_GUI.py

def openWechat():
    pyautogui.hotkey("ctrl","alt","w") #TODO 这是打开微信的快捷键
    time.sleep(0.1)
def closeWechat():
    pyautogui.hotkey("ctrl", "alt", "w")
import pyperclip
# TODO 定义一个查询联系人的函数，参数为name
def chatWho(name):
    # TODO 使用hotkey函数，操作按键"command","f"，打开搜索
    pyautogui.hotkey("ctrl","f")
    # TODO 使用pyperclip模块中的copy函数，复制微信号name到剪贴板
    pyperclip.copy(name)
    # TODO 使用hotkey函数，操作按键"command", "v"，粘贴微信号
    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)
    # TODO 使用hotkey函数，操作按键"return"，确认搜索
    pyautogui.hotkey("enter")
    time.sleep(0.5)
def sentMsg(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey("ctrl","v")
    pyautogui.hotkey("enter")

def ConvertAndDo(ui):
    nam = ui.lineEdit.text()        #利用Line Edit的text()方法获取文本
    txt = ui.textEdit.toPlainText()  #利用Text Edit的toPlainText()方法获取文本
    n = int(ui.lineEdit_3.text())
    f = float(ui.lineEdit_4.text())

    openWechat()
    chatWho(nam)
    for i in range(n):
        sentMsg(txt)
        time.sleep(1/f)   #调整等待时间
    closeWechat()
    pyautogui.alert('Message successfully sent!')
if __name__ == "__main__":

    while True:
        i = pyautogui.prompt('Username:')
        if i==None:
            sys.exit()
        j = pyautogui.password('Password:')  # 返回输入的字符串，直接关闭则返回None
        if j == '19260817':
            pyautogui.alert('Welcome, '+i+'！')
            break
        elif j==None:
            sys.exit()
        else:
            pyautogui.alert('Sorry, your password is incorrect, please try again.')

    app = QApplication(sys.argv) #构造一个应用对象
    MainWindow = QMainWindow()
    ui = Project_GUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.lineEdit_4.setText(str(10))    #默认频率为10
    pyautogui.alert('Notice:\n    由于本程序是基于热键（hotkey）实现的，因此使用前需要先确保微信电脑版相应热键开启。（如果没有自己乱改过的话，就是系统默认的快捷键即可）\n    具体为：微信电脑版>设置>快捷键。“发送消息”应为Enter；“打开微信”应为Ctrl+Alt+W。\n    在使用程序前，请确保已经登陆微信，并处于最小化状态（也即现在微信处于后台运行状态）。\n    iBuena Suerte!')
    ui.pushButton.clicked.connect(partial(ConvertAndDo, ui)) #点击按钮，执行槽中内容：ConvertAndDo函数
    sys.exit(app.exec_())  #关闭窗口后，结束程序

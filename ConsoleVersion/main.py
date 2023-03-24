from os import system
from time import sleep
from math import floor
from threading import Thread
import colorama
from urwid.old_str_util import get_width

class LifeSimulator:
    def __init__(self):
        self.focus = None
        self.Width = 100
        self.Height = 30
        system("mode con cols={} lines={}".format(str(self.Width), str(self.Height)))
    def calcWidth(self, string):
        temp = 0
        for i in range(len(string)):
            temp += get_width(ord(string[i]))
        return temp
    
    def judge(self, number):
        n1=str(float(number)).split('.')
        if n1[1]=='0': # 非小数
            return False
        else:
            return True
    
    def printStrWithLRFrame(self, string):
        '''
        输出带左右框的文字
        '''
        print("| " + string, end="")
        for i in range(self.Width - self.calcWidth(string) - 5):
            print(" ", end="")
        print(" |")
    
    def printDevideLine(self, string, fill = "-"):
        # 左侧间隔
        LeftR = (self.Width - self.calcWidth(string))/2
        offset = 1 if self.judge(LeftR) else 0
        LeftR = int(LeftR)
        for i in range(LeftR - offset):
            print("-", end="")
        print(string, end="")
        for i in range(LeftR + offset - 1):
            print("-", end="")
        print("-")
          
    def calcData(self):
        self.temp = 0
        def _calcData():
            while True:
                self.temp+=1
                
                # 限定每帧刷新率
                sleep(1/60)
        thread = Thread(target=_calcData)
        thread.setDaemon(True)
        thread.start()
    
    def button(self, string, function, autoSwitchLine, LandRSpacing: list):
        if autoSwitchLine:
            printButtonText = string.split("\n")
        else:
            printButtonText = [string]
    
    def mainLoop(self):
        self.calcData()
        while True:
            system("cls")
            self.printDevideLine("LifeSimulator")
            self.printStrWithLRFrame(str(self.temp))
            self.printDevideLine("-")
            sleep(1/30)


LifeSimulatorAll = LifeSimulator()
LifeSimulatorAll.mainLoop()
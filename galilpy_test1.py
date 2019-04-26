import sys
import string
import gclib
import matplotlib.pyplot as plt
import numpy as np
import time
from math import *

def print_plot():
	for i in range(200):
		plt.clf() #清空画布上的所有内容
		t_now = i*0.1
		#t_now = float(g.GCommand('time=?'))/1000
		t.append(t_now)#模拟数据增量流入，保存历史数据
		m.append(float(g.GCommand('RealVol=?')))#模拟数据增量流入，保存历史数据
		n.append(float(g.GCommand('RealVol2=?')))#模拟数据增量流入，保存历史数据
		plt.plot(t,m,'-r')
		plt.plot(t,n,'-b')
		plt.pause(0.01)

    
if __name__ == "__main__":
    print('Start, do your best!')
    t = [0]
    t_now = 0
    m = [sin(t_now)]
    n = [sin(t_now)]
    g = gclib.py() #make an instance of the gclib python class
    try:
        print('gclib version:', g.GVersion())
        g.GOpen('/dev/ttyUSB1 --baud 115200 --direct')
        print(g.GInfo())
        plt.ion() #开启interactive mode 成功的关键函数
        plt.figure(1)
    
    except gclib.GclibError as e:
        print('Unexpected GclibError:', e)   
    
    else:
	    print(g.GCommand('RealVol=?'))
	    print_plot()
	    plt.savefig("/home/why/doyle_why/galil_test/Python_work/py_test1/1.png")

    finally:
        g.GClose() #don't forget to close connections!
        print('gclib closed!')

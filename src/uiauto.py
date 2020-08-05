# -*- coding: utf-8 -*-
# @Author: Feng Heliang
# @Date:   2020-07-08 16:34:41
# @Last Modified by:   Feng Heliang
# @Last Modified time: 2020-08-04 14:24:51
import subprocess
import os
import sys
from Ui_main_Agent import Ui_main_Agent as uma

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uiautomation as auto
auto.uiautomation.SetGlobalSearchTimeout(15)  # 设置全局搜索超时 15


def start_process(process_path):
    subprocess.Popen(process_path)


def main():
    # 打开程序主窗口
    main_window = uma.instance()
    main_window.show_ui()

    # time.sleep(3)
    # control = auto.GetFocusedControl()
    # auto.EnumAndLogControl(control, 0xFFFFFFFF, True, startDepth=0)

    # # 找到Startup窗口
    # startupWin = None
    # for win in auto.GetRootControl().GetChildren():
    #     if win.Name == 'Startup':
    #         startupWin = win
    #         break
    # if not startupWin:
    #     auto.Logger.WriteLine("Can't find Startup Window",
    #                           auto.ConsoleColor.Red)
    #     exit()
    # # 找到Treatment Button, 并进行点击
    # treatmentTextControl = startupWin.Control(searchDepth=9, Name="治疗/计划QA")
    # treatmentTextControl.Click()
    # # 等待CCS窗口展现
    # time.sleep(10)
    # auto.Logger.SetLogFile("uiauto_log.txt")
    # auto.Logger.WriteLine('Open Treatment Scene Successfully',
    #                       auto.ConsoleColor.Blue)


if __name__ == '__main__':
    main()

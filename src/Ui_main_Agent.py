# -*- coding: utf-8 -*-
# @Author: Feng Heliang
# @Date:   2020-07-17 10:51:15
# @Last Modified by:   Heliang
# @Last Modified time: 2020-08-01 13:37:08
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
from PyQt5.QtWidgets import (QMessageBox, QTableWidgetItem, QFileDialog,
                             QTextEdit, QAbstractItemView)
from views.Ui_main import Ui_MainWindow
import sys
import os
import subprocess
from logger import MyLogger as mlog
import time
import uiautomation as auto
import json


class Ui_main_Agent(QtWidgets.QMainWindow, Ui_MainWindow):
    """对于Ui_MainWindow的继承

    Args:
        QtWidgets ([type]): [Ui_MainWindow的基类]
        Ui_MainWindow ([type]): [基类Ui_MainWindow]
    """

    _instance = None
    _exec_path = ""
    _app: QtWidgets.QApplication = None

    @classmethod
    def instance(cls) -> "Ui_main_Agent":
        """Singleton instance (this prevents com creation on import)."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        """初始化

        Args:
            parent ([type], optional): 父窗口. Defaults to None.
        """
        self._app = QtWidgets.QApplication(sys.argv)

        super().__init__(None)
        self.setupUi(self)

        # 设置tableWidget显示模式
        self._init_ui()

    def _create_textEdit(self, text, maximumHeight=180, minimumHeight=180):
        tempTextEdit = QTextEdit()
        tempTextEdit.setMaximumHeight(180)
        tempTextEdit.setMinimumHeight(180)
        tempTextEdit.setText(text)

        return tempTextEdit

    def _init_ui(self):
        """添加新的UI元素
        """
        # 设置tableWidget显示模式
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 设置verticalLayout3的控件为顶对齐
        self.verticalLayout3.setAlignment(QtCore.Qt.AlignTop)        

        # 挂载slot
        self.select_button.clicked.connect(self._slot_btn_select)
        self.run_button.clicked.connect(self._slot_btn_run)
        self.analyze_button.clicked.connect(self._slot_btn_analyze)
        self.add_button.clicked.connect(self._slot_btn_add)
        self.clear_button.clicked.connect(self._slot_btn_clear)
        self.save_btn.clicked.connect(self._slot_btn_save)

    def show_ui(self):
        """显示窗体
        """
        if self:
            self.show()
        sys.exit(self._app.exec_())

    @property
    def exec_path(self):
        """exec_path属性getter      
        """
        if self:
            self._exec_path = os.path.abspath(
                str.strip(self.textBrowser.toPlainText()))

            if len(self.textBrowser.toPlainText()) != 0:
                mlog.instance().logger.info(
                    "current execuable is " +
                    str.strip(self.textBrowser.toPlainText()))

        return self._exec_path

    def _slot_btn_select(self):
        """slot of choose_button, 选择要分析的可执行程序
        """
        file_name, file_type = QFileDialog.getOpenFileName(
            self, "选取文件", os.getcwd(), "Exe Files (*.exe)")
        mlog.instance().logger.info("Choose File {}", file_name)
        if file_name != "":
            self.textBrowser.setText(file_name)

    def _slot_btn_run(self):
        """slot of run_button, 运行要分析的可执行程序
        """
        # 判断可执行程序路径是否正确
        if (not os.path.exists(self.exec_path)) or (len(self.exec_path) == 0):
            QMessageBox.warning(self, r"警告", r"请输入有效的可执行程序路径！",
                                QMessageBox.Yes)
        else:
            try:
                # 打开可执行程序
                subprocess.Popen(self.exec_path)
            except Exception as e:
                QMessageBox.critical(self, r"错误", r"运行程序失败！", QMessageBox.Yes)
                mlog.instance().logger.error("运行程序识别，异常原因：{}", repr(e))

    def _slot_btn_analyze(self):
        """slot of analyze_button, 分析前台的应用，获取其窗体的控件列表，并填入到表格中"""
        row_index = 1

        for ctype, clsname, rect, name, handle, depth in self._get_control_infos(
        ):
            self.tableWidget.insertRow(row_index)
            self.tableWidget.setItem(row_index, 0,
                                     QTableWidgetItem(str(ctype)))
            self.tableWidget.setItem(row_index, 1, QTableWidgetItem(clsname))
            self.tableWidget.setItem(row_index, 2, QTableWidgetItem(rect))
            self.tableWidget.setItem(row_index, 3, QTableWidgetItem(name))
            self.tableWidget.setItem(row_index, 4, QTableWidgetItem(handle))
            self.tableWidget.setItem(row_index, 5, QTableWidgetItem(depth))

            row_index = row_index + 1

    def _slot_btn_add(self):
        """点击Move button,将左侧列表中选中的控件信息以json的形式写入到右侧的TextEdit控件中
        """
        item_info_dict = {}
        # 添加节点属性
        for item in self.tableWidget.selectedItems():
            mlog.instance().logger.info(
                "Current column name is {}, and current item value is {}".
                format(
                    self.tableWidget.item(0, item.column()).text(),
                    item.text()))

            column_name = self.tableWidget.item(0, item.column()).text()
            item_value = item.text()
            item_info_dict[column_name] = item_value

        # 添加操作属性
        item_info_dict['Action'] = 'click'
        item_info_dict['Pre-wait'] = '0'
        item_info_dict['Post-wait'] = '5'
        # Dump成Json格式
        item_info_json = json.dumps(item_info_dict, sort_keys=False, indent=1)
        # 附加到TextEdit
        # self.jsonTextEdit.append(item_info_json)
        self.verticalLayout3.addWidget(self._create_textEdit(item_info_json))

    def _slot_btn_clear(self):
        """清空jsonTextEdit"""
        block_count = self.jsonTextEdit.document().blockCount()
        self.jsonTextEdit
        self.jsonTextEdit.clear()
        self.jsonTextEdit.setText(str.format('clear block {}', block_count))

    def _slot_btn_save(self):
        """保存当前脚本
        """
        if self.scriptVerticalLayout.count() > 0:
            pass

    def _get_control_infos(self, seconds=3):
        """获取焦点所在应用的所有窗体控件，并便利输出控件信息

        Args:
            seconds (int, optional): 点击后n秒开始分析. Defaults to 3.

        Yields:
            [tuple]: 窗体上所有控件的信息
        """
        time.sleep(seconds)

        control = auto.GetFocusedControl()
        if control:
            for c, d in auto.WalkControl(control, True):
                mlog.instance().logger.info(c.ControlTypeName + " " + str(d))
                yield (
                    c.ControlType,
                    c.ClassName,
                    "[{},{},{},{}]".format(
                        c.BoundingRectangle.left,
                        c.BoundingRectangle.top,
                        c.BoundingRectangle.right,
                        c.BoundingRectangle.bottom,
                    ),
                    c.Name,
                    "0x{0:X}({0})".format(c.NativeWindowHandle),
                    str(d),
                )

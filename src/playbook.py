# -*- coding: utf-8 -*-
# @Author: Heliang
# @Date:   2020-08-01 14:04:19
# @Last Modified by:   Heliang
# @Last Modified time: 2020-08-01 14:58:05
import json
from logger import MyLogger as mlog
import os, sys


class PlaybookManager:
    """脚本管理类
    """

    _current_playbook_name = ""
    _playbook_content_dict = {}

    def __init__(self):
        super().__init__()

    def save(self, playbook_name):
        """将当前playbook的内容保存到指定文件中

        Args:
            playbook_name (str): 制定的文件名称

        Returns:
            int: 0 失败；1 成功
        """
        if not self._playbook_content_dict:
            mlog.instance().logger.error(
                f"{self.__class__.__name__} {sys._getframe().f_code.co_name}: playbook content dict is empty."
            )
            return 0
        elif not self.validate(self._playbook_content_dict):
            mlog.instance().logger.error(
                f"{self.__class__.__name__} {sys._getframe().f_code.co_name}: validate playbook content failed."
            )
            return 0
        else:
            try:
                with open(playbook_name, "w+") as fp:
                    fp.writelines(json.dumps(self._playbook_content_dict, indent=1))
                    mlog.instance().logger.info(
                        f"{self.__class__.__name__} {sys._getframe().f_code.co_name}: save into {playbook_name} successfully"
                    )
            except Exception as e:
                mlog.instance().logger.error(
                    f"{self.__class__.__name__} {sys._getframe().f_code.co_name}: save json_str into {playbook_name} error: {e}"
                )

            return 1

    def validate(self, content):
        return True

    def add(self, sub_content):
        """向playbook_content中添加子节点

        Args:
            sub_content (dict): 子节点

        Returns:
            int: 0 失败; 1 成功
        """
        if type(sub_content) != dict:
            mlog.instance().logger.error(
                f"{self.__class__.__name__} {sys._getframe().f_code.co_name}: {sub_content} is not a dict"
            )
            return 0
        else:
            key = f"step[{self._playbook_content_dict.items().count + 1}]"
            self._playbook_content_dict[key] = sub_content
            mlog.instance().logger.info(
                f"{self.__class__.__name__} {sys._getframe().f_code.co_name}: {key}:{sub_content} added"
            )
            return 1

    def load(self, playbook_name):
        """从制定的文件中读取playbook，文件应为json格式

        Args:
            playbook_name (str): 指定的文件名称

        Returns:
            int: 0 失败；1 成功
        """
        if len(playbook_name) == 0:
            mlog.instance().logger.error(
                f"{self.__class__.__name__} {sys._getframe().f_code.co_name}: {playbook_name} is empty"
            )
            return 0
        elif not os.path.isfile(playbook_name):
            mlog.instance().logger.error(
                f"{self.__class__.__name__} {sys._getframe().f_code.co_name}: {playbook_name} is not a file"
            )
            return 0
        else:
            try:
                with open(playbook_name, "r") as fp:
                    self._playbook_content_dict = json.load(fp)
            except Exception as e:
                mlog.instance().logger.error(
                    f"{self.__class__.__name__} {sys._getframe().f_code.co_name}: load from  {playbook_name} error: {e}"
                )
                return 0
            return 1

    def get_playbook_content(self):
        """获取playbook内容
        
        Returns:
            dict: 装载playbook内容的字典
        """
        return self._playbook_content_dict

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===============================================================================
#
# Copyright (c) 2018 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/py-clause/clause/tst-demo.py
# Author: Hai Liang Wang
# Date: 2019-09-11:22:09:30
#
# ===============================================================================

"""
Clause Client   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2018 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2019-09-11:22:09:30"

import os
import sys

curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curdir, ".."))

if sys.version_info[0] < 3:
    # raise "Must be using Python 3"
    pass
else:
    unicode = str

# Get ENV
ENVIRON = os.environ.copy()

from time import sleep

from absl import flags  # absl-py
from absl import logging  # absl-py
from absl import app  # absl-py

FLAGS = flags.FLAGS
flags.DEFINE_string('CL_HOST', "127.0.0.1", 'Clause Server\'s IP')
flags.DEFINE_integer('CL_PORT', 8056, 'Clause Server\'s Port')

from clause import Client, Data
from clause import CustomDict, SysDict, DictWord
from clause import Intent, IntentSlot, IntentUtter
from clause import Entity, ChatMessage, ChatSession

## Other contants
chatbot_id = "avtr003"
intent_name = "takeOut"
customDictName= "food"


def postCustomdict():
    '''
    创建自定义词典
    '''
    pass


import unittest


# run testcase: python /Users/hain/chatopera/py-clause/clause/tst-demo.py Test.testExample
class Test(unittest.TestCase):
    '''
    Test Clause Client
    '''

    def setUp(self):
        self.bot = Client(FLAGS.CL_HOST, FLAGS.CL_PORT)

    def tearDown(self):
        self.bot.destroy()

    def test_post_customdict(self):
        logging.info("创建自定义词典")
        data = Data()
        data.customdict = CustomDict(name=customDictName, chatbotID=chatbot_id)
        response = self.bot.postCustomDict(data)
        logging.debug("response: %s", response)

    def test_demo(self):
        logging.info("示例程序")
        '''
        自定义词典
        '''
        # 创建自定义词典
        data = Data()
        data.customdict = CustomDict(name=customDictName, chatbotID=chatbot_id)
        resp = self.bot.postCustomDict(data)
        logging.info("postCustomDict response: %s", resp)

        # 更新自定义词典
        data = Data()
        data.chatbotID = chatbot_id
        data.customdict = CustomDict(name=customDictName, chatbotID=chatbot_id)
        data.dictword = DictWord(word="西红柿", synonyms="狼桃;柿子;番茄")
        resp = self.bot.putDictWord(data)
        logging.info("putDictWord response: %s", resp)

        # 引用系统词典
        data = Data()
        data.chatbotID = chatbot_id
        data.sysdict = SysDict(name="@TIME")
        resp = self.bot.refSysDict(data)
        logging.info("refSysDict response: %s", resp)

        '''
        意图管理
        '''
        # 创建意图
        data = Data()
        data.intent = Intent(chatbotID=chatbot_id, name=intent_name)
        resp = self.bot.postIntent(data)
        logging.info("postIntent response: %s", resp)

        # 创建意图槽位: 配菜
        data = Data()
        data.intent = Intent(chatbotID=chatbot_id, name=intent_name)
        data.slot = IntentSlot(name="vegetable", requires=True, question="您需要什么配菜")
        data.customdict = CustomDict(chatbotID=chatbot_id, name=customDictName)
        resp = self.bot.postSlot(data)
        logging.info("postSlot response: %s", resp)

        # 创建意图槽位: 送达时间
        data = Data()
        data.intent = Intent(chatbotID=chatbot_id, name=intent_name)
        data.slot = IntentSlot(name="date", requires=True, question="您希望什么时候用餐")
        data.sysdict = SysDict(name="@TIME")
        resp = self.bot.postSlot(data)
        logging.info("postSlot response: %s", resp)

        # 创建意图槽位: 送达位置
        data = Data()
        data.intent = Intent(chatbotID=chatbot_id, name=intent_name)
        data.slot = IntentSlot(name="location", requires=True, question="外卖送到哪里")
        resp = self.bot.postSlot(data)
        logging.info("postSlot response: %s", resp)

        # 添加意图说法
        data = Data()
        data.intent = Intent(chatbotID=chatbot_id, name=intent_name)
        data.utter = IntentUtter(utterance="帮我来一份{vegetable}，送到{location}")
        resp = self.bot.postUtter(data)
        data.utter = IntentUtter(utterance="我想点外卖")
        resp = self.bot.postUtter(data)
        # logging.info("postUtter response: %s", resp)

        '''
        训练机器人        
        '''
        data = Data()
        data.chatbotID = chatbot_id
        resp = self.bot.train(data)
        logging.info("train response: %s", resp)

        ## 训练是一个常时间任务，进行异步反馈
        while True:
            sleep(3)
            data = Data()
            data.chatbotID = chatbot_id
            resp = self.bot.status(data)
            if resp.rc == 0:
                break

        '''
        对话
        '''
        # 创建session
        ## 关于session的说明，参考 https://dwz.cn/wRFrELrq
        data = Data()
        data.session = ChatSession(chatbotID=chatbot_id,
                                   uid="py", # 用户唯一的标识
                                   channel="testclient", # 自定义，代表该用户渠道由字母组成
                                   branch="dev" # 测试分支，有连个选项：dev, 测试分支；pro，生产分支
                                   )
        sessionId = self.bot.putSession(data).session.id
        logging.info("putSession response: %s", resp)

        # 对话
        data = Data()
        data.session = ChatSession(id=sessionId)
        text = "我想点外卖，来一份番茄"
        logging.info("chat human: %s", text)
        data.message = ChatMessage(textMessage=text)
        resp = self.bot.chat(data)
        logging.info("chat bot: %s \n 意图: %s", resp.message.textMessage, resp.session)

        text = "我想在下午三点用餐"
        logging.info("chat human: %s", text)
        data.message = ChatMessage(textMessage=text)
        resp = self.bot.chat(data)
        logging.info("chat bot: %s \n 意图: %s", resp.message.textMessage, resp.session)

def test():
    suite = unittest.TestSuite()
    # suite.addTest(Test("test_post_customdict"))
    suite.addTest(Test("test_demo"))
    runner = unittest.TextTestRunner()
    runner.run(suite)


def main(argv):
    test()


if __name__ == '__main__':
    # /Users/hain/chatopera/py-clause/clause/tst-demo.py --verbosity 1 # DEBUG 1; INFO 0; WARNING -1
    app.run(main)

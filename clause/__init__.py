# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2019 <https://www.chatopera.com> All Rights Reserved
#
#
# File: /Users/hain/chatopera/py-clause/clause/__init__.py
# Author: Hai Liang Wang
# Date: 2019-09-11:22:09:30
#
#===============================================================================
__all__ = [ "Client", "Data", "CustomDict", "SysDict", "Intent",
            "IntentSlot", "IntentUtter", "ProdVersion", "DevelopVersion",
            "BotSysdict", "ChatMessage", "ChatSession", "Entity", 
            "DictWord", "DictPattern", "DictPatternCheck",
            "__version__", "__copyright__", "__author__", "__date__"]

from .gen.clause import ttypes, constants, Serving
__copyright__ = "Copyright (c) 2019 Chatopera Inc. All Rights Reserved"
__author__ = "Hai Liang Wang<hain@chatopera.com>"
__date__ = "2019-12-12"
__version__ = "1.1.0"

## Apache Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

## Struct Wrapper for all objects
Data = ttypes.Data
CustomDict = ttypes.Dict
SysDict = ttypes.Dict
Intent = ttypes.Intent
Entity = ttypes.Entity
IntentSlot = ttypes.IntentSlot
IntentUtter = ttypes.IntentUtter
ProdVersion = ttypes.ProdVersion
DevelopVersion = ttypes.DevelopVersion
BotSysdict = ttypes.BotSysdict
ChatMessage = ttypes.ChatMessage
ChatSession = ttypes.ChatSession
DictWord = ttypes.DictWord
DictPattern = ttypes.DictPattern
DictPatternCheck = ttypes.DictPatternCheck

## logging
from absl import logging #absl-py


class ClRequest(object):

    def __init__(self):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        pass

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args):
            return getattr(args[0].client, f.__name__)(args[1])
        return wrapped_f

class Client():
    '''
    Clause Client
    '''
    def __init__(self, host = "localhost", port = 8056):
        logging.debug("connect to %s %s ..." % (host, port))
        # Make socket
        self.transport = TSocket.TSocket(host, port)

        # Buffering is critical. Raw sockets are very slow
        self.transport = TTransport.TFramedTransport(self.transport)

        # Wrap in a protocol
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)

        # Create a client to use the protocol encoder
        self.client = Serving.Client(protocol)

        # Connect!
        self.transport.open()
        logging.debug("transport opened.")

    def destroy(self):
        '''
        关闭连接
        '''
        self.transport.close()

    @ClRequest()
    def postCustomDict(self, request):
        '''
        创建自定义词典
        :param request:
        :return:
        '''

    @ClRequest()
    def putCustomDict(self, request):
        '''
        更新自定义词典
        :param request:
        :return:
        '''

    @ClRequest()
    def getCustomDicts(self, request):
        '''
        获得自定义词典列表
        :param request:
        :return:
        '''

    @ClRequest()
    def getCustomDict(self, request):
        '''
        获得自定义词典详情
        :param request:
        :return:
        '''

    @ClRequest()
    def delCustomDict(self, request):
        '''
        删除自定义词典
        :param request:
        :return:
        '''

    # @ClRequest()
    # def postSysDict(self, request):
    #     '''
    #     创建系统词典
    #     :param request:
    #     :return:
    #     '''

    # @ClRequest()
    # def putSysDict(self, request):
    #     '''
    #     更新系统词典
    #     :param request:
    #     :return:
    #     '''

    @ClRequest()
    def getSysDicts(self, request):
        '''
        获得系统词典列表
        :param request:
        :return:
        '''

    @ClRequest()
    def getSysDict(self, request):
        '''
        获得系统词典详情
        :param request:
        :return:
        '''

    @ClRequest()
    def refSysDict(self, request):
        '''
        关联系统词典
        :param request:
        :return:
        '''

    @ClRequest()
    def unrefSysDict(self, request):
        '''
        取消关联系统词典
        :param request:
        :return:
        '''

    @ClRequest()
    def myDicts(self, request):
        '''
        通过chatbotID获取所有自定义词典和被引用的词典
        :param request:
        :return:
        '''

    @ClRequest()
    def mySysdicts(self, request):
        '''
        通过chatbotID获取所有被引用的词典
        :param request:
        :return:
        '''

    @ClRequest()
    def putDictWord(self, request):
        '''
        创建或更新词条
        :param request:
        :return:
        '''

    @ClRequest()
    def getDictWords(self, request):
        '''
        获得词条列表
        :param request:
        :return:
        '''

    @ClRequest()
    def delDictWord(self, request):
        '''
        删除词条
        :param request:
        :return:
        '''

    @ClRequest()
    def hasDictWord(self, request):
        '''
        检测一个词条的标准词是否唯一
        :param request:
        :return:
        '''

    @ClRequest()
    def postIntent(self, request):
        '''
        创建意图
        :param request:
        :return:
        '''

    @ClRequest()
    def putIntent(self, request):
        '''
        更新意图
        :param request:
        :return:
        '''

    @ClRequest()
    def getIntents(self, request):
        '''
        获得意图列表
        :param request:
        :return:
        '''

    @ClRequest()
    def getIntent(self, request):
        '''
        获得意图详情
        :param request:
        :return:
        '''

    @ClRequest()
    def delIntent(self, request):
        '''
        删除意图
        :param request:
        :return:
        '''

    @ClRequest()
    def postUtter(self, request):
        '''
        创建说法
        :param request:
        :return:
        '''

    @ClRequest()
    def putUtter(self, request):
        '''
        更新说法
        :param request:
        :return:
        '''

    @ClRequest()
    def getUtters(self, request):
        '''
        获得说法列表
        :param request:
        :return:
        '''

    @ClRequest()
    def getUtter(self, request):
        '''
        获得说法详情
        :param request:
        :return:
        '''

    @ClRequest()
    def delUtter(self, request):
        '''
        删除说法
        :param request:
        :return:
        '''

    @ClRequest()
    def postSlot(self, request):
        '''
        创建槽位
        :param request:
        :return:
        '''

    @ClRequest()
    def putSlot(self, request):
        '''
        更新槽位
        :param request:
        :return:
        '''

    @ClRequest()
    def getSlots(self, request):
        '''
        获得槽位列表
        :param request:
        :return:
        '''

    @ClRequest()
    def getSlot(self, request):
        '''
        获得槽位详情
        :param request:
        :return:
        '''

    @ClRequest()
    def delSlot(self, request):
        '''
        删除槽位
        :param request:
        :return:
        '''

    @ClRequest()
    def train(self, request):
        '''
        训练语言模型
        :param request:
        :return:
        '''

    @ClRequest()
    def status(self, request):
        '''
        查看语言模型训练状态
        :param request:
        :return:
        '''

    @ClRequest()
    def devver(self, request):
        '''
        查看调试版本信息
        :param request:
        :return:
        '''

    @ClRequest()
    def prover(self, request):
        '''
        查看生产版本信息
        :param request:
        :return:
        '''

    @ClRequest()
    def version(self, request):
        '''
        查看调试及生产版本信息
        :param request:
        :return:
        '''

    @ClRequest()
    def chat(self, request):
        '''
        聊天
        :param request:
        :return:
        '''

    @ClRequest()
    def online(self, request):
        '''
        上线版本
        :param request:
        :return:
        '''

    @ClRequest()
    def offline(self, request):
        '''
        下线版本
        :param request:
        :return:
        '''

    @ClRequest()
    def putSession(self, request):
        '''
        创建或更新会话
        :param request:
        :return:
        '''

    @ClRequest()
    def getSession(self, request):
        '''
        获得会话信息
        :param request:
        :return:
        '''

    @ClRequest()
    def putDictPattern(self, request):
        '''
        更新正则表达式词典
        :param request:
        :return:
        '''

    @ClRequest()
    def getDictPattern(self, request):
        '''
        获得正则表达式词典定义
        :param request:
        :return:
        '''

    @ClRequest()
    def checkDictPattern(self, request):
        '''
        调试正则表达式
        :param request:
        :return:
        '''

    @ClRequest()
    def checkHistoryDictPattern(self, request):
        '''
        调整正则表达式历史记录
        :param request:
        :return:
        '''
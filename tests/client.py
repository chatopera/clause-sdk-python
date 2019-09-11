#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2018 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/py-clause/clause/client.py
# Author: Hai Liang Wang
# Date: 2019-09-11:22:09:30
#
#===============================================================================

"""
Clause Client   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2018 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2019-09-11:22:09:30"


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

from absl import flags   #absl-py
from absl import logging #absl-py
from absl import app #absl-py

FLAGS = flags.FLAGS
flags.DEFINE_string('CL_HOST', "127.0.0.1", 'Clause Server\'s IP')
flags.DEFINE_integer('CL_PORT', 8056, 'Clause Server\'s Port')
# flags.DEFINE_boolean('', None, '')
# flags.DEFINE_float('', None, '')

## Apache Thrift
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from clause import ttypes, constants, Serving

## Other contants
chatbot_id = "avtr003"
intent_name = "takeOut"

def postCustomdict():
    '''
    创建自定义词典
    '''
    pass



import unittest

# run testcase: python /Users/hain/chatopera/py-clause/clause/client.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        # Make socket
        self.transport = TSocket.TSocket(FLAGS.CL_HOST, FLAGS.CL_PORT)

        # Buffering is critical. Raw sockets are very slow
        self.transport = TTransport.TFramedTransport(self.transport)

        # Wrap in a protocol
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)

        # Create a client to use the protocol encoder
        self.client = Serving.Client(protocol)

        # Connect!
        self.transport.open()

    def tearDown(self):
        # Close!
        self.transport.close()

    def test_customdict(self):
        logging.info("test_customdict")

def test():
    suite = unittest.TestSuite()
    suite.addTest(Test("test_customdict"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main(argv):
    test()

if __name__ == '__main__':
    # /Users/hain/chatopera/py-clause/clause/client.py --verbosity 1 # DEBUG 1; INFO 0; WARNING -1
    app.run(main)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"

import random
import unittest

import slex.corpus.element

class TestToken(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        e0 = slex.corpus.element.Element()
        self.assertEqual( e0.get_meta(), {} )

    def test_add(self):
        init_meta = { u"name" : u"Bob" }
        e1 = slex.corpus.element.Element(init_meta)
        self.assertEqual( e1.get_meta(), init_meta )

    def test_del(self):
        init_meta = { u"name" : u"Bob" }
        e1 = slex.corpus.element.Element(init_meta)
        e1.del_meta( u"name" )
        self.assertEqual( e1.get_meta(), {} )

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

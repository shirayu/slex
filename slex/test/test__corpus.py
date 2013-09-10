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

import slex.corpus.corpus
import slex.corpus.document

class Test(unittest.TestCase):
    def setUp(self):
        self.metadata = {u"ID": u"TEST-001"}
        self.corpus = slex.corpus.corpus.Corpus(self.metadata)
        self.assertEqual(len(self.corpus), 0)

    def test_meta(self):
        self.assertEqual( self.corpus.get_meta(), self.metadata )

    def __append(self):
        self.docs = []
        for i in range(0,3):
            d = slex.corpus.document.Document({u"ID":i})
            self.corpus.append(d)
            self.docs.append(d)
       
    def test_append(self):
        self.__append()
        self.assertEqual([d for d in self.corpus], self.docs)
        self.assertEqual(len(self.corpus), len(self.docs))
     
    def test_shuffle(self):
        self.__append()
        c1 =  slex.corpus.corpus.Corpus(self.metadata)
        for d in self.corpus:
            c1.append(d)

        self.corpus.shuffle(12345)
        l0 =  [d for d in self.corpus]
        c1.shuffle(12345)
        l1 =  [d for d in c1]
        self.assertEqual(l0, l1)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

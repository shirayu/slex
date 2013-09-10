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

import slex.corpus.document

class Test(unittest.TestCase):
    def setUp(self):
        self.metadata = {u"ID": u"TEST-001"}
        self.doc = slex.corpus.document.Document(self.metadata)
        parags = [  [ u"This are a test.", u"There are many items."], \
                    [u"Good luck!", u"Never gives up!"],   \
                    [u"1234 567 89"],   \
                    [u"111 222"],   \
                    [u"111 111 777 222ing"],   \
                    [u"111  333"],   \
                    [u"444  z aaa 555"],   \
                ]
        self.corr_lines = [  u"This is a test.", \
                u"There are many items.", \
                u"Good luck!", \
                u"Never give up!", \
                u"1-7 89", \
                u"1234 a 222",\
                u"333 333 88 222es end", \
                u"111 x 333",   \
                u"444 666666 yyyyy  555",   \
                ]
        self.corr_keep_lines = [  u"This is a test.", \
                u"There are many items.", \
                u"Good luck!", \
                u"Never give up!", \
                u"1-7 89", \
                u"111 a 222",  \
                u"111 111 88 222ing", \
                u"111 x 333",   \
                u"444 666666 z  555",   \
                ]
        self.lines = []
        for p in parags:
            for i, l in enumerate(p):
                p[i] = slex.corpus.sentence.ParsedSentence(l)
                position = 0
                for nodeid, surf in enumerate(l.split(" ")):
                    token = slex.corpus.token.Token(nodeid, surf, position)
                    position += len(surf)+1
                    p[i].append(token)
                self.lines.append(p[i])

            self.doc.append_paragraph(p)
        self.offset0 = ( (0,5), (0,8) )
        self.offset1 = ( (3,6 ), (3,11) )
        self.offset1_old = ( (1,17 ), (1,22) )


    def test_meta(self):
        self.assertEqual( self.doc.get_meta(), self.metadata )

    def test_append_paragraph(self):
        #__iter__
        self.assertEqual( [l for l in self.doc], self.lines )

    def test_append_paragraph(self):
        #__iter__
        for i, line in enumerate(self.lines):
            self.assertEqual( self.doc.get_sentence(i), line )



    def tearDown(self):
        pass


    def setParser(self):
        import slex.test.dummy
        self.parser = slex.test.dummy.DummyParser()



if __name__ == '__main__':
    unittest.main()

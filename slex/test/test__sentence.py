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

import slex.corpus.sentence

class TestMark(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mark(self):
        raw_sentence = u"I love you."
        raw_marked_sentence = u"I >love< you."
        range_ = (2,6) #not (2,5) but (2,6)

        self.assertEqual( slex.corpus.sentence.mark(raw_sentence, range_), raw_marked_sentence)


class Test(unittest.TestCase):
    def setUp(self):
        raw_sentence = u"I love you."
        self.sen = slex.corpus.sentence.ParsedSentence(raw_sentence)
        self.assertEqual( [token for token in self.sen], [] )

        self.tokens = []
        self.tokens.append( slex.corpus.token.Token(3, u"I", 0) )
        self.tokens.append( slex.corpus.token.Token(5, u"love", 2) )
        self.tokens.append( slex.corpus.token.Token(7, u"you", 7) )
        self.tokens.append( slex.corpus.token.Token(8, u".", 12 ))
        for t in self.tokens:
            self.sen.append(t)

        self.assertEqual( [token for token in self.sen], self.tokens )
        self.assertEqual( len(self.sen), len(raw_sentence) )
        self.assertEqual( self.sen.getSurface(), raw_sentence )

    def __add_nodes(self):
        self.nodes = [ \
            slex.corpus.token.Node(0, u"ROOT", -1 ) ,\
            slex.corpus.token.Node(1, u"S", 0) ,\
            slex.corpus.token.Node(2, u"NP", 1)    ,\
            slex.corpus.token.Node(3, u"PRP", 2)   , \
            slex.corpus.token.Node(4, u"VP", 1)    ,\
            slex.corpus.token.Node(5, u"VBP", 4)   ,\
            slex.corpus.token.Node(6, u"NP", 4 )   ,\
            slex.corpus.token.Node(7, u"PRP", 6)   ,\
            slex.corpus.token.Node(8, u".", 1 )    ,]
        for i, node in enumerate(self.nodes):
            self.sen.appendNode(i, node)

    def test_node(self):
        self.__add_nodes()
        mynodes = []
        goldnodes =[ self.nodes[4-1], self.nodes[6-1], self.nodes[8-1], self.nodes[9-1],]
        for token in self.tokens:
            node = self.sen.getNode(token)
            mynodes.append(node)
        self.assertEqual( mynodes, goldnodes )

    def test_getNode(self):
        self.__add_nodes()
        for i in range(0, 4):
            self.assertEqual( self.sen.getNode(i), self.nodes[i] )
        self.assertEqual( self.sen.getNode(self.tokens[0]), self.nodes[4-1])
        self.assertEqual( self.sen.getNode(self.tokens[1]), self.nodes[6-1])
        self.assertEqual( self.sen.getNode(self.tokens[2]), self.nodes[8-1])
        self.assertEqual( self.sen.getNode(self.tokens[3]), self.nodes[9-1])


    def test_getToken(self):
        self.__add_nodes()
        for i in range(0, 4):
            self.assertEqual( self.sen.getToken(i), self.tokens[i] )
        self.assertEqual( self.sen.getToken(self.nodes[4-1]), self.tokens[0])
        self.assertEqual( self.sen.getToken(self.nodes[6-1]), self.tokens[1])
        self.assertEqual( self.sen.getToken(self.nodes[8-1]), self.tokens[2])
        self.assertEqual( self.sen.getToken(self.nodes[9-1]), self.tokens[3])

        gold_ids = [0, 0, \
                1, 1, 1, 1, \
                1, \
                2, 2, 2, \
                2, \
                3, 3, 3, 3\
                ]
#        gold_ids = [0, None, \
#                1, 1, 1, 1, \
#                None, \
#                2, 2, 2, \
#                None, None, \
#                3, \
#                None, None]
        gold_right_ids = [1, 1, \
                2, 2, 2, 2, \
                2, \
                3, 3, 3, \
                3, \
                None, None,\
                None, None]

        for i in xrange(0, 15):
#            print i, self.sen.getSurface()[:i+1]
            self.assertEqual( self.sen.getTokenIdByPosition(i), gold_ids[i])

        for i in xrange(0, 15):
            id = gold_ids[i]
            if id is None:
                self.assertEqual( self.sen.getTokenByPosition(i), None)
            else:
                self.assertEqual( self.sen.getTokenByPosition(i), self.tokens[id])

        for i in xrange(0, 15):
            self.assertEqual( self.sen.getTokenIdByPosition(i, True), gold_right_ids[i])



    def test_dependency(self):
        self.__add_nodes()
        self.sen.appendDependency(1, 0)
        self.sen.appendDependency(0, 2)
        rels = [2, 0, -1, -1]
        self.assertEqual( [token.getDependency() for token in self.sen], rels )
        dep_rels = [ [1], [], [0], [] ]
        self.assertEqual( [token.getDependedTokenIds() for token in self.sen], dep_rels)


    def test_relation(self):
        self.__add_nodes()
        self.sen.appendRelation(1, 0, u'nsubj' )
        self.sen.appendRelation(1, 2, u'dsubj' )
        rels = [ {}, {0: u'nsubj', 2: u'dsubj'}, {}, {}  ]
        self.assertEqual( [token.getRelations() for token in self.sen], rels )
        dep_rels = [ [1], [], [1], [] ]
        self.assertEqual( [token.getTypedDependedTokenIds() for token in self.sen], dep_rels)


    def test_getParentNode(self):
        self.test_node() #!
        n0 = self.sen.getNode(self.tokens[0])
        self.assertEqual( self.sen.getParentNode(n0), self.nodes[3-1] )
        self.assertEqual( self.sen.getParentNode(self.tokens[0]), self.nodes[3-1] )
        self.assertEqual( self.sen.getParentNode(n0, 1), self.nodes[3-1] )
        self.assertEqual( self.sen.getParentNode(n0, 2), self.nodes[2-1] )
        self.assertEqual( self.sen.getParentNode(n0, 3), self.nodes[1-1] )
        self.assertEqual( self.sen.getParentNode(n0, 4, None ) )

    def test_getParentNode(self):
        self.test_node() #!
        n0 = self.sen.getNode(self.tokens[0])
        self.assertEqual( self.sen.getChildNodes(n0), [])
        n1 = self.sen.getParentNode(n0, 1)
        self.assertEqual( self.sen.getChildNodes(n1), [3])
        n2 = self.sen.getParentNode(n0, 2)
        self.assertEqual( self.sen.getChildNodes(n2), [2, 4, 8])
        n3 = self.sen.getParentNode(n0, 3)
        self.assertEqual( self.sen.getChildNodes(n3), [1])

    def test_getIndex(self):
        self.assertEqual( self.sen.getIndex(self.tokens[0]), 0)
        self.assertEqual( self.sen.getIndex(self.tokens[1]), 1)
        self.assertEqual( self.sen.getIndex(self.tokens[2]), 2)
        self.assertEqual( self.sen.getIndex(self.tokens[3]), 3)

    def test_getNext(self):
        self.assertEqual( self.sen.getNext(self.tokens[0], -1), None)
        self.assertEqual( self.sen.getNext(self.tokens[1], -1), self.tokens[0])
        self.assertEqual( self.sen.getNext(self.tokens[2], -1), self.tokens[1])
        self.assertEqual( self.sen.getNext(self.tokens[3], -1), self.tokens[2])

        self.assertEqual( self.sen.getNext(self.tokens[0], -2), None)
        self.assertEqual( self.sen.getNext(self.tokens[1], -2), None)
        self.assertEqual( self.sen.getNext(self.tokens[2], -2), self.tokens[0])
        self.assertEqual( self.sen.getNext(self.tokens[3], -2), self.tokens[1])
  
        self.assertEqual( self.sen.getNext(self.tokens[0], 0), self.tokens[0])
        self.assertEqual( self.sen.getNext(self.tokens[1], 0), self.tokens[1])
        self.assertEqual( self.sen.getNext(self.tokens[2], 0), self.tokens[2])
        self.assertEqual( self.sen.getNext(self.tokens[3], 0), self.tokens[3])

        self.assertEqual( self.sen.getNext(self.tokens[0]), self.tokens[1])
        self.assertEqual( self.sen.getNext(self.tokens[1]), self.tokens[2])
        self.assertEqual( self.sen.getNext(self.tokens[2]), self.tokens[3])
        self.assertEqual( self.sen.getNext(self.tokens[3]), None)
        
        self.assertEqual( self.sen.getNext(self.tokens[0], 1), self.tokens[1])
        self.assertEqual( self.sen.getNext(self.tokens[1], 1), self.tokens[2])
        self.assertEqual( self.sen.getNext(self.tokens[2], 1), self.tokens[3])
        self.assertEqual( self.sen.getNext(self.tokens[3], 1), None)
 
        self.assertEqual( self.sen.getNext(self.tokens[0], 2), self.tokens[2])
        self.assertEqual( self.sen.getNext(self.tokens[1], 2), self.tokens[3])
        self.assertEqual( self.sen.getNext(self.tokens[2], 2), None)
        self.assertEqual( self.sen.getNext(self.tokens[3], 2), None)
 

    def tearDown(self):
#        print unicode(self.sen)
        pass



if __name__ == '__main__':
    unittest.main()




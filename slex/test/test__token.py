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

import slex.corpus.token

class TestToken(unittest.TestCase):
    def setUp(self):
        surf = u"Moon"
        lsurf = u"moon"
        nodeid = 14
        position = 8
        self.t0 = slex.corpus.token.Token(nodeid, surf, position)
        self.assertEqual( self.t0.getSurface(), surf )
        self.assertEqual( self.t0.getLowerSurface(), lsurf )
        self.assertEqual( self.t0.getNodeid(), nodeid )
        self.assertEqual( self.t0.getPosition(), position )
        self.assertEqual( self.t0.getRelations(), {} )

    def tearDown(self):
        pass

    def test_appendRelation(self):
        nodeid = 32
        relation = u"subj"
        rel = { nodeid : relation }

        self.t0.appendRelation(nodeid, relation)
        self.t0.appendTypedDependedTokenId(17)
        self.assertEqual( self.t0.getRelations(), rel )
        self.assertEqual( self.t0.getTypedDependedTokenIds(), [17] )

        self.t0.setDependency(16)
        self.assertEqual( self.t0.getDependency(), 16 )
        self.t0.appendDependedTokenId(179)
        self.assertEqual( self.t0.getDependedTokenIds(), [179] )



class TestNode(unittest.TestCase):
    def setUp(self):
        pass

    def test_node(self):
        tag = u"some"
        parent_node_id = 13
        self.n0 = slex.corpus.token.Node(9, tag, parent_node_id)
        self.assertEqual( self.n0.getTag(), tag )
        self.assertEqual( self.n0.getParentNodeid(), parent_node_id )
        self.assertEqual( self.n0.getNodeid(), 9 )

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()

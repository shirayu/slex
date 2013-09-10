#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""


__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"

import slex.corpus.sentence
import slex.corpus.element

super = slex.corpus.element.Element
class Document(super):
    def __init__(self, metadata=None):
        super.__init__(self, metadata)
        self.__lines = [] #ParsedSentence
        self.__paragraphs = []

    def append_paragraph(self, txts):
        assert type(txts) in [list, tuple]
        assert type(txts[0]) is slex.corpus.sentence.ParsedSentence

        self.__paragraphs.append( len( self.__lines ) )#store the line number where this paragraphs
        for txt in txts:
            self.__lines.append( txt )
    
    def get_sentence(self, lineid ):
        return self.__lines[lineid]

    def get_string(self, offset):
        assert isinstance(offset, (list,tuple))
        assert len(offset) == 2
        assert len(offset[0]) == 2
        assert len(offset[1]) == 2
        ((start_line_num, start_offset), (end_line_num, end_offset)) = offset
        if start_line_num == end_line_num:
            return self.__lines[ start_line_num ].getSurface()[start_offset:end_offset]
        elif start_line_num > end_line_num:
            raise KeyError
        else:
            ret = self.__lines[ start_line_num ].getSurface()[start_offset:]
            for i in range(start_line_num+1, end_line_num):
                ret += u"\n" + self.__lines[ i ].getSurface()
            ret += u"\n" + self.__lines[ end_line_num ].getSurface()[:end_offset]
            return ret

    def mark(self, offset):
        ((start_line_num, start_offset), (end_line_num, end_offset)) = offset
        if start_line_num != end_line_num:
            return u"*** Cross lines ***"
        else:
            return u"%s" % slex.corpus.sentence.mark( self.__lines[start_line_num].getSurface(), (start_offset, end_offset) )


    def __unicode__(self):
        dump = u""
        dump += unicode(super.__unicode__(self))
        dump += u"\n"
        dump += u"Paragraphs Head Line number:\t"
        dump += u"%s\n" % str(self.__paragraphs)

        dump += u"[Lines]\n"
        for p in self.__lines:
            dump += unicode(p)

        return dump

    def __iter__(self):
        return iter(self.__lines)

    def __len__(self):
        return len(self.__lines)



if __name__=='__main__':
    pass


#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from smallsmilhandler import SmallSMILHandler
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import json


class KaraokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fichero))
        self.lista = sHandler.get_tags()

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python karaoke.py file.smil.')

    karaoke = KaraokeLocal(fichero)
    print(karaoke)
    karaoke.do_local()
    print(karaoke)
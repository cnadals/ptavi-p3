#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        pass

    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.backgroundcolor = attrs.get('backgroundcolor',"")
        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
        elif name == 'img':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
        elif name == 'audio':
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
        elif name == 'textstream':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.right = ""
        self.left = ""
        self.img_src = ""
        self.img_region = ""
        self.img_begin = ""
        self.img_dur = ""
        self.aud_src = ""
        self.aud_begin = ""
        self.aud_dur = ""
        self.text_src = ""
        self.text_region = ""
        self.lista = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.backgroundcolor = attrs.get('backgroundcolor', "")
            at = {'width': self.width,
            	  'height': self.height,
            	  'backgroundcolor': self.backgroundcolor}
            at['tag'] = name
            self.lista.append(at)
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            at = {'id': self.id,
            	  'top': self.top,
            	  'bottom': self.bottom,
            	  'right': self.right,
            	  'left': self.left}
            at['tag'] = name
            self.lista.append(at)
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            at = {'src': self.img_src,
            	  'region': self.img_region,
            	  'begin': self.img_begin,
            	  'dur': self.img_dur}
            at['tag'] = name
            self.lista.append(at)
        elif name == 'audio':
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            at = {'src': self.aud_src,
            	  'begin': self.aud_begin,
            	  'dur': self.aud_dur}
            at['tag'] = name
            self.lista.append(at)
        elif name == 'textstream':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            at = {'src': self.text_src,
            	  'region': self.text_region}
            at['tag'] = name
            self.lista.append(at)

    def get_tags(self):
        return self.lista


if __name__ == "__main__":

        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open('karaoke.smil'))
        Datos = sHandler.get_tags()
        print(Datos)

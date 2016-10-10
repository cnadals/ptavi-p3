#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

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
            at = {'src': self.src,
                'region': self.region,
                'begin': self.begin,
                'dur': self.dur}
            at['tag'] = name
            self.lista.append(at)
        elif name == 'audio':
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            at = {'src': self.src,
                'begin': self.begin,
                'dur': self.dur}
            at['tag'] = name
            self.lista.append(at)
        elif name == 'textstream':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            at = {'src': self.src,
                'region': self.region}
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

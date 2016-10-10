#!/usr/bin/python3
# -*- coding: utf-8 -*-

from smallsmilhandler import SmallSMILHandler
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from urllib.request import urlretrieve
import json
import sys
import urllib.request


class KaraokeLocal()

    def init(self, fichero):
        parser = make_parser()
        self.sHandler = SmallSMILHandler()
        self.misdatos = []
        parser.setContentHandler(self.sHandler)
        parser.parse(open(fichero))
        misdatos = self.sHandler.get_tags()
        return misdatos

    def str(self, datos):
        datosetiqueta = ""
        for data in datos:
            datosetiqueta += data['tag']
            for info in data:
                numero = data[info]
                datosetiqueta += '\t' + info + '=' + '"' + numero + '"'
            datosetiqueta += '\n'
        return datosetiqueta

    def do_local(self, datos):
        datosetiqueta = ""
        for data in datos:
            datosetiqueta += data['tag']
            for info in data:
                numero = data[info]
                if (numero.startswith('http://')):
                    numNuevo = numero.split('/')[-1]
                    datosetiqueta += '\t' + info + '=' + '"' + numNuevo + '"'
                    urlretrieve(numero, numNuevo)
                else:
                    datosetiqueta += '\t' + info + '=' + '"' + numero + '"'
            datosetiqueta += '\n'
        return datosetiqueta

    def do_json(misdatos):
        archivosmil = sys.argv[1]
        archivojson = open(archivosmil.split('.')[0] + '.json', 'w')
        jsoncontent = json.dumps(misdatos)
        archivojson.write(jsoncontent)

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python karaoke.py file.smil.')

    klocal = KaraokeLocal()
    diccionario = []
    diccionario = klocal.init(fichero)
    print(klocal.str(diccionario))
    print(klocal.do_local(diccionario))

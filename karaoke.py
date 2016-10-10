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

    #Tengo que sacar cada diccionario de la lista de diccionarios y 
    def imprimirdatos(lista):
        for datos in lista: #separo cada diccionario: datos
            datatributos = datos['tag'] #a partir de aqui, son los datos del "titulo"
            del datos['tag'] #borro la etiqueta para quedarme con la info
            for info in datos:    #dato es cada atributo del diccionario
                numero = datos[info]
                datatributos = datatributos + '\t' + info + '=' + '"' + numero + '"' 
            print(datatributos)

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python karaoke.py file.smil.')

    karaoke = KaraokeLocal(fichero)
    imprimirdatos(lista)

    #imprime primero tag y luego sus atributos

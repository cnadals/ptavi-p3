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
            datosetiqueta = datos['tag'] #a partir de aqui, son los datos de la etiqueta
            del datos['tag'] #borro la etiqueta para quedarme con "el resto"
            for info in datos: #dato es cada atributo del diccionario
                numero = datos[info] #numero es el valor de cada atributo
                datosetiqueta = datosetiqueta + '\t' + info + '=' + '"' + numero + '"' #imprimo los datos de la etiqueta como pide
            print(datosetiqueta)

#Guarda el archivo en formato json
    def to_json(lista):
        archivosmil = sys.argv[1]
        archivojson = open(archivosmil.split('.')[0] + '.json', 'w')
        jsoncontent = json.dumps(lista)
        archivojson.write(jsoncontent)

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python karaoke.py file.smil.')

    karaoke = KaraokeLocal(fichero)
    parser.parse(open(fichero))
    imprimirdatos(lista)
    to_json(lista)


    #imprime primero tag y luego sus atributos

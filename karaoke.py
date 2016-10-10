#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from smallsmilhandler import SmallSMILHandler
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import json

#class karaoke(SmallSMILHandler):

def init(fichero):
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open(fichero))
    return sHandler.get_tags()

#Tengo que sacar cada diccionario de la lista de diccionarios
def imprimirdatos(Lista):
    for datos in Lista: #separo cada diccionario: datos
        datosetiqueta = datos['tag'] #a partir de aqui, son los datos de la etiqueta
        del datos['tag'] #borro la etiqueta para quedarme con "el resto"
        print(datosetiqueta)
        for info in datos: #dato es cada atributo del diccionario
            numero = datos[info] #numero es el valor de cada atributo
            datosetiqueta = datosetiqueta + '\t' + info + '=' + '"' + numero + '"' #imprimo los datos de la etiqueta como pide
        print(datosetiqueta)
        datosetiqueta = ' '

#Guarda el archivo en formato json
def to_json(Lista):
    archivosmil = sys.argv[1] #cojo el archivo
    archivojson = open(archivosmil.split('.')[0] + '.json', 'w') #cambio el formato del archivo
    jsoncontent = json.dumps(Lista) 
    archivojson.write(jsoncontent)

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python karaoke.py file.smil.')

    Lista = init(fichero)
    imprimirdatos(Lista)
    to_json(Lista)
    #GREGORIO DICE: imprime primero tag y luego sus atributos

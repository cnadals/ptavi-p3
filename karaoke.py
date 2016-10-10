#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from smallsmilhandler import SmallSMILHandler
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
#from smallsmilhandler import SmallSMILHandler
import sys
import json
#import urllib.request

parser = make_parser()
sHandler = SmallSMILHandler()
parser.setContentHandler(sHandler)
misdatos = sHandler.get_tags()

#Tengo que sacar cada diccionario de la lista de diccionarios
def imprimirdatos(misdatos):
    datosetiqueta = ""
    for datos in misdatos: #separo cada diccionario: datos
        datosetiqueta += datos['tag'] #a partir de aqui, son los datos de la etiqueta
        del datos['tag'] #borro la etiqueta para quedarme con "el resto"
        for info in datos: #info es cada atributo del diccionario
            numero = datos[info] #numero es el valor de cada atributo
            datosetiqueta += '\t' + info + '=' + '"' + numero + '"' #imprimo los datos de la etiqueta
        datosetiqueta += '\n'
    return datosetiqueta

#Guarda el archivo en formato json
def to_json(misdatos):
    archivosmil = sys.argv[1] #cojo el archivo
    archivojson = open(archivosmil.split('.')[0] + '.json', 'w') #cambio el formato del archivo
    jsoncontent = json.dumps(misdatos)
    archivojson.write(jsoncontent)

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python karaoke.py file.smil.')

    parser.parse(open(fichero))
    print(imprimirdatos(misdatos))
    to_json(misdatos)

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from smallsmilhandler import SmallSMILHandler
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from urllib.request import urlretrieve
import json
import sys
import urllib.request

class KaraokeLocal():

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
        for data in datos: #separo cada diccionario: datos
            datosetiqueta += data['tag'] #a partir de aqui, son los datos de la etiqueta
            for info in data: #info es cada atributo del diccionario
                numero = data[info] #numero es el valor de cada atributo
                datosetiqueta += '\t' + info + '=' + '"' + numero + '"' #imprimo los datos de la etiqueta
            datosetiqueta += '\n'
        return datosetiqueta

    #Tengo que sacar cada diccionario de la lista de diccionarios
    def do_local(self, datos):
        datosetiqueta = ""
        for data in datos: #separo cada diccionario: datos
            datosetiqueta += data['tag'] #a partir de aqui, son los datos de la etiqueta
            for info in data: #info es cada atributo del diccionario
                numero = data[info] #numero es el valor de cada atributo
                if (numero.startswith('http://')): #miro a ver desde donde inicia
                    numeroNuevo = numero.split('/')[-1] #cojo de la ultima / hasta el final
                    datosetiqueta += '\t' + info + '=' + '"' + numeroNuevo + '"' #aqui recorto el valor del atributo src que empieza por http
                    urlretrieve(numero, numeroNuevo) #descargo el fichero: de internet a local
                else:
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

    klocal = KaraokeLocal()
    diccionario = []
    diccionario = klocal.init(fichero)
    print(klocal.str(diccionario))
    print(klocal.do_local(diccionario))
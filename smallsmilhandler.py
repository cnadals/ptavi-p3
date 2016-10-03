#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

	def __init__ (self):
	"""
	Constructor. Inicializamos las variables
	"""
	pass

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.width = attrs.get('root-layout',"")
            self.height = 
            self.backgroundcolor =
        elif name == 'region':
            self.id = 1
            self.top =
            self.bottom =
            self.left =
            self.right =
        elif name == 'img':
            self.src = 1
            self.region =
            self.begin =
            self.dur =
        elif name == 'audio':
        	self.begin = 1
        	self.dur =
        elif name == 'textstream':
        	self.src =
        	self.region =
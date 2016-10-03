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
            self.height = attrs.get('root-layout',"")
            self.backgroundcolor = attrs.get('root-layout',"")
        elif name == 'region':
            self.id = attrs.get('region',"")
            self.top = attrs.get('region',"")
            self.bottom = attrs.get('region',"")
            self.left = attrs.get('region',"")
            self.right = attrs.get('region',"")
        elif name == 'img':
            self.src = attrs.get('img',"")
            self.region = attrs.get('img',"")
            self.begin = attrs.get('img',"")
            self.dur = attrs.get('img',"")
        elif name == 'audio':
        	self.begin = attrs.get('audio',"")
        	self.dur = attrs.get('audio',"")
        elif name == 'textstream':
        	self.src = attrs.get('textstream',"")
        	self.region = attrs.get('textstream',"")
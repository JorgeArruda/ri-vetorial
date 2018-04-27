#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from PIL import Image  # Importando o módulo Pillow para abrir a imagem no script
import pytesseract     # Módulo para a utilização da tecnologia OCR

def ocrInFolder(path):
    if type(path) != str:
        return "Erro, argument path != string"
    files = os.listdir(path)
    documents = {}
    for file in files:
        documents[file] = pytesseract.image_to_string( Image.open(path+file), lang='por' ) # eng = english and por = portuguese
    return documents

def ocrInFile(name):    
    if type(name) != str:
        return "Erro, argument name != string"
    
    return pytesseract.image_to_string( Image.open(name), lang='por' ) # eng = english and por = portuguese

# Exemplo
# string = ocrInFile('download.jpg')
# print(string)
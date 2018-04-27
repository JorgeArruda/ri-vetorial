#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import lex
from PIL import Image  # Importando o módulo Pillow para abrir a imagem no script
import pytesseract     # Módulo para a utilização da tecnologia OCR

texto = pytesseract.image_to_string( Image.open('download.jpg'), lang='por' ) # eng = english and por = portuguese

print(texto)
print("\nTokens", lex.tokenize(texto))




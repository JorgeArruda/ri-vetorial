#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

# Importando arquivos
import lex as lex
import ocr as ocr
import pdf_read as pdf_read
import docx_read as docx_read
import html_read as html_read
from operator import itemgetter


def sort_dic(dic, indice=0):
    return sorted(dic.items(), key=itemgetter(indice))

def get_text(name, path = '/'):
    if type(path) != str:
        return "Erro, argument path != string"
    archive_type = name.split(".")[-1]
    try:
        if (archive_type == "html"):
            return html_read.file(path+name)
        elif (archive_type == "pdf"):
            return pdf_read.file(path+name)
        elif (archive_type == "docx"):
            return docx_read.file(path+name)
        elif ((archive_type == "jpg") | (archive_type == "png")):
            return ocr.file(path+name)
        else:
            return ' '
    except FileNotFoundError:
       print("No such file or directory: ",path+name)
       return ' '

def get_tokens(text, language='portuguese'):
    if type(text) != str:
        return "Erro, argument text != string"
    return lex.tokenize(text, language)

def remove_stopwords( tokens ):
    "Remove stopwords e verifica a quantidade removida. Return {'tokens', 'qt_stopwords', 'qt_stopwords_total', 'qt_adverbios', 'qt_adverbios_total'}"
    if ( type(tokens) != dict ):
        print( '\n---Tokens não é uma lista!', tokens)
    if ( len(tokens) == 0 ):
        print( '\n---Lista de tokens vazia!', tokens)

    qt_stopwords = qt_stopwords_total = 0
    qt_adverbios = qt_adverbios_total = 0
    qt_tok_total = qt_tok = 0

    max_tf = 0
    new_tokens = {}

    if ( not(type(tokens) != dict or len(tokens) == 0) ):
        stopwords = stop().stopwords
        adverbios = stop().adverbios
        
        for key in tokens:
            qt_tok_total += tokens[key]
            qt_tok += 1
            if ( key in stopwords ):
                qt_stopwords += 1
                qt_stopwords_total += tokens[key]
                # tokens.pop(key)
            elif ( key in adverbios ):
                qt_adverbios += 1
                qt_adverbios_total += tokens[key]
                # tokens.pop(key)
            else:
                if tokens[key] > max_tf:
                    max_tf = tokens[key]
                new_tokens[key] = tokens[key]
        print( '\n\t%d Stopwords e %d adverbios removidos.' % (qt_stopwords_total, qt_adverbios_total) )
    return {'tokens': new_tokens,\
        'qt_stopwords':qt_stopwords, 'qt_stopwords_total': qt_stopwords_total,\
        'qt_adverbios': qt_adverbios, 'qt_adverbios_total': qt_adverbios_total,\
        'qt_tok': qt_tok, 'qt_tok_total': qt_tok_total, 'max':max_tf }
    

def get_frequency(listTokens):
    "Vare a lista de tokens do documento, retorna a frequência. return frequencyDocument"
    frequencyDocument = {}
    for token in listTokens:
        print(token)
        if token in frequencyDocument:
            frequencyDocument[ token ]+=1
        else:
            frequencyDocument[ token ]=1
    
    return dict(sort_dic(frequencyDocument))

def get_tf( frequency, qtTokens ):
    if ( type(frequency) != dict ):
        print( '\n---Tokens não é uma lista!', frequency)
    if ( len(frequency) == 0 ):
        print( '\n---Lista de tokens vazia!', frequency)
    tf = {}
    if qtTokens != 0:
        for key in frequency:
            tf[key] = frequency[key] / qtTokens
    return tf

def get_tfLog( frequency ):
    if ( type(frequency) != dict ):
        print( '\n---Tokens não é uma lista!', frequency)
    if ( len(frequency) == 0 ):
        print( '\n---Lista de tokens vazia!', frequency)
    tfLog = {}
    for key in frequency:
        tfLog[key] = math.log(1 + frequency[key])
    return tfLog

def get_tfDouble( frequency, qtMax ):
    if ( type(frequency) != dict ):
        print( '\n---Tokens não é uma lista!', frequency)
    if ( len(frequency) == 0 ):
        print( '\n---Lista de tokens vazia!', frequency)
    tfDouble = {}
    if qtMax != 0:
        for key in frequency:
            tfDouble[key] = 0.5 + ( 0.5 * (frequency[key] / qtMax))
    return tfDouble

def get_idf( fDocument, numDocument ):
    if ( type(fDocument) != dict ):
        print( '\n---Tokens não é uma lista!', fDocument)
    if ( len(fDocument) == 0 ):
        print( '\n---Lista de tokens vazia!', fDocument)

    idf_word = {}
    for key in fDocument:
        idf_word[key] = math.log( numDocument / fDocument[key], 2 )

    return idf_word
    
if __name__ =="__main__d":
    get_text("jkak.pdf")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql as mysql
import pymysql.cursors

def connect():
    key = str(input('Password: '))
    return mysql.connect(host = "127.0.0.1", user = "root", passwd = key, db = 'ri_vetorial', port= 3306)

def saveTokens(connection, name, tokens):
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO `ri_vetorial`.`documents` (`titulo`, `texto`) VALUES ( %s, %s)"""
            cursor.execute(sql,(name,tokens))

            connection.commit()
    finally:
        connection.close()

def getTokens(connection, name):
    try:
        with connection.cursor() as cursor:
            sql = """SELECT documents.texto FROM ri_vetorial.documents WHERE documents.nome = %s"""
            cursor.execute(sql,(name))
            return cursor.fetchone()[0]           
    finally:
        connection.close()
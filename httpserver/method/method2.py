# -*- coding: utf-8 -*-
import web
import time
import os
import sys

class method2:  
    def GET(self):
        response = ''
        try:
            imdata = web.data()
            header = web.input()
            id = int(header.id)
            action = header.action
            response = 'ok'
            return response
        except Exception,ex:
            print Exception,":",ex
        return response

    def POST(self):
        response = ''
        try:
            imdata = web.data()
            header = web.input()
            id = int(header.id)
            action = header.action
            response = 'ok'
            return response
        except Exception,ex:
            print Exception,":",ex
        return response

#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
#cgitb.enable()    
cgitb.enable(display=1, logdir="/home/sites/python1/log/cgi.log")
print("Content-Type: text/html;charset=utf-8")
print()
    
print("Hello World!")

import os
for i in os.environ:
	print("<br>",i,os.environ[i])


print("<br><br>",os.environ['REQUEST_METHOD'])

import cgi
arguments = cgi.FieldStorage()
for i in arguments.keys():
 print (i,arguments[i].value)


print("<FORM METHOD=POST ACTION='?'><INPUT TYPE=TEXT name='campo1'><INPUT TYPE=SUBMIT></FORM>")

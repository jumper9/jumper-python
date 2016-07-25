#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
cgitb.enable()    
print("Content-Type: text/html;charset=utf-8")
print()    
print("Hello World!")

import cgi
arguments = cgi.FieldStorage()
for i in arguments.keys():
 print (i,arguments[i].value)


print("<FORM METHOD=POST ACTION='?'><INPUT TYPE=TEXT name='campo1'><INPUT TYPE=SUBMIT></FORM>")

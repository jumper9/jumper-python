#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
cgitb.enable(display=1)


import sys
import os
import os.path
import j

## DB ##
j.dbConnect()

## ARGUMENTS ##
j.setParams()
## ARGUMENTS END ##

## ROUTING ##
_requestMethod = os.environ['REQUEST_METHOD'].lower() 
_url = os.environ['SCRIPT_URL'].split('/')
_met = ""

if(len(_url)>=4):
  _pkg = _url[1]
  _obj = _url[2]
  _met = _url[3]
elif(len(_url)==3):
  _pkg = _url[1]
  _obj = _url[2] 
else:
  _pkg = "default"
  _obj = _url[1]

if(_met==""):
  _met = _requestMethod
#print ("Method:",_met)

if(os.path.isfile("../"+_pkg+"/services/"+_obj+".py")): 
  #try:
    sys.path.append("../"+_pkg+"/services")
    m = __import__ (_obj)
    func = getattr(m, _met)
    func()
    j.output()

  #except AttributeError:
  #  print("OBJECT FOUND:" + _pkg + "/" + _obj)
  #  print("METHOD NOT FOUND:" + _met)

else:
  print("OBJECT NOT FOUND:" + _pkg + "/" + _obj)
## ROUTING END ##


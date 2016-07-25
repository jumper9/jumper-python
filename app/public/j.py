import sys
import cgi
import json
import os

params = {}
 
def getParam(p):
  try:
    return params[p.lower()]
  except:
    return ""

def getParams():
  return params
  
  
def setParams():
  ## Order from most important: GET, POST, PAYLOAD 
  # Payload
  try:
    fields = json.loads(sys.stdin.read()) 
    for i in fields.keys():
      params[i.lower()] = fields[i]
  except:
    pass

  # GET & POST
  fields = cgi.FieldStorage()
  for i in fields.keys():
    params[i.lower()] = fields[i].value
  
 


# get file list
# iterate files   
  # get file content
  # explode def[name]():
  # iterate functions
    # get comments
    # build json
    # add json to list
    
# print json
  
  
  
  
  
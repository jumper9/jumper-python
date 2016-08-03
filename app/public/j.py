import sys
import cgi
import json
import os
sys.path.append("../jumper/lib")
import jumperDb
import config
import server

params = {}
errors = []
response = None

def getConfig(p):
  if(p in config.c):
    return config.c[p]
  else:
    return False


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
def dbConnect():
  jumperDb.connect()

  
def dbRes(sql, queryParams = {}):
  jumperDb.debug(sql)
  return jumperDb.res(sql, queryParams)

def dbFirstRow(sql, queryParams = {}):
  jumperDb.debug(sql)
  return jumperDb.firstRow(sql, queryParams)

def dbFullRes(sql, queryParams = {}):
  jumperDb.debug(sql)
  return jumperDb.fullRes(sql, queryParams)

def query(sql, queryParams = {}):
  jumperDb.debug(sql)
  return jumperDb.query(sql, queryParams)
  
def dbDebug(on = True):
  jumperDb.sqlDebug(on)

def setResponse(data):
  global response
  response = data

def strToken(str, pos, div):
  out = ""
  s = str.split(div)
  if(pos > 0 and len(s) >= pos):
    out = s[pos - 1]
  elif(pos < 0):
    pos = len(s) + pos
    if(pos >= 0): 
      out = s[pos]
  return out

def setError(code, text, id = 0):
  global errors
  errors.append({"code": str(code), "text": text, "id": id})

def output():
  global errors, response
  out = ""
  statusTxt = "200 OK"

  if(len(errors) == 0):
    if(isinstance(response, str) or isinstance(response, int)):
      out = {"value" : response}
    else:
      out = response
  else:
    out = {"errors" : errors }
    if(getConfig("sendErrorHTMLCodes")):
      statusTxt = errors[0]["code"] + " " + errors[0]["text"] 

  print("Content-Type: application/json;charset=utf-8") 
  print("Status: " + statusTxt )
  print()


  print(json.dumps(out))

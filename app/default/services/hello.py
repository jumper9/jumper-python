import j
import os
import re
import json

baseJson = { "swagger" :"2.0" }
baseJson.update({"info" : { "description": "", "version": "16.0.1", "title": "jumper-python"}})
baseJson.update({"host":"", "basePath":"", "schemes":"", "paths":{}, "definitions": {}})
baseJson.update({"responses":{ "200": { "description": "OK" }}})
allPaths = {}


def get():
#{"ss":true,"summary":"Listar items GET",
#"ssss":3444, "b":"dd"}
#
    print ('GET CLASS :)<br><br>')
    print(j.getParam("A"));
    p = j.getParams()
    for i in p:
      print("<br>",i,p[i])

def post():
#    "Prints a."
    print ('POST CLASS!')
    print(j.getParam("BBB"));

    p = j.getParams()
    for i in p:
      print("<br>",i,p[i])



def dirs():
  files = []
  for dirname, dirnames, filenames in os.walk('..'):
    # print path to all filenames.
    for filename in filenames:
        file = os.path.join(dirname, filename)[3:]
        if(file.endswith(".py") and not file.startswith("public/")):
          with open("../"+file, 'r') as myfile:
            fileContents = myfile.read()
            docParams = searchFile(file, "\n"+fileContents)
  
  baseJson.update({"paths":allPaths})
  print(json.dumps(baseJson, sort_keys=True, indent=4))


def ext():
  pass

def internal():
  pass
  s
def searchFile(fileName, fileContents):
  serviceName = fileName[:-3] # remove .py
  fileComments = []
  for methodContent in fileContents.split("\ndef "):
    methodName = re.split("\n",methodContent)[0].strip().lower();
    if(methodName.endswith("():") and not methodName.startswith("_")):
      methodName = methodName[:-3] # remove ():
      comments = getComments(serviceName, methodName, methodContent)
      if("method" in comments and "path" in comments):
        method = comments["method"]
        path = comments["path"]
        if(not path in allPaths):
          allPaths.update({ path : {} })
        allPaths[path].update({method:comments})
        

def getComments(serviceName, methodName, methodContent):
  lines = re.split("\n",methodContent)[1:]
  jsonString = ""
  jsonObject = {}
  isMethodVerb = False
  for l in lines:
    if not l.startswith("#"):
      break
    jsonString += l[1:]
  try:
    jsonObject = json.loads(jsonString)
    if(methodName in ["get", "post", "put", "delete"]):
      jsonObject.update({"method": methodName})
      isMethodVerb = True
    else:  
      jsonObject.update({"method": "get"})

    jsonObject.update({"path": getPath(serviceName, methodName, isMethodVerb) })
    jsonObject.update({"serviceName": serviceName })
    jsonObject.update({"methodName": methodName })

  except:
    pass
  
  return jsonObject


def getPath(serviceName, methodName, isMethodVerb):
  path = ""
  serviceSplit = serviceName.split("/")
  if( serviceSplit[0] == "default" and isMethodVerb):
    path = serviceSplit[2]
  else:
    if(isMethodVerb):
      path = serviceSplit[0]+"/"+serviceSplit[2]
    else:
      path = serviceSplit[0]+"/"+serviceSplit[2]+"/"+methodName
  return "/"+path
  
  
def testService():
#  {  "method":"POST", "summary" : "Subida de uno o varios contenidos multimedia",
#                  "description":"Upload de contenidos multimepdia como archivo adjunto.Recibe multipart/form-data.Devuelve un hash.",
#                  "consumes": [
#                      "multipart/form-data"
#                  ],
#                  "produces": [
#                      "application/json"#
#                  ],
#                  "parameters" : [
#                                   { "name" : "_api_key", "in" : "formData", "description": "Token de auntentificacion para los servicios", "type": "string" },
#                                   { "name" : "mediaArray[]", "in" : "formData", "description": "Contenido multimedia a subir", "type": "file" },
#                                   { "name" : "creation_date", "in" : "formData", "description": "Fecha y hora", "type": "string" },
#                                   { "name" : "extra_fields", "in" : "formData", "description": "String de datos variables con formato de objeto JSON que se adjuntan al CSV", "type": "string" }
#                                 ],
#                          "responses": {
#                              "400": { "description": "Invalid token<br>Invalid media_product" },
#                              "500": { "description": "El contenido multimedia no es aceptado Ext:{extension}(jpeg, jpg, png, gif,mp3,wav,wma,avi,mpeg,mp4,3gp)<br>El tamano del contenido no debe superar los 50MB<br>No se pudo subir el contenido multimedia, intente nuevamente"}
#                          } }
#
  pass 
  
def res():
# { "summary":"Executes a SQL script and returns a single string value" }  
  pass

def test1():  
#  j.setError(400, "Codigo error A")

#  j.setError(401, "Codigo error 1")
#  j.setError(402, "Codigo error 3",3)
  j.setResponse(j.dbFullRes("select date_format(now(), '%Y-%m-%d %H:%i:%s') union select 1 union select 2 union select 3", {"p2":"1"}))


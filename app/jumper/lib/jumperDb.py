import pymysql
import sys
import j
import server

debugOn = False
conn = None
c = None

def printMessage(msg):
    print("<div style='font-family:Courier New;padding:10px;margin:0px;"
        ,"background-color:#cccccc;font-size:13px'>",msg.replace('\n'
        , '<br />'),"</div>")

def debug(sql):
  global debugOn
  if(debugOn):
    printMessage(sql)

def sqlDebug(pDebug = True):
  global debugOn
  debugOn = pDebug


def res(sql, queryParams = {}):

  sql = sqlReplace(sql, queryParams)
  global c
  out = ""
  try:
    c.execute(sql)
    out = c.fetchone()[0]
  except:
    printMessage( "error: " + sql ) # + " :" + sys.exc_info()[0]
  return out


def firstRow(sql, queryParams = {}):
  sql = sqlReplace(sql, queryParams)
  global c
  out = {}
  try:
    c.execute(sql)
    fields = []
    for f in c.description:
      fields.append(f[0]);
    r = c.fetchone()
    for f in range(0,len(fields)):
      out.update({fields[f]: r[f]})
  except:
    printMessage( "error: " + sql ) # + " :" + sys.exc_info()[0]
  return out


def fullRes(sql, queryParams = {}):
  sql = sqlReplace(sql, queryParams)
  global c
  out = []
  try:
    c.execute(sql)
    fields = []
    for f in c.description:
      fields.append(f[0]);
    for r in c.fetchall():
      row = {}
      for f in range(0,len(fields)):
        row.update({fields[f]: r[f]})
      out.append(row)
  except:
    printMessage( "error: " + sql ) # + " :" + sys.exc_info()[0]
  return out


def query(sql):
  sql = sqlReplace(sql, queryParams)
  global c
  out = 0
  try:
    c.execute(sql)
    out = c.rowcount
  except:
    printMessage( sql ) # + " :" + sys.exc_info()[0]
  return out


def connect():
  global conn, c, server
  try: 
    conn = pymysql.connect(
      db=server.db,
      user=server.user,
      passwd=server.password,
      host=server.host,
      autocommit=True)
    c = conn.cursor()
  except:
    printMessage("Connection Error")


def sqlReplace(sql, queryParams):
  out = ""
  pos = sql.find("{")
  pos2 = sql.find("}")
  while(pos >= 0 and pos2 > pos):
    var = sql[pos+1:pos2]
    value = ""

    if(var[0:2] == "d:"):
      if(var[2:] in queryParams):
        value = queryParams[var[2:]]
    else:
      if(var in queryParams):
        value = "'" + pymysql.escape_string(queryParams[var]) + "'"
      else:
        value = "'" + pymysql.escape_string(j.getParam(var)) + "'"

    sql = sql.replace("{"+var+"}", value)

    pos = sql.find("{")
    pos2 = sql.find("}")

  return sql

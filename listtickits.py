#!/usr/bin/python
from xml.dom.minidom import parse, parseString
import libxml2
#from xml import xpath
#from xml import xpath
doc = libxml2.parseFile('/home/kristian/.local/share/gtg/99cd7d36-92e1-47d0-983a-58a9d522ebea.xml')
query = '//task[@status="Active"]/title'
res = doc.xpathEval(query)


#ctxt = doc.xpathNewContext()


#doc.freeDoc()
#ctxt.xpathFreeContext()

#doc = parse('/home/kristian/.local/share/gtg/99cd7d36-92e1-47d0-983a-58a9d522ebea.xml')
#res = xpath.find('//task[@status="Active"]/title', doc)
for title in res:
  print title.content.strip()
#ctxt = dom1.xpathNewContext()

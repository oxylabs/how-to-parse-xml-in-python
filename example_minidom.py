from xml.dom.minidom import parseString
xml_string = """<?xml version="1.0" encoding="UTF-8"?>
<library>
  <book>
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <year>1925</year>
  </book>
</library>
"""
document = parseString(xml_string)
print(document.getElementsByTagName("title")[0].firstChild.nodeValue)
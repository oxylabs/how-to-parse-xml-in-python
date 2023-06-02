import xml.etree.ElementTree as ET
xml_string = """<?xml version="1.0" encoding="UTF-8"?>
<library>
  <book>
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <year>1925</year>
  </book>
</library>
"""
root = ET.fromstring(xml_string)

parsed_dict = dict()

for child in root.iter():
    if child.text.strip():
        parsed_dict[child.tag] = child.text

print(parsed_dict)

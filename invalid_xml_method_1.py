import pandas as pd
from xml.dom.minidom import parseString

invalid_xml = """<?xml version="1.0" encoding="UTF-8"?>
<root>
 <person>
 <name> John Doe</name>
 <message>This is a message & an invalid XML example.</message>
 </person>
</root>
"""

# preprocessing method 1
valid_xml = invalid_xml.replace("&", "&amp;")
parsed_data = parseString(valid_xml)
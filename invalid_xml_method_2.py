from bs4 import BeautifulSoup
invalid_xml = """<?xml version="1.0" encoding="UTF-8"?>
<root>
 <person>
 <name> John Doe</name>
 <message>This is a message & an invalid XML example.</message>
 </person>
</root>
"""
soup = BeautifulSoup(invalid_xml, features="lxml-xml")
print(soup.prettify())
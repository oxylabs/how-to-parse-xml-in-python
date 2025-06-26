How to Parse XML in Python
==========================

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/product-integrations/refs/heads/master/Affiliate-Universal-1090x275.png)](https://oxylabs.io/pages/gitoxy?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=how-to-parse-xml-in-python-github&transaction_id=102f49063ab94276ae8f116d224b67)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

Introduction
------------

In this article, you'll learn how to parse XML data in Python by exploring popular Python libraries. The article will cover the basics of XML, DOM representation, built-in Python libraries for parsing XML Documents, and their differences. You'll also learn the step-by-step procedure of parsing XML files, handling invalid XML, converting to a dictionary, and saving data to a CSV file. Let's get started.

What is XML?
------------

XML (Extensible Markup Language) is a popular markup language used in a wide range of applications and systems. It's a structured and hierarchical data format that allows you to store and exchange data between different platforms and applications. XML files are commonly used for data exchange, configuration files, and web services. Take a look at the below example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<menu>
 <food>
   <item name="lunch" type="main">Chicken Biryani</item>
   <price currency="USD">$12.99</price>
   <description>
     Aromatic basmati rice cooked with tender chicken pieces, spices, and herbs.
   </description>
   <calories>780</calories>
   <ingredients>
     <ingredient>Basmati rice</ingredient>
     <ingredient>Chicken</ingredient>
     <ingredient>Spices</ingredient>
     <ingredient>Herbs</ingredient>
   </ingredients>
 </food>
</menu>
```

This XML file starts with an XML Declaration that lets the parser know the version and encoding of the file. The root element `menu` contains information about a food item. Notice how each of the properties and attributes is structured to convey the information in a hierarchy.

What is DOM?
------------

The Document Object Model (DOM) provides a hierarchical representation of the document, allowing developers to interact with its elements programmatically. It provides a standardized interface to interact with web documents programmatically. It also has versatile and wide browser support enabling the creation of dynamic, interactive, and responsive web applications. It's a platform and language-neutral interface that allows you to dynamically access and update the content, structure, and style of XML and HTML documents.

```html
<!DOCTYPE html>
<html>
<head>
   <title>DOM Example</title>
</head>
<body>
   <h1>Welcome to the DOM Example</h1>
   <p>This is a sample paragraph.</p>
   <ul>
       <li>Item 1</li>
       <li>Item 2</li>
       <li>Item 3</li>
   </ul>
</body>
</html>
```

The DOM serves as a powerful tool for web development. It enables efficient manipulation of the document's structure, allowing for the addition, removal, or modification of elements, attributes, and text. It provides a tree-like structure, where each element in the document is represented as a node. The root node represents the document itself, with child nodes representing elements, attributes, and text nodes. This hierarchical structure makes node traversal easy and manipulation of the document's contents a breeze.

What is XML parsing?
---------------------

XML parsing is a fundamental process of working with XML data. It has several key steps such as checking the syntax of the XML document, tokenizing, and building the document structure in a hierarchy. XML parsing is surprisingly difficult if you've worked with any XML document before, then you might already know this. Luckily, Python provides tons of libraries that can be utilized for parsing XML documents. All these tools have different trade-offs. Some are optimized for speed and some for memory. You can pick the necessary tool you like based on your requirements.

Built-in Python libraries for parsing XML
-----------------------------------------

Almost all the Python distributions provide a standard XML library that bundles abstract interfaces for Parsing XML documents. It also enables you to supply concrete parser implementation. However, in reality, you'll hardly use a parser implementation of your own. Instead, you'll take advantage of the Python bindings of various XML parsing libraries, such as [Expat](https://en.wikipedia.org/wiki/Expat_(library)). Python's standard XML library automatically binds it for you. Let's explore some of the sub-modules of Python's standard XML library.

### The xml.dom.minidom library

This library enables you to parse XML documents in the DOM interface. This is a relatively old implementation of the W3c specification. All the common objects such as Document, Element, Attr, etc. are available. This module is less useful as it lacks proper documentation.

```py
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
```

The above code will parse the `xml_string` and store it in the `document` object. Now, you can use the DOM interface to access the various nodes of this XML document. Let's print the title

```py
print(document.getElementsByTagName("title")[0].firstChild.nodeValue)
```

The `getElementsByTagName` method returns a list of elements from which the first element was picked. This will output the title `The Great Gatsby` 

Since the `minidom` library follows the old w3c specification of the DOM interface, it feels old and not Pythonic. Moreover, the library source code hasn't received any updates in more than 20 years so.

### The xml.etree.ElementTree library

The ElementTree API is a lightweight, feature-rich Interface for parsing and manipulating XML documents. The implementation is fast and elegant which attracted many third-party libraries to build on it. The documentation of this library is also better than `minidom`. When it was first introduced in Python 2.5, it had a faster C implementation named cElementTree. Nowadays, you don't have to bother as the current implementation is far better in performance than the older implementation.

```py
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
```

The `root` object will contain the parsed XML document. Notice, we created an alias `ET` to shorten the library name in the code, this is a common convention for `ElementTree` based Python scripts. The `fromstring` method takes an XML string as an argument and returns the parsed ElementTree object. Next, you can iter over all the child nodes of the root node and print the texts, using the below code:

```py
for child in root.iter():
   if child.text.strip():
       print(child.text)
```

The output will be:

| The Great GatsbyF. Scott Fitzgerald1925 |
| --- |

How do I parse an XML file?
---------------------------

So far, you've learned how to parse XML documents from Python string objects. Now, let's learn how to parse XML files using these libraries. Fortunately, both `minidom` and `ElementTree` provide a built-in function to parse XML files.

### 1. Parsing XML from file

#### minidom

You can use the `parse` method of `minidom` to read XML content from a file.

```py
from xml.dom.minidom import parse
document = parse("sample.xml")
print(document.getElementsByTagName("title")[0].firstChild.nodeValue)
```

#### ElementTree

The ElementTree library also has a `parse` method to read XML files.

```py
import xml.etree.ElementTree as ET
root = ET.parse("sample.xml")
parsed_dict = dict()
for child in root.iter():
   if child.text.strip():
       parsed_dict[child.tag] = child.text
print(parsed_dict)
```

First, we create a root XML document of the `sample.xml` file using the `parse` method. Then, we're iterating over all the child nodes and storing the data in a `dict` object.

### 2. Converting XML to a dictionary

You can use the `untangle` library to convert XML documents directly to a Python dictionary object. The code is self-explanatory.

```python
import untangle
parsed_dict = untangle.parse("sample.xml")
```

The cool thing about this library is, you can pass a URL, filename, or even an XML string to the `parse` and it will still work.

### 3. Saving parsed XML data to a CSV

You can use the `pandas` library to store the data in a CSV file.

```sql
df = pd.DataFrame(parsed_dict)
df.to_csv("parsed_xml_data.csv", index=False)
```

If you run the above code, it'll initialize a pandas Data Frame `df` with the `parsed_data`. And, save the data in a CSV file named `parsed_xml_data.csv`

Parsing Invalid XML
-------------------

Unfortunately, Python's standard XML libraries don't validate the structure of the XML file. So, it can't parse and extract data from invalid XML files containing invalid characters or, broken tags or elements. For example, take a look at the below XML file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
 <person>
 <name> John Doe</name>
 <message>This is a message & an invalid XML example.</message>
 </person>
</root>
```

At first glance, it might seem like a valid XML but, if you try to parse this XML document you will get an error. Notice the `&` symbol inside the message element, this symbol is an invalid XML character thus all the standard XML libraries will fail to parse this XML file. Now let's try to parse this invalid XML using a couple of methods.

### Method 1: Preprocessing XML documents as strings

For simple XML documents like the above, you can preprocess the XML document as a string to remove the invalid elements or symbols from the XML Document before passing it to the parser.

```python
from xml.dom.minidom import parseString
invalid_xml = """<?xml version="1.0" encoding="UTF-8"?>
<root>
<person>
<name> John Doe</name>
<message>This is a message & an invalid XML example.</message>
</person>
</root>
"""
# preprocessing
valid_xml = invalid_xml.replace("&", "&amp;")
parsed_data = parseString(valid_xml)
```

As you can see in the preprocessing step, the replace method will replace the `&` symbol of the `invalid_xml` with `&amp;`. Now, if you run this script it'll parse the XML document without any errors. There are many ways to preprocess the XML documents sometimes you can take advantage of Python's `re` module to use RegEx and replace complex text as well. However, if the XML document is too large then this method will become cumbersome.

### Method 2: Use a robust parsing Library

If the invalid XML document is too large, it'll be hard to preprocess. In such cases, instead of using a stricter XML parser that doesn't handle broken XML documents, you can use a more forgiving parsing library such as Beautiful Soup. It can take care of invalid XML literals, missing or broken tags, and elements automatically.

```python
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
```

You should keep in mind that, Beautiful Soup is slower than the other XML parsing libraries such as ElementTree or lxml. If performance is an issue then you might've to use preprocessing or other robust libraries instead.

Conclusion
----------

This tutorial has equipped you with a thorough understanding of XML parsing in Python. You have explored various parsing models, delved into the standard library and third-party parsers, and learned about declarative parsing and safe XML parsing practices. With this knowledge, you are now empowered to choose the most suitable XML parser for your needs and handle XML data effectively and efficiently in your Python projects. Last but not least, whenever dealing with XML documents you must pay extra attention as some XML documents can be malicious. Python's standard XML libraries aren't secured enough to protect against such maliciously crafted XML files. To learn more about the vulnerabilities and risks read the official Python XML library [documentation](https://docs.python.org/3/library/xml.html#xml-vulnerabilities).

Frequently asked questions
--------------------------

### 1. Is Python good for file parsing?

Python is one of the most popular general-purpose programming languages. It has sets of powerful libraries that make Python great for file parsing. Since Python is an interpreted programming language, it doesn't provide C, and C++ like performance out of the box. However, you can combine Cython or other faster Python implementations and binaries to improve performance.

### 2. Which is the easiest XML parser?

Python's built-in XML library provides multiple sub-modules and libraries with different syntax and styles giving you the flexibility to choose the one that fits best with your preference. If you're comfortable with DOM manipulation then you might find the `dom` module or `minidom` easier to learn. On the other hand, the `etree` module is also beginner friendly. From the third-party libraries, `lxml` is popular for XML parsing in the Python community. And, if you're familiar with Beautiful Soup, you can use the `BeautifulSoup` library as well. There is another library named [untangle](https://github.com/stchris/untangle) which enables users to convert XML documents into Python `dict` objects with a single line of code. However, this library is not in active development. So, it's not recommended for production use.

### 3. Which is the fastest XML parsing library?

`lxml` is arguably the fastest XML parsing library with support for Xpath, XSLT & XML Schema standards. it's the Python binding for the C libraries [libxml2](https://en.wikipedia.org/wiki/Libxml2) and [libxslt](https://en.wikipedia.org/wiki/Libxslt). This library is not only fast but also packs a familiar interface as ElementTree API with the broadest spectrum of functionalities. It's also compatible with Python's ElementTree. Many libraries such as Beautiful Soup can also utilize the `lxml` parser under the hood to get a performance boost.

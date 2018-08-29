# lxml-etree读取文件
from lxml import etree

xml = etree.parse("./py24.xml")
sxml = etree.tostring(xml, pretty_print=True)

print(sxml)
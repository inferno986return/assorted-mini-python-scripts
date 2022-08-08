from lxml import etree

root = etree.Element("head")
etree.Element("meta", name="dtb:uid" content="-")
etree.Element("meta", name="dtb:depth" content="1")
etree.Element("meta", name="dtb:totalPageCount" content="0")

print(etree.tostring(root))
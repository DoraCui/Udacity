from xml.etree import ElementTree
import pprint

tree = ElementTree.parse('exampleresearcharticle.xml')
root = tree.getroot()

for child in root:
    print(child.tag)

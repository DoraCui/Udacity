from xml.etree import ElementTree
import pprint

tree = ElementTree.parse('exampleresearcharticle.xml')
root = tree.getroot()

for child in root:
    print(child.tag)

ui = root.find('ui')
print ui.text

title_p = root.find('fm/bibl/title/p')
print title_p.text

snm_list = root.findall('fm/bibl/aug/au/snm')
for snm in snm_list:
    print snm.text
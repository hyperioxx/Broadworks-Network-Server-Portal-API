import xml.etree.ElementTree as ET

class Xml_Parser:

    def __init__(self):
        pass

    def parse(self,response):
        root = ET.fromstring(response)
        print root.__dict__







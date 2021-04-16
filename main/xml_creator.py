from lxml import etree as et


class XML_generator:

    def __init__(self, headers):
        self.headers = headers

    def create_root(self, root_name, type_value=None):
        root = et.Element(root_name, type=type_value)
        return root

    def create_child(self, parent, tag, held_value=None):
        child = et.SubElement(parent, tag)
        if held_value is not None:
            child.text = held_value
        return child

    def create_file(self, root):
        data_as_string = et.tostring(root)
        file = open('output.xml', "w")
        file.write(data_as_string)
        return data_as_string
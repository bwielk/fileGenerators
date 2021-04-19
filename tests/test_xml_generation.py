from main.xml_creator import XML_generator
from datetime import datetime

from .test_data.test_data import headers, all_data_to_write


def test_xml_is_generated():
    xml_generator = XML_generator(headers)
    root = xml_generator.create_root("User_data", "user_data_list")
    xml_generator.create_child(root, "Timestamp", str(datetime.now()))
    for user in range(0, len(all_data_to_write)):
        wrapper = xml_generator.create_child(root, "User")
        for i in range(0, len(headers)):
            xml_generator.create_child(wrapper, headers[i], all_data_to_write[user][i])
    xml_generator.create_file(root)

from main.xml_creator import XML_generator
from datetime import datetime

headers = ["First_Name", "Last_Name", "Favourite_Fruit"]

data_to_write_1 = ["Name1", "Surname2", "Apple"]
data_to_write_2 = ["Name2", "Surname3", "Banana"]
data_to_write_3 = ["Name3", "Surname4", "Grapes"]


def test_xml_is_generated():
    users_data = [data_to_write_1, data_to_write_2, data_to_write_3]
    xml_generator = XML_generator(headers)
    root = xml_generator.create_root("User_data", "user_data_list")
    xml_generator.create_child(root, "Timestamp", str(datetime.now()))
    for user in range(0, len(users_data)):
        wrapper = xml_generator.create_child(root, "User")
        for i in range(0, len(headers)):
            xml_generator.create_child(wrapper, headers[i], data_to_write_1[i])
    xml_generator.create_file(root)

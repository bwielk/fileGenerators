from main.xml_creator import XML_generator

headers = ["First_Name", "Last_Name", "Favourite_Fruit"]

data_to_write_1 = ["Name1", "Surname2", "Apple"]


def test_xml_is_generated():
    xml_generator = XML_generator(headers)
    root = xml_generator.create_root("User_data", "user_data_list")
    for i in range(0, len(headers)):
        xml_generator.create_child(root, headers[i], data_to_write_1[i])
    xml_generator.create_file(root)

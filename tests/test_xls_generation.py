from main.xls_and_xlsx_creator import XLS_XLSX_generator

headers = ["First_Name", "Last_Name", "Favourite_Fruit"]

data_to_write_1 = ["Name1", "Surname2", "Apple"]
data_to_write_2 = ["Name2", "Surname3", "Banana"]
data_to_write_3 = ["Name3", "Surname4", "Grapes"]


def test_xls_and_xlsx_generation_works():
    data = [data_to_write_1, data_to_write_2, data_to_write_3]
    xls_generator = XLS_XLSX_generator(headers)
    xls_generator.create_file("./data/firstxls", "xls", data)

def test_xlsx_and_xlsx_generation_works():
    data = [data_to_write_1, data_to_write_2, data_to_write_3]
    xls_generator = XLS_XLSX_generator(headers)
    xls_generator.create_file("./data/firstxlsx", "xlsx", data)

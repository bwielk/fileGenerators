from main.csv_creator import CSV_generator

headers = ["First_Name", "Last_Name", "Favourite_Fruit"]

data_to_write_1 = ["Name1", "Surname2", "Apple"]
data_to_write_2 = ["Name2", "Surname3", "Banana"]
data_to_write_3 = ["Name3", "Surname4", "Grapes"]


def test_csv_is_generated():
    all_data_to_write = [data_to_write_1, data_to_write_2, data_to_write_3]
    csv_generator = CSV_generator(headers)
    csv_generator.create_csv("data/example", all_data_to_write)

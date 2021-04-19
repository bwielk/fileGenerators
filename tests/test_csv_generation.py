from main.csv_creator import CSV_generator

from .test_data.test_data import headers, all_data_to_write


def test_csv_is_generated():
    csv_generator = CSV_generator(headers)
    csv_generator.create_csv("data/example", all_data_to_write)

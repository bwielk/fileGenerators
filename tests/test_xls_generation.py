from main.xls_and_xlsx_creator import XLS_XLSX_generator

from .test_data.test_data import headers, all_data_to_write


def test_xls_and_xlsx_generation_works():
    xls_generator = XLS_XLSX_generator(headers)
    xls_generator.create_file("./data/firstxls", "xls", all_data_to_write)


def test_xlsx_and_xlsx_generation_works():
    xls_generator = XLS_XLSX_generator(headers)
    xls_generator.create_file("./data/firstxlsx", "xlsx", all_data_to_write)

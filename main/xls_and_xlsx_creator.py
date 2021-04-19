import xlsxwriter
import random
import string

class XLS_XLSX_generator:

    def __init__(self, headers):
        self.headers = headers
        self.headers_written = False
        self.initial_worksheet_name = None
        self.workbook = None
        self.allowed_formats = ["xls", "xlsx"]

    def initiate_spreadsheet(self, file_name, format):
        if format not in self.allowed_formats:
            raise Exception("Allowed formats - 'xls' and 'xlsx'")
        file = file_name + "." + format
        workbook = xlsxwriter.Workbook(file)
        letters = string.ascii_lowercase
        self.initial_worksheet_name = ''.join(random.choice(letters) for i in range(10))
        workbook.add_worksheet(self.initial_worksheet_name)
        self.workbook = workbook
        return self.workbook

    def write_headers(self):
        if self.workbook is None:
            raise Exception("Initiate a spreadsheet first!")
        row = 0
        col = 0
        if not self.headers_written:
            for i in range(0, len(self.headers)):
                self.workbook.get_worksheet_by_name(self.initial_worksheet_name).write(row, col, self.headers[i])
                col += 1
            self.headers_written = True

    def write_rows(self, list_of_data_lists):
        if self.headers_written is False:
            raise Exception("Write headers first!")
        row = 1
        col = 0
        for data_per_row in list_of_data_lists:
            current_data = data_per_row
            if len(current_data) == len(self.headers):
                for i in range(0, len(current_data)):
                    self.workbook.get_worksheet_by_name(self.initial_worksheet_name).write(row, col, current_data[i])
                    col += 1
                col = 0
            else:
                raise Exception("Data must fit the number of provided headers")
            row +=1

    def create_file(self, file_name, format, list_of_data_to_enter):
        self.initiate_spreadsheet(file_name, format)
        self.write_headers()
        self.write_rows(list_of_data_to_enter)
        self.workbook.close()



import csv

class CSV_generator:

    def __init__(self, headers):
        self.headers = headers

    def define_csv_writer(self, filename):
        writer = csv.DictWriter(filename, self.headers)
        return writer

    def insert_csv_rows(self, writer, row_data_list):
        if len(self.headers) == len(row_data_list):
            row = {}
            for i in range(0, len(self.headers)):
                row[self.headers[i]] = str(row_data_list[i])
            writer.writerow(row)
        else:
            raise Exception("The data provided doesn't fit the columns of the csv")

    def create_csv(self, filename, list_of_lists_to_write):
        with open(filename + ".csv", mode="w") as pp_list:
            # headers
            writer = self.define_csv_writer(pp_list)
            writer.writeheader()
            for i in range(0, len(list_of_lists_to_write)):
                self.insert_csv_rows(writer, list_of_lists_to_write[i])

import csv
from pprint import pprint

def classfactory(class_name, dictionary):
    return type(class_name,[tuple], dictionary)

class CsvReader:
    data = []

    def __init__(self,filepath):
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data)
            for row in csv_data:
                self.data.append(row)
                pprint(row)
        pass

    def return_data_as_object(self, class_name):
        objects = []
        for row in self.data:
            objects.append(classfactory(class_name,row))
        return objects
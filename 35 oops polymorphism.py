#import pandas as pd

class DataProcessor:
    def process(self, data:None):
        raise NotImplementedError("Subclasses must implement the process method")

class CSVProcessor(DataProcessor):
    def process(self, filepath:None):
        print(f"Processing CSV file: {filepath}")
        return

class JSONProcessor(DataProcessor):
    def process(self, filepath:None):
        print(f"Processing JSON file: {filepath}")
        return

class ExcelProcessor(DataProcessor):
    def process(self, filepath:None):
        print(f"Processing Excel file: {filepath}")
        return

def load_and_process_data(processor, path):
    data = processor.process(path)
    return data

# Using the processors
csv_processor = CSVProcessor()
json_processor = JSONProcessor()
excel_processor = ExcelProcessor()

csv_data = load_and_process_data(csv_processor, "data.csv")
print("-" * 20)
json_data = load_and_process_data(json_processor, "data.json")
print("-" * 20)
excel_data = load_and_process_data(excel_processor, "data.xlsx")
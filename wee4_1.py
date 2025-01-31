import collections
import csv
import os

class InvalidColumnNames(Exception):
    def __init__(self, col_names):
        self.col_names = col_names
        self.msg = f"The names of the columns are invalid. Column names can only be letters and numbers: {col_names}"
        print(self.msg)
        super().__init__(self.msg)

class NoRecordStatsFound(Exception):
    def __init__(self, stats_column_name):
        self.column_name = stats_column_name
        self.msg = f"The column stats you’re trying to access doesn’t exist. You entered {stats_column_name}."
        print(self.msg)
        super().__init__(self.msg)

class Records:
    def __init__(self, file_name, file_title, stats_column):
        self.file_name = file_name
        self.file_title = file_title
        self.stats_column = stats_column
        self.record_dict = collections.defaultdict(lambda: collections.defaultdict(list))
        self.load_data()
    
    # def load_data(self):
    #     while True:
    #         try:
    #             with open(self.file_name, newline='') as file:
    #                 reader = csv.reader(file)
    #                 first_line = next(reader)  # Read column names
    #                 container, standardized_columns, Entry = self._create_container(first_line)
                    
    #                 # Ensure 'data' key is initialized
    #                 container[self.file_title]["data"] = []
    #                 container[self.file_title][f"stats_{self.stats_column}"] = collections.Counter()
                    
    #                 for row in reader:
    #                     entry = Entry(*row)
    #                     container[self.file_title]["data"].append(entry)
                        
    #                     # Update stats counter for the specified column
    #                     column_index = standardized_columns.index(self.stats_column)
    #                     container[self.file_title][f"stats_{self.stats_column}"][row[column_index]] += 1
                    
    #                 self.record_dict[self.file_title] = container[self.file_title]
    #         except FileNotFoundError:
    #             print(f"Error: The file '{self.file_name}' was not found.")
    #             return
    #         else:
    #             print(f"File '{self.file_name}' loaded successfully.")
    #             return

    def load_data(self):
        while True:
            try:
                with open(self.file_name, newline='') as file:
                    reader = csv.reader(file)
                    
                    # Ensure we get a valid first line (skip empty lines)
                    first_line = next(reader)
                    while not any(first_line):  # Skip completely empty lines
                        first_line = next(reader)

                    container, standardized_columns, Entry = self._create_container(first_line)

                    # Ensure 'data' key is initialized
                    container[self.file_title]["data"] = []
                    container[self.file_title][f"stats_{self.stats_column}"] = collections.Counter()

                    for row in reader:
                        row = row[:len(standardized_columns)]  # Trim excess columns
                        while len(row) < len(standardized_columns):
                            row.append('')  # Fill missing values
                            
                        entry = Entry(*row)
                        container[self.file_title]["data"].append(entry)

                        # Update stats counter for the specified column
                        column_index = standardized_columns.index(self.stats_column)
                        container[self.file_title][f"stats_{self.stats_column}"][row[column_index]] += 1

                    self.record_dict[self.file_title] = container[self.file_title]
            except FileNotFoundError:
                print(f"Error: The file '{self.file_name}' was not found.")
                return
            else:
                print(f"File '{self.file_name}' loaded successfully.")
                return

    
    def _create_container(self, first_line):
        standardized_columns = self._standardize_col_names(first_line)
        # Entry = collections.namedtuple("Entry", standardized_columns)
        # return collections.defaultdict(lambda: collections.defaultdict(list)), standardized_columns, Entry
        if not standardized_columns or any(col.strip() == "" for col in standardized_columns):
            raise ValueError(f"Invalid column headers: {standardized_columns}")

        Entry = collections.namedtuple("Entry", standardized_columns)
        return collections.defaultdict(lambda: collections.defaultdict(list)), standardized_columns, Entry
    
    # def _standardize_col_names(self, column_names):
    #     standardized_names = [col.replace("_", "").replace("-", "").replace(" ", "") for col in column_names]
    #     return standardized_names if all(col.isalnum() for col in standardized_names) else []

    def _standardize_col_names(self, column_names):
        standardized_names = [col.replace("_", "").replace("-", "").replace(" ", "") for col in column_names]

        # Ensure at least one valid column name
        if not any(standardized_names):
            raise ValueError("No valid column headers found in file.")

        return standardized_names

    
    def extract_top_n(self, n, file_title, stats_column_name):
        stats_key = f"stats_{stats_column_name}"
        if file_title not in self.record_dict or stats_key not in self.record_dict[file_title]:
            print(f"No statistics found for {stats_column_name} in {file_title}.")
            return []
        return self.record_dict[file_title][stats_key].most_common(n)

if __name__ == "__main__":
    # Default file configurations
    datasets = {
        "Credit Card": ("credit_card.csv", "Period"),
        "Complaints": ("customer_complaints.csv", "Product")
    }
    
    top_n = 10  # Number of most common occurrences to retrieve
    
    for title, (file, column) in datasets.items():
        records = Records(file, title, column)
        if records.record_dict:
            top_values = records.extract_top_n(top_n, title, column)
            print(f"\nTop {top_n} most common values in '{column}' for {title}:")
            for value, count in top_values:
                print(f"{value}: {count} times")
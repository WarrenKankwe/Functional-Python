import os
import csv
from collections import namedtuple

class AutoMPG:
    '''
    Class DocString. 
    A class called AutoMPG that represents attributes that are available for each record in the AutoMPG data set.

    Attributes:
    ----------------------------------------
    make (str): automobile manufacturer. First token in the “car name” field of the data set.
    model (str): automobile model. All the other tokens in the “car name” field of the data set except the first.
    year (int): automobile year of manufacturer. This is the four-digit year that corresponds to the “model year” field of the data set.
    mpg (float): miles per gallon. This is a floating point value that corresponds to the “mpg” field of the data set.

    Methods:
    ----------------------------------------
    __init__ : a constructor that takess four parameters to initialize after self.
    __repr__ and __str__: returns the string representation of the object. One of these can call the other one.
    __eq__: implements equality comparison between two AutoMPG objects.
    __lt__: implements less-than comparison between two AutoMPG objects.
    __hash__: implement an appropriate hash function for these objects.
    '''
    def __init__(self, make: str, model: str, year: int, mpg: float):                                       # Attributes
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg
    
    def __repr__(self):                                                                                     # Methods
        return f"AutoMPG('{self.make}', '{self.model}', {self.year}, {self.mpg})"

    def __str__(self):
        return f"AuttoMPG({self.make}, {self.model}, {self.year}, {self.mpg})"

    def __eq__(self, other):
        if not isinstance(other, AutoMPG):
            return NotImplemented
        return (self.make == other.make and
                self.model == other.model and
                self.year == other.year and
                self.mpg == other.mpg)
    
    def __lt__(self, other):
        if not isinstance(other, AutoMPG):
            return NotImplemented
        if self.make < other.make:
            return True
        elif self.make == other.make:
            if self.model < other.model:
                return True
            elif self.model == other.model:
                if self.year < other.year:
                    return True
                elif self.year == other.year:
                    if self.mpg < other.mpg:
                        return True
        return False

    def __hash__(self):
        return hash((self.make, self.model, self.year, self.mpg))





class AutoMPGData:
    '''
    Class DocString. 
    A class called AutoMPGData that represents represents the entire AutoMPG data set.

    Attributes:
    ----------------------------------------
    Data (str, int, float): a list of AutoMPG objects

    Methods:
    ----------------------------------------
    __init__ : a constructor with no arguments.
    __iter__: to make the class iterable.
    __clean_data__: will read the original data file, convert the TAB character to spaces, and save to a “cleaned” file.
    __load_data__: will load the cleaned data file and instantiate AutoMPG objects and add them to the data attribute.
    '''
    def __init__(self):
        self.data = []
        self._load_data()

    def __iter__(self):
        return iter(self.data)

    def _clean_data(self, original_file: str, clean_file: str):
        with open(original_file, "r") as infile, open(clean_file, "w") as outfile:
            for line in infile:
                cleaned_line = line.expandtabs()                                            # Convert TABs to spaces
                outfile.write(cleaned_line)
                return

    def _load_data(self):
        clean_file = "auto-mpg.clean.txt"
        original_file = "auto-mpg.data.txt"

        if not os.path.exists(clean_file):                                                  # Check if the clean file exists; otherwise, clean the data
            self._clean_data(original_file, clean_file)

        Record = namedtuple("Record", [                                                     # Define a namedtuple for structured row representation
            "mpg", "cylinders", "displacement", "horsepower", "weight", 
            "acceleration", "model_year", "origin", "car_name"])

        with open(clean_file, "r") as file:                                                 # Parse the cleaned file
            reader = csv.reader(file, delimiter=" ", skipinitialspace=True)                 # Handle space-delimited fields
            for row in reader:
                filtered_row = [col for col in row if col]                                  # Filter out empty strings caused by multiple spaces

                if len(filtered_row) != 9:                                                  # Count that we have the right number of fields
                    continue

                record = Record(*filtered_row)

                car_name = record.car_name.strip('"')                                       # Extract make and model from car_name and remove quotes
                make, model = car_name.split(" ", 1) if " " in car_name else (car_name, "")

                try:
                    mpg = float(record.mpg)
                    year = 1900 + int(record.model_year)                                    # Convert model year to 4-digit year

                    self.data.append(AutoMPG(make, model, year, mpg))
                except ValueError:
                    continue
                    return



def main():
    """
    Function DocString. 
    Instantiates an AutoMPGData object and then uses the iterator
    protocol to loop across the object, printing each AutoMPG object.
    
    Args:
    ----------------------------------------
    None

    Return:
    ----------------------------------------
    Prints each AutoMPG object
    """
    for a in AutoMPGData():                                                                 # Loop over the AutoMPGData using the iterator protocol
        print(a)

if __name__ == "__main__":
    main()
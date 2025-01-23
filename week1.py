def paired_list(strings, integers):
    '''
    Function DocString. 
    Combines two lists into a list, pairing them using zip.
    Handles mismatched list length pairs with placeholders.

    Args:
    ----------------------------------------
    strings (list): a list of strings.
    integers (list): a list of integers.

    Returns:
    ----------------------------------------
    list: a list of tuples pairing values from two lists.
    '''

    result = list(zip(strings, integers))                               # Pair lists

    if len(integers) > len(strings):                                    # If the list containing strings is longer
        result.extend(('FNU', i) for i in integers[len(strings):])

    avg = sum(integers) // len(integers)                                # Calculate the average of integers for later use
    if len(strings) > len(integers):                                    # If the list containing integers is longer
        result.extend((j, avg) for j in strings[len(integers):])

    return result

# # Tests
# def test_paired_list():
#     strings1 = ["Matt", "Alice"]
#     integers1 = [99, 50]
#     print(paired_list(strings1, integers1))  # should read [('Matt', 99), ('Alice', 50)]

    # strings2 = ["Matt", "Alice"]
    # integers2 = [99, 50, 25]
    # print(paired_list(strings2, integers2))  # should read [('Matt', 99), ('Alice', 50), ('FNU', 25)]

#     strings3 = ["Matt", "Alice", "Tom", "Jake"]
#     integers3 = [99, 50, 25]
#     print(paired_list(strings3, integers3))  # should read [('Matt', 99), ('Alice', 50), ('Tom', 25), ('Jake', 58)]
# test_paired_list()
# # End of tests





def even_odd_pairs(paired_list, even=True):
    '''
    Function DocString. 
    Filters a list of tuples based on whether the integer in each tuple is even or odd.

    Args:
    ----------------------------------------
    paired_list (list): a list of tuples with a string and an integer.
    even (bool): if True, filters for even integers; if False, filters for odd integers.

    Returns:
    ----------------------------------------
    list: A filtered list of tuples based on the condition.
    '''
    if even:
         return [pair for pair in paired_list if pair[1] % 2 == 0]               # Filtering even integers
    else:
        return [pair for pair in paired_list if pair[1] % 2 != 0]               # Filtering odd integers

# # Tests
# def test_even_odd_pairs():
#     paired_list_result = paired_list(strings2, integers2)

#     # Filtering even integers
#     print(even_odd_pairs(paired_list_result, True))  # [('Alice', 50)]

#     # Filtering odd integers
#     print(even_odd_pairs(paired_list_result, False))  # [('Matt', 99), ('FNU', 25)]
# test_even_odd_pairs()
# # End of tests





# Tent class implementation
class Tent:
    '''
    Class DocString. 
    A class to represent a tent with various attributes and comparison methods.

    Attributes:
    ----------------------------------------
    num_occupants (int): number of occupants
    material (str): material of tent
    setup_time (int): tent setup time
    sqft (float): tent squarefeet
    vestibule (bool): does tent have a vestibule
    weight (float):  tent weight in ounces
    structure_poles (bool): does tent have structural poles
    seasons (int): seasons of tent

    Methods:
    ----------------------------------------
    __str__: returns human readable string
    __repr__: returns official string representationof objects
    __lt__: compares which tent is less than
    is_better: compares which tent is better
    '''
    def __init__(self, num_occupants, material, setup_time, sqft, vestibule, weight,structure_poles=True, seasons=3):       # Attributes
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.sqft = sqft
        self.vestibule = vestibule
        self.weight = weight
        self.structure_poles = structure_poles
        self.seasons = seasons

    def __str__(self):                                                                                                       # Methods
        return (f"Tent({self.num_occupants} occupants, {self.material} material, "
                f"{self.setup_time} min setup, {self.sqft} sqft, "
                f"{'with vestibule' if self.vestibule else 'no vestibule'}, "
                f"{self.weight} oz, "
                f"{'with' if self.structure_poles else 'no'} structure poles, "
                f"{self.seasons}-season)")

    def __repr__(self):
        return (f"Tent(num_occupants={self.num_occupants}, material='{self.material}', "
                f"setup_time={self.setup_time}, sqft={self.sqft}, vestibule={self.vestibule}, "
                f"weight={self.weight}, structure_poles={self.structure_poles}, "
                f"seasons={self.seasons})")
    
    def __lt__(self, other):
        return (self.num_occupants < other.num_occupants) and (self.sqft < other.sqft)

    def is_better(self, other):
        return (self.weight < other.weight and 
                self.setup_time < other.setup_time and 
                self.seasons >= other.seasons)

# # Tests
# tent1=Tent(num_occupants=4, material="polyester", setup_time=6, sqft=36, vestibule=False, weight=12.5, structure_poles=True, seasons=3)
# tent2=Tent(num_occupants=4, material="polyester", setup_time=5, sqft=35, vestibule=False, weight=11.5, structure_poles=True, seasons=3)
# tent3=Tent(num_occupants=3, material="polyester", setup_time=4, sqft=35, vestibule=False,  weight=11.0, structure_poles=True, seasons=4)

# # __lt__ comparisons
# print(tent1 < tent2)  # False (num_occupants is equal, not less)
# print(tent1 < tent3)  # False (num_occupants and sqft are greater)
# print(tent3 < tent1)  # True (num_occupants and sqft are less)
# print(tent3 < tent2)  # False (num_occupants is less, but sqft is the same)

# # is_better comparisons
# print(tent2.is_better(tent1))  # True (weight and setup_time for tent2 are less whilst maintaining the same season rating)
# print(tent3.is_better(tent1))  # True (weight and setup_time for tent3 are less and the season rating is better)
# print(tent1.is_better(tent2))  # False (heavier and longer setup_time)
# # End of tests





class Hammock:
    '''
    Class DocString. 
    A class to represent a hammock with various attributes and comparison methods.

    Attributes:
    ----------------------------------------
    num_occupants (int): number of occupants
    material (str): material of hammock
    setup_time (int): hammock setup time
    weight (float):  hammock weight in ounces
    length (int): hammock length  in feet
    seasons (int): seasons of hammock

    Methods:
    ----------------------------------------
    __str__: returns human readable string
    __repr__: returns official string representationof objects
    __lt__: compares which hammock is less than
    is_better: compares which hammock is better
    '''
    def __init__(self, num_occupants, material, setup_time, weight, length=11, seasons=3):          # Attributes
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.length = length
        self.seasons = seasons

    def __str__(self):                                                                              # Methods
        return (f"Hammock({self.num_occupants} occupants, {self.material} material, "
                f"{self.setup_time} min setup, {self.weight} oz, {self.length} ft length, "
                f"{self.seasons}-season)")

    def __repr__(self):
        return (f"Hammock(num_occupants={self.num_occupants}, material='{self.material}', "
                f"setup_time={self.setup_time}, weight={self.weight}, length={self.length}, "
                f"seasons={self.seasons})")

    def __lt__(self, other):
        return (self.weight < other.weight) and (self.setup_time < other.setup_time)

    def is_better(self, other):
        return (self.weight < other.weight and 
                self.setup_time < other.setup_time and 
                self.seasons >= other.seasons)
    




class Tarp:
    '''
    Class DocString. 
    A class to represent a tarp with various attributes and comparison methods.

    Attributes:
    ----------------------------------------
    num_occupants (int): number of occupants
    material (str): material of tarp
    setup_time (int): tarp setup time
    sqft (float): tarp squarefeet
    weight (float):  tarp weight in ounces
    seasons (int): seasons of tarp

    Methods:
    ----------------------------------------
    __str__: returns human readable string
    __repr__: returns official string representationof objects
    __lt__: compares which tarp is less than
    is_better: compares which tarp is better
    '''
    def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons=3):          # Attributes
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.sqft = sqft
        self.weight = weight
        self.seasons = seasons

    def __str__(self):                                                                              # Methods
        return (f"Tarp({self.num_occupants} occupants, {self.material} material, "
                f"{self.setup_time} min setup, {self.sqft} sqft, {self.weight} oz, "
                f"{self.seasons}-season)")

    def __repr__(self):
        return (f"Tarp(num_occupants={self.num_occupants}, material='{self.material}', "
                f"setup_time={self.setup_time}, sqft={self.sqft}, weight={self.weight}, "
                f"seasons={self.seasons})")

    def __lt__(self, other):
        return (self.num_occupants < other.num_occupants) and (self.sqft < other.sqft)

    def is_better(self, other):
        return (self.weight < other.weight and 
                self.setup_time < other.setup_time and 
                self.seasons >= other.seasons)
    
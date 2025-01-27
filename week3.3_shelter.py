class Tent:
    """
    Instantiates and defines a series of methods for a camping tent object
    Attributes:
    ---------------------------------------
    num_occupants (int): total number of sleeping spots
    material (str): fabric type
    setup_time (int): number of minutes it takes to set up the tent
    sqft (float): total square footage of the tent
    vestibule (bool): True if tent has a vestibule, False otherwise
    weight (float): weight of the tent in ounces
    structure_poles (bool): True if tent has structural poles, False otherwise
    seasons (int): seasons the tent is rated for 3 or 4
    Methods:
    ---------------------------------------
    __lt__: compares two tents based on number of occupants and square footage
    is_better: compares two tents based on weight, setup time, and seasons rating
    """
    def __init__(self, num_occupants, material, setup_time, sqft, vestibule,
    weight, \
    structure_poles=True, seasons=3) -> None:
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.sqft = sqft
        self.vestibule = vestibule
        self.weight = weight
        self.structure_poles = structure_poles
        self.seasons = seasons
    def __lt__(self, other):
        if type(self) == type(other):
            return (self.num_occupants < other.num_occupants) and (self.sqft <
        other.sqft)
        return NotImplemented
    def __str__(self) -> str:
        return self.__repr__()
    def __repr__(self) -> str:
        return f"Tent({self.num_occupants}, {self.material}, {self.setup_time},
    {self.sqft}, \
    {self.vestibule}, {self.weight}, {self.structure_poles},
    {self.seasons})"
    def is_better(self, other) -> bool:
        if type(self) == type(other):
            return (self.weight < other.weight) and (self.setup_time <
        other.setup_time) and \
        (self.seasons >= other.seasons)
        return NotImplemented





class Hammock:
    """
    Instantiates and defines a series of methods for a camping hammock object
    Attributes:
    ---------------------------------------
    num_occupants (int): total number of sleeping spots
    material (str): fabric type
    setup_time (int): number of minutes it takes to set up the tent
    weight (float): weight of the tent in ounces
    length (int): length of a hammock in feet
    seasons (int): seasons the tent is rated for 3 or 4
    Methods:
    ---------------------------------------
    __lt__: compares two hammocks based on weight and setup time
    is_better: compares two hammocks based on weight, setup time, and seasons
    rating
    """
    def __init__(self, num_occupants, material, setup_time, weight, length=11,
    seasons=3) -> None:
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.length = length
        self.seasons = seasons
    def __lt__(self, other):
        if type(self) == type(other):
            return (self.weight < other.weight) and (self.setup_time < other.setup_time)
        return NotImplemented
    def __str__(self) -> str:
        return self.__repr__()
    def __repr__(self) -> str:
        return f"Hammock({self.num_occupants}, {self.material}, {self.setup_time}, \
        {self.weight}, {self.length}, {self.seasons})"
    def is_better(self, other) -> bool:
        if type(self) == type(other):
            return (self.weight < other.weight) and (self.setup_time <
        other.setup_time) and \
        (self.seasons >= other.seasons)
        return NotImplemented





class Tarp:
    """
    Instantiates and defines a series of methods for a camping tarp object
    Attributes:
    ---------------------------------------
    num_occupants (int): total number of sleeping spots
    material (str): fabric type
    setup_time (int): number of minutes it takes to set up the tent
    sqft (float): total square footage of the tent
    weight (float): weight of the tent in ounces
    seasons (int): seasons the tent is rated for 3 or 4
    Methods:
    ---------------------------------------
    __lt__: compares two tents based on number of occupants and square footage
    is_better: compares two tents based on weight, setup time, and seasons rating
    """
    def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons=3)
    -> None:
    self.num_occupants = num_occupants
    self.material = material
    self.setup_time = setup_time
    self.sqft = sqft
    self.weight = weight
    self.seasons = seasons
    def __lt__(self, other):
        if type(self) == type(other):
            return (self.num_occupants < other.num_occupants) and (self.sqft <
    other.sqft)
        return NotImplemented
    def __str__(self) -> str:
        return self.__repr__()
    def __repr__(self) -> str:
        return f"Tarp({self.num_occupants}, {self.material}, {self.setup_time},
        {self.sqft}, \
        {self.weight}, {self.seasons})"
    def is_better(self, other) -> bool:
        if type(self) == type(other):
            return (self.weight < other.weight) and (self.setup_time <
    other.setup_time) and \
    (self.seasons >= other.seasons)
        return NotImplemented
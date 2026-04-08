class NotSleeping:
    '''
    A class making counting sheeps.

    Attributes:
        name (str): The name of the person.
        count_sheeps (int): The number of sheep counted so far.

    Methods:
        add_sheep(): Increments the sheep count by one.
    '''
    def __init__(self, name, count_sheeps = 0):
        '''
        Initialize  person's sleeping.

        Args:
            name (str): The name of the person.
            count_sheeps (int): Initial number of sheep counted.
        '''
        self.name = name
        self.count_sheeps = count_sheeps

    def add_sheep(self) -> None:
        '''
        Adds one sheep to the count_sheeps.

        Returns:
            None
        '''
        self.count_sheeps += 1
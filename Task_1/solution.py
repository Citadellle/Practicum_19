class Dog:
    '''
    The class making a dog.

    Attributes:
        name (str): Name of dog

    Methods:
        say(): Prints a dog barking
    '''
    def __init__(self, name: str):
        '''
        Initialize a dog.

        Args:
            name (str): The name of the dog.
        '''
        self.name = name

    def __str__(self):
        '''
        Method returning str name of dog.

        Return: dog name
        '''
        return self.name

    def say(self) -> None:
        '''
        Method prints the sound a dog makes.

        Return: 
            None
        '''
        print('Гав!')
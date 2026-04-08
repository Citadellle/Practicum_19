class User:
    '''
    A class making a user information.

    Attributes:
        id (int): Unique identifier of the user.
        nick_name (str): User's nickname.
        first_name (str): User's first name.
        last_name (str): User's last name (optional).
        middle_name (str): User's middle name (optional).
        name (list): List containing [first_name, last_name, middle_name].
        gender (str): User's gender (optional).

    Methods:
        update(): Updates user information.
    '''
        
    def __init__(self,
                 id : int,
                 nick_name: str,
                 first_name: str,
                 last_name: str = None,
                 middle_name: str = None,
                 gender: str = None):
        '''
        Initialize of user information.

        Args:
            id (int): Unique identifier of the user.
            nick_name (str): User's nickname.
            first_name (str): User's first name.
            last_name (str): User's last name (optional).
            middle_name (str): User's middle name (optional).
            gender (str): User's gender (optional).
        '''
        self.id = id
        self.nick_name = nick_name

        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.name = [first_name, last_name, middle_name]

        self.gender = gender
    
    def __str__(self):
        '''
        Returns a formatted string with user information.

        Returns:
            str: Formatted user data including ID, login, name, and optionally gender.
        '''
        name_pr = ' '.join(n for n in self.name if n)
        string = f'ID: {self.id} LOGIN: {self.nick_name} NAME: {name_pr} '

        if self.gender:
            string += f'GENDER: {self.gender}'

        return string

    def __repr__(self):
        '''
        Returns a string representation of the user.

        Returns:
            str: User's nickname.
        '''
        return self.nick_name
    
    def update(self,
               id : int = 0,
               nick_name: str = '',
               first_name: str = '',
               last_name: str = '',
               middle_name: str = '',
               gender: str = '') -> None:
        '''
        Updates user information with non-empty or non-zero values.

        Args:
            id (int): New ID (if not 0).
            nick_name (str): New nickname (if not empty).
            first_name (str): New first name (if not empty).
            last_name (str): New last name (if not empty).
            middle_name (str): New middle name (if not empty).
            gender (str): New gender (if not empty).

        Returns:
            None
        '''
        if id != 0:
            self.id = id
        if nick_name != '':
            self.nick_name = nick_name
        if first_name != '':
            self.name[0] = first_name
        if last_name != '':
            self.name[1] = last_name
        if middle_name != '':
            self.name[2] = middle_name
        if gender != '':
            self.gender = gender
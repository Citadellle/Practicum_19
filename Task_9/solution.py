class StrandsDNA:
    '''
    A class representing a collection of DNA strands.

    Attributes:
        all_strands (List): List of DNA strand strings.

    Methods:
        add_strands(): Adds new DNA strands to the collection.
        get_max_strands(): Returns the longest unique DNA strands sorted alphabetically.
    '''

    def __init__(self, all_strands: list = []):
        '''
        Initialize a new StrandsDNA instance.

        Args:
            all_strands (List): Initial list of DNA strands. Defaults to empty list.
        '''
        self.all_strands = all_strands
    
    def __str__(self):
        '''
        Returns a string representation of all DNA strands.

        Returns:
            str: Space-separated DNA strands.
        '''
        return ' '.join(self.all_strands)
    
    def add_strands(self, strands) -> None:
        '''
        Adds new DNA strands to the collection.

        Args:
            strands (str): Space-separated DNA strands to add.

        Returns:
            None
        '''
        self.all_strands.extend(strands.split())

    def get_max_strands(self) -> str:
        '''
        Returns the longest unique DNA strands sorted alphabetically.

        Returns:
            str: Space-separated longest DNA strands (unique, sorted).
        '''
        max_len = max(len(strand) for strand in self.all_strands)
        strands_max_len = list({strand for strand in self.all_strands 
                           if len(strand) == max_len})
        strands_max_len.sort()

        return ' '.join(strands_max_len)
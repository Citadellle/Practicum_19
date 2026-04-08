from typing import Dict

class Game:
    '''
    A class making a basketball game.

    Attributes:
        command1 (str): Name of the first command.
        command2 (str): Name of the second command.
        score (dict): Dictionary storing scores for both commands.

    Methods:
        ball_thrown(): Adds points to a specified command.
        get_score(): Returns current scores of both commands.
        get_winner(): Returns the name of the winning command or 'Tie'.
    '''
    
    def __init__(self,
                 commands: Dict[str : str, str : str]):
        '''
        Initialize a new game.

        Args:
            commands (Dict[str, str]): Dictionary with keys 
                'command1' and 'command2' containing command names.
        '''
        self.command1 = commands['command1']
        self.command2 = commands['command2']
        self.score = {self.command1 : 0, self.command2 : 0}
    
    def ball_thrown(self,
                    command: int,
                    points: int):
        '''
        Adds points to a specified command.

        Args:
            command (int): Command number.
            points (int): Number of points to add.

        Returns:
            None
        '''
        match command:
            case 1:
                self.score[self.command1] += points
            case 2:
                self.score[self.command2] += points

    def get_score(self):
        '''
        Returns current scores of both commands.

        Returns:
            tuple: (score_command1, score_command2)
        '''
        return self.score[self.command1], self.score[self.command2]
    
    def get_winner(self):
        '''
        Returning the winner command of the game.

        Returns:
            str: Name of the winning command, or 'Ничья' if scores are equal.
        '''
        command1_score = self.score[self.command1]
        command2_score = self.score[self.command2]
        result_game = command1_score > command2_score

        match result_game:
            case True:
                return self.command1
            case False:
                return self.command2
            case _:
                return 'Ничья'
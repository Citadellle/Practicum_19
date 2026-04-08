class TrafficLight:
    '''
    A class representing a traffic light with a sequence of signals.

    Attributes:
        permisiible_values (list): List of valid traffic light signals 
                                    in order.
        current_signal (str): The current signal of the traffic light.

    Methods:
        next_signal(): Changes the current signal to the next one 
                        in the sequence.
    '''
    permisiible_values = ['зелёный', 'желтый', 'красный', 'желтный']

    def __init__(self, current_signal: str = 'зелёный'):
        '''
        Initialize a new TrafficLight.

        Args:
            current_signal (str): The initial signal. Defaults to 'green'.
        '''
        self.current_signal = current_signal

    def next_signal(self) -> None:
        '''
        Changes the current signal to the next one in the cyclic sequence.

        Returns:
            None
        '''
        num_cur_sign = TrafficLight.permisiible_values.index(
                        self.current_signal)
        self.current_signal = TrafficLight.permisiible_values[
                        (num_cur_sign + 1) % 4]
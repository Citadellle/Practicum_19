class MorseMsg:
    '''
    A class representing a message encoded in Morse code.

    Attributes:
        encode_str (str): The Morse code string (dots and dashes, space-separated).
        eng_decode_str (list): List of decoded English letters.
        ru_decode_str (list): List of decoded Russian letters.

    Methods:
        eng_decode(): Decodes Morse code to English text.
        ru_decode(): Decodes Morse code to Russian text.
        get_vowels(): Returns vowels from the decoded message for a given language.
        get_consonants(): Returns consonants from the decoded message for a given language.
    '''

    def __init__(self, encode_str):
        '''
        Initialize a new MorseMsg instance.

        Args:
            encode_str (str): The Morse code string to be decoded.
        '''
        self.encode_str = encode_str
        self.eng_decode_str = []
        self.ru_decode_str = []

    def __str__(self):
        '''
        Return string representation of the object.

        Returns:
            str:Original Morse code message.
        '''
        return self.encode_str
    
    def eng_decode(self) -> str:
        '''
        Decodes Morse code to English text.

        Returns:
            str: Decoded English string.
        '''
        morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                      '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                      '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                      '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                      '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                      '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                      '-.--': 'Y', '--..': 'Z'}
        for letter in self.encode_str.split():
            self.eng_decode_str.append(morse_dict[letter])
        
        return ''.join(self.eng_decode_str)
    
    def ru_decode(self) -> str:
        '''
        Decodes Morse code to Russian text.

        Returns:
            str: Decoded Russian string.
        '''
        morse_dict = {'.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д',
                      '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й',
                      '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
                      '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У',
                      '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
                      '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь',
                      '..-..': 'Э', '..--': 'Ю', '.-.-': 'Я'}
        for letter in self.encode_str.split():
            self.ru_decode_str.append(morse_dict[letter])
        
        return ''.join(self.ru_decode_str)
    
    def get_vowels(self, lang) -> list:
        '''
        Returns vowels from the decoded message for a given language.

        Args:
            lang (str): Language.

        Returns:
            list: List of vowel letters from the decoded message.
        '''
        vowels_eng = []
        vowels_ru = []

        match lang:
            case 'eng':
                for letter in self.eng_decode_str:
                    if letter in 'AEIOUY':
                        vowels_eng.append(letter)
                return vowels_eng
            case 'ru':
                for letter in self.ru_decode_str:
                    if letter in 'АЕИОУЫЭЮЯ':
                        vowels_ru.append(letter)
                return vowels_ru
    
    def get_consonants(self, lang) -> list:
        '''
        Returns consonants from the decoded message for a given language.

        Args:
            lang (str): Language.

        Returns:
            list: List of consonant letters from the decoded message.
        '''
        consonants_eng = []
        consonants_ru = []

        match lang:
            case 'eng':
                for consonant in self.eng_decode_str:
                    if consonant in 'BCDFGHJKLMNPQRSTVWXZ':
                        consonants_eng.append(consonant)
                return consonants_eng
            case 'ru':
                for consonant in self.ru_decode_str:
                    if consonant in 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
                        consonants_ru.append(consonant)
                return consonants_ru
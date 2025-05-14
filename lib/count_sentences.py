import re

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self._value = value
        else:
            self._value = ''
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        '''Returns True if the string ends with a period.'''
        return self._value.endswith('.')
    
    def is_question(self):
        '''Returns True if the string ends with a question mark.'''
        return self._value.endswith('?')
    
    def is_exclamation(self):
        '''Returns True if the string ends with an exclamation mark.'''
        return self._value.endswith('!')
    
    def count_sentences(self):
        '''Counts the number of sentences in the string.'''
        # Split the string by sentence-ending punctuation
        sentences = re.split(r'[.?!]', self._value)
        # Remove empty strings that may appear due to trailing punctuation or spaces
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
import json
import random

class NameGenerator(object):
    
    def __init__(self, url):
        json_file = open(url, "r")
        data = json.load(json_file)
        self.consonants = data["consonants"]
        self.vowels = data["vowels"]
        
    def generate_name(self):
        choice = random.randrange(6)
        num_syllables = 1 if choice == 0 else 3 if choice > 3 else 2
        name = ""
        for _ in range(num_syllables):
            name += self.generate_syllable()
            if len(name) == num_syllables == 1:
                name += self.generate_syllable()
        
        #TODO titles ("the X")
        name = name[0].capitalize() + name[1:]
        return name
    
    def generate_syllable(self):
        syllable = ""
        if random.randrange(4) > 0:
            syllable += self.random_consonant()
        syllable += self.random_vowel()
        if random.randrange(4) > 0:
            syllable += self.random_consonant()
        return syllable
    
    def random_consonant(self):
        return self.consonants[random.randrange(len(self.consonants))]
    
    def random_vowel(self):
        return self.vowels[random.randrange(len(self.vowels))]
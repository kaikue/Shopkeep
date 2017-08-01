import json
import random

class NameGenerator(object):
    
    def __init__(self, url):
        json_file = open(url, "r")
        data = json.load(json_file)
        self.consonants = data["consonants"]
        self.start_consonants = data["start_consonants"]
        self.end_consonants = data["end_consonants"]
        self.vowels = data["vowels"]
        self.titles = data["titles"]
        
    def generate_name(self):
        #pick number of syllables- 1/6 chance of 1, 2/3 chance of 2, 1/6 chance of 3
        choice = random.randrange(6)
        num_syllables = 1 if choice == 0 else 3 if choice == 1 else 2
        
        name = ""
        for _ in range(num_syllables):
            name += self.generate_syllable()
            
            #prevent single-character names
            if len(name) == num_syllables == 1:
                name += self.generate_syllable()
        
        if random.randrange(3) == 0:
            name += " the " + self.random_title()
        
        #capitalize first letter
        name = name[0].capitalize() + name[1:]
        
        return name
    
    def generate_syllable(self):
        syllable = ""
        if random.randrange(4) > 0:
            syllable += self.random_consonant(False)
        syllable += self.random_vowel()
        if random.randrange(4) > 0:
            syllable += self.random_consonant(True)
        return syllable
    
    def random_consonant(self, end):
        if end:
            other_consonants = self.end_consonants
        else:
            other_consonants = self.start_consonants
        
        num_consonants = len(self.consonants)
        choice = random.randrange(num_consonants + len(other_consonants))
        return self.consonants[choice] if choice < num_consonants else other_consonants[choice - num_consonants]
    
    def random_vowel(self):
        return self.vowels[random.randrange(len(self.vowels))]
    
    def random_title(self):
        return self.titles[random.randrange(len(self.titles))]
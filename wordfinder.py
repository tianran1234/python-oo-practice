"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self,path):
        f = open(path,'r')
        self.words = self.parse(f)
        print(f"{len(self.words)} words read")


    def random(self):
        return random.choice(self.words)

    def parse(self,f):
        return [word.strip() for word in f]


class SpeicalWordFiner(WordFinder):
    

    def __init__(self,path):
        super().__init__(path)

    def parse(self,f):
        return [word.strip() for word in f if word.strip() and not word.startswith('#')]






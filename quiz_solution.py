
from google.colab import files

uploaded = files.upload()

import string

def is_palindrom(word):
    word = ''.join(c.lower() for c in word if c not in string.punctuation)
    if word == word[::-1]:
        return True
    return False

with open('words.txt') as f:
      for numb,line in enumerate(f, 1):
        if is_palindrom(line.strip()):
            print('positive')
        else:
            print('negative')

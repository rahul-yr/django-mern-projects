
import random
import string

def generateRandomVariable(name):
     letters = string.ascii_lowercase
     gen = ''.join(random.sample(letters,5))
     return name.lower()+'_'+gen



# print(generateRandomVariable('RAHREDDY'))
import string
import random
import pyperclip

class Password:
  characters = {
    "LOWERCASE": string.ascii_lowercase,
    "UPPERCASE": string.ascii_uppercase,
    "SPECIAL": string.punctuation
  }
  
  def __init__(self, length = 12):
    self.length = length
    self.password = self.generate()

  def shuffle(self, string):
    string = list(string)
    random.shuffle(string)
    return "".join(string)

  def generate(self):
    password = ""

    # generate random characters, 1/3 from each bank
    for bank in self.characters:
      for i in range(self.length // 3):
        password += random.choice(self.characters[bank])

    # make up for missing characters with lowercase letters
    while len(password) < self.length:
      password += random.choice(self.characters["LOWERCASE"])

    # shuffle password
    password = self.shuffle(password)
    
    return password

  def __str__(self):
    return self.password

def main():
  password = Password()
  print(password)
  pyperclip.copy(str(password))

if __name__ == "__main__":
  main()

print("Welcome to Animal Sound game!")
print()
print("To exit the game reply 'yes' or 'no' when asked the question 'Do you want to exit?'")


def animalSound():
  quitList = ["y","yes", 'quit', 'exit']
  exit = ""
  while exit.lower() not in quitList:
    print()
    animal = input("What animal do you want?: ")
    if animal.isnumeric() == False: 
      if(animal.lower() == "cow" or animal.lower()=="cattle"):
        print()
        print("A",animal,"goes moo!")
      elif animal.lower() == "dog":
        print()
        print("A",animal,"barks it goes woof!")  
      elif animal.lower() == "cat":
        print()
        print("A",animal,"goes meow!")  
      elif animal.lower() == "snake":
        print()
        print("A",animal,"hiss! or rattle!")    
      elif animal.lower() == "bird":
        print()
        print("A",animal,"chirps!")    
      elif animal.lower() == "wolf":
        print()
        print("A",animal,"howls!")  
      elif animal.lower() == "squirrel":
        print()
        print("A",animal,"squeaks!")  
      elif animal.lower() == "lion":
        print()
        print("A",animal,"roars!")
      elif animal.lower() == "giraffe":
        print()
        print("A",animal,"bleats!")  
      elif animal.lower() == "frog":
        print()
        print("A",animal,"croaks!")  
      elif animal.lower() == "hyena":
        print()
        print("A",animal,"laughs!")  
      elif animal.lower() == "dolphin":
        print()
        print("A",animal,"chirps!")  
      elif animal.lower() == "eagle":
        print()
        print("A",animal,"screeches!")  
      else:
        print()
        print("Oops! I don't know that kind of animal.")  
    else:
      print()
      print("Oops! invalid characters.")

    print()
    exit = input("Do you want to exit?: ")


def endGame():
  while True:
    print()
    input("""Thank you for playing!
To play again please click Stop on top right page and click Run """)
    print()
    continue

if __name__ == "__main__":
  animalSound()
  endGame()
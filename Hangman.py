import random 



print('''
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
''')

print("🎮 Welcome to the Hangman Game 🎯")
print("Guess the word before you run out of lives!\n")

stages = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]



lives = 6

word_list = ["lamborghini", "porsche", "ferrari", "bugatti", "mcLaren", "astonMartin", "rollsRoyce", "bentley", "maserati", "pagani"]

chosen_word = random.choice(word_list)



word_lengtn = len(chosen_word)

placeholder = ""

for possition in range(word_lengtn):
  placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:

  guess = input("Guess The latter: ").lower()

  if guess in correct_letters:
    print(f"You've already guessed {guess}. Try again.")
    lives-=1
    print(f'{lives} lives left.')
    if lives == 0:
      print("You lose.")
      game_over= True
      print(f"The word was: {chosen_word}")

  display = ""

  for latters in chosen_word:
    if guess in latters:
      display += latters

      correct_letters.append(guess)
    elif latters in correct_letters:
      display += latters
    else:
      display += "_"

    
  print(display)

  if guess not in chosen_word:
    lives-=1
    print(stages[lives])
    print(f'{lives} lives left.')
    if lives == 3:
      print("⚠️ You’re about to lose! Only 3 lives left.")
    elif lives==1:
      print("😨 Last chance! Just 1 life left.")
    if lives == 0:
      print("💀 You’re out of lives! You lose.")
      print(f"The word was: {chosen_word}")
      game_over= True
      print("You lose.")

  if "_" not in display:
          game_over = True
          print("\n🎉 You win!")
          print("""
            +---+
            |   |
                |
            😄  |
                |
                |
          =========
          """)


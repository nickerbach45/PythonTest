from time import sleep
class Hangman():
  def init(self):
    print ("Welcome to 'Hangman game, you need to guess the word or else ...")
    print ("you will be hanged")
    print ("press enter to continue")
    input("->")
    self.start_game()
    def start_game(self):
        print ("Starting game...")
        sleep(1)
        self.core_game()
    
    def core_game(self):
        guesses = 0
        letters_used = ""
        the_word = "pizza"
        progress = ['*','*','*','*','*']
    
        while guesses < 6:
            guess = input("Guess a letter ->")
    
            if (guess in the_word) and (guess not in letters_used):
                print ("Your guess was RIGHT!")
                letters_used +=  guess +","
                self.hangman_graphic(guesses)
                print ("Progress: " + self.progress_updater(guess, the_word, progress))
                print ("Letter used: " + letters_used)
            elif (guess not in the_word) and (guess not in letters_used):
                guesses += 1
                print ("Wrong Guess!")
                letters_used += guess + ","
                self.hangman_graphic(guesses)
                print ("Progress: " + "".join(progress))
                print ("Letter used: " + letters_used)
            else:
                print ("You already typed this letter")
                print ("Try again!")
            if ''.join(progress) == the_word:
                print ("You Guessed the word:" + the_word)
                print ("You Won")
                break
    
    
    
    
    def hangman_graphic(self, guesses):
        if guesses == 0:
            print ("________      ")
            print ("|      |      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
        elif guesses == 1:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
        elif guesses == 2:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /       ")
            print ("|             ")
            print ("|             ")
        elif guesses == 3:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|      ")
            print ("|             ")
            print ("|             ")
        elif guesses == 4:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|             ")
            print ("|             ")
        elif guesses == 5:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     /       ")
            print ("|             ")
        else:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     / \     ")
            print ("|             ")
            print("YOU LOST")
            print ("GAME OVER!")
            self.__init__()
    
    def progress_updater(self, guess, the_word, progress):
        i = 0
        while i < len(the_word):
            if guess == the_word[i]:
                progress[i] = guess
                i += 1
            else:
                i += 1
    
        return "".join(progress)
    game = Hangman()
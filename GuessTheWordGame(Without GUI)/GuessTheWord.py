# Guess The Word Game
# Let you fill the blank of the missing letters to guess the word
import random


class GuessTheWord:
    def __init__(self):
        self.list_of_words = ["THE AMAZING SPIDER-MAN", "IRON-MAN", "VICTOR", "HULK"]  # you can add/remove words you want to guess
        # add description of the word and must be with the same index
        self.list_of_descriptions = ["Friendly neighborhood superhero", "Genius superhero", "Thor Wannabe", "Green Hero"]  
        self.chosen_word = random.choice(self.list_of_words)
        self.index_of_chosen_word = self.list_of_words.index(self.chosen_word)
        self.chosen_description = self.list_of_descriptions[self.index_of_chosen_word]
        self.blanks = []
        self.hint_letters = []
        self.guess_word = ""
        self.tries = 5

        self.creating_blanks()
        self.start_game()

    def creating_hints(self):
        alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        for counter in range(4, 7):  # generates 4 to 7 random alphabet and add to the hint_letters list
            random_letters = random.choice(alphabet.split())
            self.hint_letters.append(random_letters)

    def creating_blanks(self):
        self.creating_hints()
        for counter in range(len(self.chosen_word)):  # creates blanks based on how many letters are there in chosen_word
            if self.chosen_word[counter] in self.hint_letters:  # put the hint_letters if the chosen_word has it
                self.blanks.append(self.chosen_word[counter])
            elif self.chosen_word[counter] == " ":  # if there's a space in the word, replace it with a space
                self.blanks.append(" ")
            elif self.chosen_word[counter] == "-":  # if there's a hyphen in the word, replace it with a hyphen
                self.blanks.append("-")
            else:  # if the letters in chosen_word not satisfy the statements above, then replace it with blanks.
                self.blanks.append("_")

    def start_game(self):
        print("Your guess word is: {}".format(" ".join(self.blanks)))
        print("Description: {}".format(self.chosen_description))

        while self.chosen_word != self.guess_word:
            if self.tries == 0:
                print("\nSorry you're out of lives!")
                print(self.chosen_word)
                exit()
            else:
                user_input = input("\nEnter your guess: ")
                letter = user_input.upper()
                if letter in self.blanks:
                    print("Letter '{}' is already available.".format(letter))
                    print("Your guess word is: {}".format(" ".join(self.blanks)))
                elif letter in self.chosen_word:  # if the user inputs the correct letter then replace the blanks with it
                    for index in range(len(self.chosen_word)):  # scanning if there's multiple same letters in chosen_word
                        if self.chosen_word[index] == letter:
                            self.blanks[index] = letter
                            self.guess_word = "".join(self.blanks)
                    print("Your guess word is: {}".format(" ".join(self.blanks)))
                else:
                    self.tries -= 1
                    print("Wrong guess! You only have {} tries left".format(self.tries))
                    print("Your guess word is: {}".format(" ".join(self.blanks)))
        print("You've guessed it right!!")


main = GuessTheWord()


#Hangman Game
import random;
from wordlist import words

hangman_art = {0:("  ",
                  "  ",
                  "  "),
               1:(" O ",
                  "  ",
                  "  "),
               2:(" O ",
                  " |",
                  "  "),
               3:(" O ",
                  "/| ",
                  "  "),
               4:(" O ",
                  "/|\\ ",
                  "  "),
               5:(" O ",
                  "/|\\ ",
                  "/ "),
               6:(" O ",
                  "/|\\ ",
                  "/ \\")}

def create_hangman(wrong_guesses):
    print("********************");
    for line in hangman_art[wrong_guesses]:
        print(line);
    print("********************");

def display_hint(hints):
    print(" ".join(hints));

def display_answer(answer):
    print(" ".join(answer));

def main():
    answer = random.choice(words);

    hints =["_"] * len(answer);
    wrong_guesses = 0;
    guessed_letter = set();
    is_running = True;

    while is_running :
        create_hangman(wrong_guesses);
        display_hint(hints);
        print("Category: District of Nepal");
        guess = input("Enter a letter:").lower();

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input");
            continue;
        
        if guess in guessed_letter :
            print(f"{guess} is already guessed");
        
        guessed_letter.add(guess);

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess :
                    hints[i] = guess;
        else :
            wrong_guesses +=1;

        if "_" not in hints:
            create_hangman(wrong_guesses);
            display_answer(answer);
            print("You Won");
            is_running = False;
        elif wrong_guesses >= len(hangman_art) -1:
            create_hangman(wrong_guesses);
            display_answer(answer);
            print("You Lose");
            is_running = False;

if __name__ == "__main__":
    main();


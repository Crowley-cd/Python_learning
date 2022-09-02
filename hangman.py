import random

def add_letter_to_file(letter, position, out_word):
    if position == 1:
        start, end = out_word[0], out_word[position + 1:]
    elif position == 0:
        start, end = '', out_word[1:]
    elif position == len(out_word) - 1:
        start, end = out_word[:position], ''
    else:
        start, end = out_word[:position], out_word[position + 1:]
    word = start + letter + end
    return word

def enter_letter(show_word):
    print(show_word)
    guess_letter = input('Input a letter:')
    guess_letter = check(guess_letter)
    if guess_letter == 'False':
        return enter_letter(show_word)
    enter_letters.append(guess_letter)
    return guess_letter

def check(letter):
    while len(letter) != 1:
        print('Please, input a single letter.')
        print()
        return "False"

    while letter in enter_letters:
        print("You've already guessed this letter.")
        print()
        return "False"

    while letter not in 'abcdefghijklmnopqrstuvwxyz':
        print("Please, enter a lowercase letter from the English alphabet.")
        print()
        return "False"

    return letter


def start_game():
    global win_count
    global lost_count
    global live
    global rand_word

    global enter_letters
    enter_letters.clear()

    show_word = ''

    for i in range(len(rand_word)):
        show_word += '-'



    while live != 0:
        # print(show_word)
        if rand_word == show_word:
            print(f'You guessed the word {rand_word}!\nYou survived!')
            win_count += 1
            main_menu()

        guess_letter = enter_letter(show_word)

        if guess_letter in rand_word:
            for l in range(len(rand_word)):
                if guess_letter == rand_word[l]:
                    show_word = add_letter_to_file(guess_letter, l, show_word)
        if guess_letter not in rand_word:
            live -= 1
            print("That letter doesn't appear in the word.")
            print()

    print('\nYou lost!')
    lost_count += 1
    main_menu()


def result_board():
    global win_count
    global lost_count
    print(f'You won: {win_count} times.')
    print(f'You lost: {lost_count} times.')
    main_menu()


def main_menu():
    do = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    do = do.lower()
    if do == 'play':
        start_game()
    elif do == 'results':
        result_board()
    elif do == 'exit':
        exit(1)
    else:
        print('Try again')


live = 8
win_count = 0
lost_count = 0
enter_letters = []
word_list = ('python', 'java', 'swift', 'javascript')
rand_word = random.choice(word_list)


print('H A N G M A N')

main_menu()





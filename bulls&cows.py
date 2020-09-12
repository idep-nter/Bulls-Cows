import random
import datetime

def main():
    """
    Prints an intro to the game, starts the game while clocking the time and
    when it's over, it shows results and history of previous games if desired.
    At last it asks user if he wants to repeat the game.
    """
    while True:
        print('Hi there!')
        print('I\'ve generated a random 4 digit number for you.')
        print('Let\'s play a bulls and cows game.')
        n = gen_num()
        start = datetime.datetime.now()
        n_of_guesses = 0

        while True:
            n_of_guesses += 1
            guess = num_guess()
            comparsion = compare(n, guess)
            bulls, cows = comparsion['bulls'], comparsion['cows']
            print(f'{bulls} bulls, {cows} cows')
            check = check_if_over(bulls)
            if check == True:
                break

        end = datetime.datetime.now()
        length = end - start
        evaluation = result(n_of_guesses, length)
        save = save_results(n_of_guesses, length)
        q1 = input('Do you want to show history of previous games?')
        if q1 == 'y':
            show_history = history()
        q2 = input('Do you want to play again?')
        if q2 == 'y':
            continue
        else:
            break

def gen_num():
    """
    Generates a number with 4 unique digits.
    """
    num = ''
    while len(num) != 4:
        n = random.randint(0, 9)
        if str(n) not in num:
            num += str(n)
    return num

def num_guess():
    """
    Checks user's input if all digits are unique and length is four.
    """
    ok_guess = ''
    while len(ok_guess) != 4:
        guess = input('Enter a number: ')
        for i in guess:
            if str(i) not in ok_guess:
                ok_guess += str(i)
            else:
                print('Digits must be unique!')
                ok_guess = ''
                break
        if len(guess) != 4:
            print('Number must be 4 digits!')
            ok_guess = ''
    return ok_guess

def compare(n, guess):
    """
    Compares both numbers and returns number of cows and bulls.
    """
    result = {'cows' : 0, 'bulls' : 0}
    for i, num in enumerate(n):
        if num == guess[i]:
            result['bulls'] += 1
        elif num in guess:
            result['cows'] += 1
        else:
            continue
    return result

def check_if_over(bulls):
    """
    Checks the number of bulls and returns True if it's enough.
    """
    if bulls >= 3:
        return True

def result(n_of_guesses, length):
    """
    Evaluates result according to specified criteria and prints it.
    """
    length_minutes = length.seconds // 60
    if n_of_guesses < 5 and length_minutes < 1:
        print(f'Correct, you\'ve guessed the right number in {n_of_guesses} '
              f'guesses and in {length}!\nThat\'s amazing!')
    elif n_of_guesses < 10 and length_minutes < 2:
        print(f'Correct, you\'ve guessed the right number in {n_of_guesses} '
              f'guesses! and in {length}!\nThat\'s average.')
    else:
        print(f'Correct, you\'ve guessed the right number in {n_of_guesses} '
              f'guesses! and in {length}!\nThat\'s not so good.')

def save_results(n_of_guesses, length):
    """
    Saves the result of current game into file.
    """
    sec = length.total_seconds()
    minutes, seconds = divmod(sec, 60)
    seconds = round(seconds)
    if minutes >= 1:
        entry = f'Number of guesses: {n_of_guesses} |, length: {minutes}m:' \
                f'{seconds}s'
    else:
        entry = f'Number of guesses: {n_of_guesses} |, length: {seconds}s'
    with open('results.txt', 'a') as f:
        f.write(entry)
        f.write('\n')

def history():
    """
    Prints the history of previous games.
    """
    with open('results.txt', 'r') as f:
        print('History of your games:')
        print('\n')
        for line in f:
            print(line)

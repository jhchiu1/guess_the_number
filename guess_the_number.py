import random

guesses = 0
correct = 'you guessed correctly!'
too_low = 'Too Low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    range1 = input("Please input range:\n>>")
    range2 = input("Please input range:\n>>")
    return range1, range2


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(int(low), int(high))


def get_guess():
    '''get user's guess'''
    while True:
        try:
            user_input = int(input('Guess the secret number? '))
            return user_input
        except Exception:
            print("Please enter a whole number.")
            continue
	


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
        guess += 1
    if guess > secret:
        return too_high
        guess += 1

    print('You were able to guess in' + guesses + 'tries!').format(configure_range, guesses)

def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break


if __name__ == '__main__':
    main()

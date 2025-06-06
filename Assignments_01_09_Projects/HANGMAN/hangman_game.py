
import random
from hangman.words import words  # Ab kaam karega

# ... (same code as above starting from get_valid_word)
# Word list directly in main file
words = [
    'apple', 'banana', 'python', 'game',
    'computer', 'mobile', 'keyboard',
    'mouse', 'laptop', 'internet'
]

def get_valid_word(all_words):
    word = random.choice(all_words)
    while ' ' in word or '-' in word:
        word = random.choice(all_words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('\n--- Hangman Game ---')
        print(f'Lives Left: {lives}')
        print('Used Letters:', ' '.join(used_letters))
        
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print('Word:', ' '.join(word_display))
        
        user_guess = input('Guess a letter: ').upper()
        
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                print('Correct! ✅')
            else:
                lives -= 1
                print('Wrong! ❌')
        elif user_guess in used_letters:
            print('You already guessed this letter!')
        else:
            print('Invalid guess! Only A-Z letters allowed.')

    if lives == 0:
        print(f'\nGame Over! 😢 The word was: {word}')
    else:
        print(f'\nYou Won! 🎉 The word was: {word}')

if __name__ == '__main__':
    hangman()
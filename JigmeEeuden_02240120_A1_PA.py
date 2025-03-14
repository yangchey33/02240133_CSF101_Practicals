
import random

def prime_sum():
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True 
        if n % 2 == 0:
            return False
        i = 3 
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2 
            return True
        

    start = int(input("Enter range to start: "))
    finish = int(input("Enter range to end: "))
    prime_sum = 0
    for num in range(start, finish + 1):
        if is_prime(num):
            prime_sum += num

    print(f"The sum of prime numbers between {start} and {finish} is: {prime_sum}")


def length_converter():

    
    def meters_to_feet(meters):
        return round(meters * 3.28084, 2)
    
    def feet_to_meters(feet):
        return round(feet / 3.28084, 2)
    
    value = float(input("Enter the length value: "))
    units = input("Enter 'M' for meters to feet or 'F' for feet to meters: ").upper()
    
    if units == 'M':
        result = meters_to_feet(value)
        print(f"{value} meters = {result:.2f} feet")
    elif units == 'F':
        result = feet_to_meters(value)
        print(f"{value} feet = {result} meters")
    else:
        print("Invalid units! Please enter 'M' or 'F'.")





def consonants_counter():

    text = input("Enter a string: ")
    consonant = 0
    for character in text:
        if ('a' <= character <= 'z') or ('A' <= character <= 'Z'):
             if character not in 'aeiouAEIOU':
                 consonant += 1
    
    print(f"The number of consonants is: {consonant}")



def min_max_finder():
    digits = []
    while True:
        user = input('Enter a list of numbers separated by commas (or "done" to finish): ')
        if user.lower() == 'done':
            break
        digits = user.split(',')
        try:
            value = [float(num) for num in digits]
        except ValueError:
            print("Invalid input. Please enter a list of numbers separated by commas.")
            continue
        if value:
            min_num = min(value)
            max_num = max(value)
            print(f"The minimum number is: {min_num}")
            print(f"The maximum number is: {max_num}")
        else:
            print("No value were entered.")



def palindrome_checker():
    palindrome_string = input("Enter a word: ").strip()
    text = palindrome_string.lower().replace(" ", "")
    inversed = ""
    for character in text:
        inversed = character + inversed
    is_palindrome = (text == inversed)
    
    if is_palindrome:
        print(f"'{palindrome_string}' is a palindrome!")
    else:
        print(f"'{palindrome_string}' is not a palindrome.")
  
    
palindrome_checker()

    

def words_counter():

    target_words = ["the" "was" "and"]
    word_counts = {word: 0 for word in target_words}
    file_path = input('enter the path to the text file:')
    try:
        with open(file_path,'r') as file:
            text = file.read().lower()
            words = text.split()
            word_count = len(words)
            print(f'the number of words in the file contains {word_count} words')


            for word in words:
                clean_word = "".join(char for char in word if char.isalnum())
                if clean_word in target_words:
                    word_counts[clean_word] += 1

            for word, count in word_counts.items():
                print(f'The word "{word}" appears {count} times')
    except FileNotFoundError:
        print('file not found')



def main():
    while True:
        print("\n___menu bar___")
        print('1.sum of prime numbers')
        print('2.unit converter')
        print('3.consonants counter')
        print('4.minimum_maximum')
        print('5.palindrome checker')
        print('6.words counter')
        print('7.exiting...')

        option = input('Enter a number (1-7):')

        if option == "1":
            prime_sum()

        elif option == "2":
            length_converter()

        elif option == "3":
            consonants_counter()

        elif option == "4":
            min_max_finder()

        elif option == "5":
            palindrome_checker()

        elif option == "6":
            words_counter()

        elif option == "7":
            print("exiting...")
            break 
        else:
            print('Invalid. Please enter number (1-7)')

if __name__ == '__main__':
    main()        
        

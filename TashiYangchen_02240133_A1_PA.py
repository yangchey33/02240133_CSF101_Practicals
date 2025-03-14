
#Function1
#Prme number sum calculator

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
        

    begin = int(input("Enter range to start: "))
    end = int(input("Enter range to end: "))
    prime_sum = 0
    for num in range(begin, end + 1):
        if is_prime(num): #checking if the number is prime or not
            prime_sum += num #adding prime numter to the sum

    print(f"The sum of prime numbers between {begin} and {end} is: {prime_sum}")


#Function 2
#Length unit conversion
def length_converter(value, direction):
    
    if direction not in ['M', 'F']:
        raise ValueError("Direction must be 'M' for meters to feet or 'F' for feet to meters.")
    
    if direction == 'M':
        return round(value * 3.28084, 2)  # changing Meters to Feet
    else:
        return round(value / 3.28084, 2)  # changing Feet to Meters


# Function 3
# Consonant Counter
def consonants_counter():

    text = input("Enter a string: ")
    consonant = 0
    for character in text:
        if ('a' <= character <= 'z') or ('A' <= character <= 'Z'):
             if character not in 'aeiouAEIOU':
                 consonant += 1

#Function 4
#Min-Max number finder
def min_max_finder():
    num = []
    while True:
        user = input('Enter a list of numbers separated by commas (or "done" to finish): ')
        if user.lower() == 'done':
            break
        num = user.split(',')
        try:
            value = [float(num) for num in num]
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
    
   
#Function 5
#Palindrome checker
def is_palindrome(words):
    
    fresh_text = ''.join(charater.lower() for charater in words if charater.isalnum()) #removing spaces and converting to lowercase

    return fresh_text == fresh_text[::-1]

#Function 6
#Word counter
def words_counter():

    aim_words = ["the" "was" "and"]   #word count
    word_counts = {word: 0 for word in aim_words} 
    doc_path = input('enter the path to the text file:') #path to file
    try:
        with open(doc_path,'r') as file:
            text = file.read().lower()
            words = text.split()
            word_count = len(words)
            print(f'the number of words in the file contains {word_count} words')


            for word in words:
                clean_word = "".join(char for char in word if char.isalnum())
                if clean_word in aim_words:
                    word_counts[clean_word] += 1

            for word, count in word_counts.items():    
                print(f'The word "{word}" appears {count} times')  #printing the word and its count
    except FileNotFoundError:
        print('file not found')

#main function program
def main():
    
    while True:
        print("\nSelect a function:")
        print("1. Prime Number Sum Calculator")
        print("2. Length Unit Converter")
        print("3. Consonant Counter")
        print("4. Min-Max Number Finder")
        print("5. Palindrome Checker")
        print("6. Word Counter")
        print("7. Exit")

        option = input("Enter your choice (1-7): ")

        
        if option == "1":
            prime_sum()
    
        elif option == "2":
            value = float(input("Enter the length value: "))
            direction = input("Enter direction (M for meters to feet, F for feet to meters): ")
            print(f"Converted length: {length_converter(value, direction)}")

        elif option == "3":
            consonants_counter()

        elif option == "4":
          min_max_finder()

        elif option == "5":
          words = input("Enter a text string: ")
          print(f"Is palindrome: {is_palindrome(words)}")
 
        elif option == "6":
          words_counter()

        elif option == "7":
            print("Exiting ...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()
def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(start, end):
    """Calculates the sum of prime numbers within a range."""
    if start > end:
        return "Invalid range: start must be less than or equal to end."
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return sum(primes)

def length_converter(value, direction):
    """Converts length units (meters to feet or feet to meters)."""
    if direction.upper() == 'M':
        return round(value * 3.28084, 2)
    elif direction.upper() == 'F':
        return round(value / 3.28084, 2)
    else:
        return "Invalid direction. Use 'M' for meters to feet or 'F' for feet to meters."

def consonant_count(text):
    """Counts the number of consonants in a string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

def min_max_finder(numbers):
    """Finds the minimum and maximum numbers in a list."""
    if not numbers:
        return "No numbers provided."
    return f"Smallest: {min(numbers)}, Largest: {max(numbers)}"

def is_palindrome(text):
    """Checks if a string is a palindrome (ignoring spaces and case)."""
    processed_text = "".join(char.lower() for char in text if char.isalnum())
    return processed_text == processed_text[::-1]

def word_counter(filename):
    """Counts the occurrences of specific words in a file."""
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            words_to_count = ["the", "was", "and"]
            counts = {word: text.split().count(word) for word in words_to_count}
            return counts
    except FileNotFoundError:
        return "File not found."

def get_numbers_from_user():
    """Gets a series of numbers from the user."""
    try:
        count = int(input("How many numbers do you want to enter? "))
        if count <= 0:
            return "Please enter a positive integer."
        numbers = []
        for i in range(count):
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
        return numbers
    except ValueError:
        return "Invalid input. Please enter numbers only."

def main():
    """Main program loop."""
    while True:
        print("\nSelect a function (1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("0. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                start = int(input("Enter start range: "))
                end = int(input("Enter end range: "))
                result = sum_primes(start, end)
                print(f"Sum of primes: {result}")
            except ValueError:
                print("Invalid input. Please enter integers.")
        elif choice == '2':
            try:
                value = float(input("Enter value: "))
                direction = input("Enter direction (M/F): ")
                result = length_converter(value, direction)
                print(f"Converted length: {result}")
            except ValueError:
                print("Invalid input. Please enter a number for the value.")
        elif choice == '3':
            text = input("Enter a string: ")
            result = consonant_count(text)
            print(f"Number of consonants: {result}")
        elif choice == '4':
            numbers = get_numbers_from_user()
            if isinstance(numbers, list):
                result = min_max_finder(numbers)
                print(result)
            else:
                print(numbers)
        elif choice == '5':
            text = input("Enter a string: ")
            result = is_palindrome(text)
            print(f"Is palindrome: {result}")
        elif choice == '6':
            filename = "sample_text.txt" #Make sure the file is in the same directory.
            result = word_counter(filename)
            if isinstance(result, dict):
                for word, count in result.items():
                    print(f'{word}: {count}')
            else:
                print(result)
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 0-6.")

        continue_choice = input("Would you like to try another function? (y/n): ")
        if continue_choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
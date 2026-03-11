# Problem 0: Example
def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")
print_greeting()

# Problem 1: Vowel or consonant
def check_letter():
    # 1. Prompt the user for input
    letter = input("Enter a letter (a-z): ")

    # 2. Basic validation: ensure it's a single letter
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single valid letter.")
        return

    # 3. Check logic using .lower() and 'in'
    if letter.lower() in 'aeiou':
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

# Call the function at the bottom of your script to run it
check_letter()

# Problem 2: Old enough to vote?
def check_voting_eligibility():
    # 1. Prompt for age and convert to an integer
    try:
        age = int(input("Enter your age: "))
        
        # 2. Check the condition
        if age >= 18:
            print("You are eligible to vote!")
        else:
            print(f"You are not eligible to vote. You must be 18, but you are {age}.")
            
    except ValueError:
        # 3. Handle cases where the user types something that isn't a number
        print("Invalid input. Please enter your age as a whole number.")

# Uncomment the line below to test this specific function
check_voting_eligibility()

# Problem 3: Calculate dog years
def calculate_dog_years():
    try:
        years = int(input("Input a dog's age in human years: "))
        
        if years < 0:
            print("Age cannot be negative.")
        elif years <= 2:
            dog_years = years * 10.5
            print(f"The dog's age in dog years is {dog_years}")
        else:
            # First 2 years = 21 (10.5 * 2), then 4 years for every year after
            dog_years = 21 + (years - 2) * 4
            print(f"The dog's age in dog years is {dog_years}")
            
    except ValueError:
        print("Please enter a valid number.")

# To test, uncomment the line below:
calculate_dog_years()

# Problem 4: Weather advice
def weather_advice():
    # 1. Ask the user for input
    is_cold = input("Is it cold outside? (yes/no): ").lower()
    is_raining = input("Is it raining outside? (yes/no): ").lower()

    # 2. Check the conditions
    if is_cold == "yes" and is_raining == "yes":
        print("Wear a waterproof coat, scarf, and gloves.")
    elif is_cold == "yes" and is_raining == "no":
        print("Wear a warm coat and maybe a scarf.")
    elif is_cold == "no" and is_raining == "yes":
        print("Take an umbrella.")
    else:
        print("It's a nice day, no extra gear needed!")

# Uncomment the line below to test
weather_advice()

# Problem 5: What’s the season?
def determine_season():
    month = input("Enter the month (e.g., Jan, Feb, Mar): ").lower()
    day = int(input("Enter the day: "))

    # Define seasons
    # Winter: Dec 21 - Mar 19
    # Spring: Mar 20 - Jun 20
    # Summer: Jun 21 - Sep 21
    # Fall:   Sep 22 - Dec 20

    if (month == 'dec' and day >= 21) or (month in ['jan', 'feb']) or (month == 'mar' and day < 20):
        print(f"{month.capitalize()} {day} is in Winter.")
    elif (month == 'mar' and day >= 20) or (month in ['apr', 'may']) or (month == 'jun' and day < 21):
        print(f"{month.capitalize()} {day} is in Spring.")
    elif (month == 'jun' and day >= 21) or (month in ['jul', 'aug']) or (month == 'sep' and day < 22):
        print(f"{month.capitalize()} {day} is in Summer.")
    elif (month == 'sep' and day >= 22) or (month in ['oct', 'nov']) or (month == 'dec' and day < 21):
        print(f"{month.capitalize()} {day} is in Fall.")
    else:
        print("Invalid date input.")

# To test, uncomment the line below:
determine_season()
